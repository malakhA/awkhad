awkhad.define('web.FieldManagerMixin', function (require) {
"use strict";

/**
 * The FieldManagerMixin is a mixin, designed to do the plumbing between field
 * widgets and a basicmodel.  Field widgets can be used outside of a view.  In
 * that case, someone needs to listen to events bubbling up from the widgets and
 * calling the correct methods on the model.  This is the field_manager's job.
 */

var BasicModel = require('web.BasicModel');
var concurrency = require('web.concurrency');

var FieldManagerMixin = {
    custom_events: {
        field_changed: '_onFieldChanged',
        load: '_onLoad',
        mutexify: '_onMutexify',
    },
    /**
     * A FieldManagerMixin can be initialized with an instance of a basicModel.
     * If not, it will simply uses its own.
     *
     * @param {BasicModel} [model]
     */
    init: function (model) {
        this.model = model || new BasicModel(this);
        this.mutex = new concurrency.Mutex();
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * Apply changes by notifying the basic model, then saving the data if
     * necessary, and finally, confirming the changes to the UI.
     *
     * @todo find a way to remove ugly 3rd argument...
     *
     * @param {string} dataPointID
     * @param {Object} changes
     * @param {AwkhadEvent} event
     * @returns {Deferred} resolves when the change has been done, and the UI
     *   updated
     */
    _applyChanges: function (dataPointID, changes, event) {
        var self = this;
        var options = _.pick(event.data, 'context', 'doNotSetDirty', 'notifyChange', 'viewType', 'allowWarning');
        return this.model.notifyChanges(dataPointID, changes, options)
            .then(function (result) {
                if (event.data.force_save) {
                    return self.model.save(dataPointID).then(function () {
                        return self._confirmSave(dataPointID);
                    }).fail(function () {
                        return self._rejectSave(dataPointID);
                    });
                } else if (options.notifyChange !== false) {
                    return self._confirmChange(dataPointID, result, event);
                }
            });
    },
    /**
     * This method will be called whenever a field value has changed (and has
     * been confirmed by the model).
     *
     * @abstract
     * @param {string} id basicModel Id for the changed record
     * @param {string[]} fields the fields (names) that have been changed
     * @param {AwkhadEvent} event the event that triggered the change
     * @returns {Deferred}
     */
    _confirmChange: function (id, fields, event) {
        return $.when();
    },
    /**
     * This method will be called whenever a save has been triggered by a change
     * in some controlled field value.  For example, when a priority widget is
     * being changed in a readonly form.
     *
     * @see _onFieldChanged
     * @abstract
     * @param {string} id The basicModel ID for the saved record
     * @returns {Deferred}
     */
    _confirmSave: function (id) {
        return $.when();
    },
    /**
     * This method will be called whenever a save has been triggered by a change
     * and has failed. For example, when a statusbar button is clicked in a
     * readonly form view.
     *
     * @abstract
     * @private
     * @param {string} id The basicModel ID for the saved record
     * @returns {Deferred}
     */
    _rejectSave: function (id) {
        return $.when();
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * This is the main job of the FMM: deciding what to do when a controlled
     * field changes.  Most of the time, it notifies the model that a change
     * just occurred, then confirm the change.
     *
     * @param {AwkhadEvent} event
     */
    _onFieldChanged: function (event) {
        // in case of field changed in relational record (e.g. in the form view
        // of a one2many subrecord), the field_changed event must be stopped as
        // soon as is it handled by a field_manager (i.e. the one of the
        // subrecord's form view), otherwise it bubbles up to the main form view
        // but its model doesn't have any data related to the given dataPointID
        event.stopPropagation();
        this._applyChanges(event.data.dataPointID, event.data.changes, event)
            .done(event.data.onSuccess || function () {})
            .fail(event.data.onFailure || function () {});
    },
    /**
     * Some widgets need to trigger a reload of their data.  For example, a
     * one2many with a pager needs to be able to fetch the next page.  To do
     * that, it can trigger a load event. This will then ask the model to
     * actually reload the data, then call the on_success callback.
     *
     * @param {AwkhadEvent} event
     * @param {number} [event.data.limit]
     * @param {number} [event.data.offset]
     * @param {function} [event.data.on_success] callback
     */
    _onLoad: function (event) {
        var self = this;
        event.stopPropagation(); // prevent other field managers from handling this request
        var data = event.data;
        if (!data.on_success) { return; }
        var params = {};
        if ('limit' in data) {
            params.limit = data.limit;
        }
        if ('offset' in data) {
            params.offset = data.offset;
        }
        this.mutex.exec(function () {
            return self.model.reload(data.id, params).then(function (db_id) {
                data.on_success(self.model.get(db_id));
            });
        });
    },
    /**
     * @private
     * @param {AwkhadEvent} ev
     * @param {function} ev.data.action the function to execute in the mutex
     */
    _onMutexify: function (ev) {
        ev.stopPropagation(); // prevent other field managers from handling this request
        this.mutex.exec(ev.data.action);
    },
};

return FieldManagerMixin;
});
