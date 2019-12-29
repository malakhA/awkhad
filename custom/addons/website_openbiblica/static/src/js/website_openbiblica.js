awkhad.define('website_openbiblica.website_openbiblica', function (require) {
'use strict';

    require('web.dom_ready');
    var ajax = require('web.ajax');
    var core = require('web.core');

    var _t = core._t;

    var lastsearch;


//    $('.o_lngs').ready(function(){
//            ajax.jsonRpc('/get/langs', 'call', {
//            }).then(function (lngs) {
//            console.log(lngs);
//            var select = $("select[name='lng_id']");
//            var i;
//            for (i = 0; i < lngs.length; i++) {
//                select.append('<option value="' + lngs[i][0] + '"><t t-esc="' + lngs[i][0] + '" /></option>');
//            };
//            $("t[id='languages']").foreach = data['lngs'];
//            var id = data['id'];
//            var name = data['name'];
//            var langs = data['lngs'];
//            var lngs = langs[0];
//            var lngs = data['lngs'];
//            var select = $("select[name='lng_id']");
//
//            var i;
//            for (i = 0; i < lngs.length; i++) {
//                select.append('<option value="' + lngs[i].id + '"><t t-esc="' + lngs[i].name + '" /></option>');
//            };
//            select.append('<t t-foreach="' + lngs + '" t-as="language"><option t-att-value="language.id"><t t-esc="language.name" /></option></t>').change();
//            select.append('<option value=" ">Coba Keluar gak</option>');
//        });
//    });

//    if ($('.o_content_view').length) {
//        $('.o_content_view').ready(function(){
//            var parts = $("input[id='parts']");
//            console.log(parts)
////            for (i = 0; i < parts; i++) {
//            $("table[id='content']").append(
//            '<tr><td>Test</td></tr>'
//            );
////            };
//        });
//    }

    $('.o_install_next').ready(function(){
        $("#install_next_button").click();
    });

    if ($('.o_biblica_source').length) {
        var biblica_option = $("select[name='bib_id']:enabled option:not(:first)");

        $('.o_biblica_source').on('change', "select[name='lng_id']", function () {
            var biblica_select = $("select[name='bib_id']");
            biblica_option.detach();
            var displayed_source = biblica_option.filter("[data-lang_id="+($(this).val() || 0)+"]");
            var nb = displayed_source.appendTo(biblica_select).show().size();
            biblica_select.parent().toggle(nb>=1);
            });

        $('.o_biblica_source').on('change', "select[name='bib_id']", function () {
            $("span[name='add_source_button']").toggle();
        });

        $('.o_biblica_source').find("select[name='lng_id']").change();
        $('.o_biblica_source').find("select[name='bib_id']").change();
    }

    if ($('.o_content_source').length) {
        var biblica_options = $("select[name='bib_id']:enabled option:not(:first)");
        var content_options = $("select[name='con_id']:enabled option:not(:first)");
        
        $('.o_content_source').ready(function () {
            var select_lng_id = $("select[name='lng_id']");
            var select_con_id = $("select[name='con_id']");
            content_options.detach();
            var displayed_con_id = content_options.filter("[data-lng_id="+($(select_lng_id).val() || 0)+"]");
            var nb_con_id = displayed_con_id.appendTo(select_con_id).show().size();
            select_con_id.parent().toggle(nb_con_id>=1);
        });
        
        $('.o_content_source').on('change', "select[name='lng_id']", function () {
            var select_bib_id = $("select[name='bib_id']");
            var select_con_id = $("select[name='con_id']");
            biblica_options.detach();
            content_options.detach();
            var displayed_bib_id = biblica_options.filter("[data-lng_id="+($(this).val() || 0)+"]");
//            var displayed_con_id = content_options.filter("[data-lng_id="+($(this).val() || 0)+"]").filter("[data-bib_id="+($(select_bib_id).val() || 0)+"]");
            var displayed_con_id = content_options.filter("[data-bib_id="+($(select_bib_id).val() || 0)+"]");
            var nb_bib_id = displayed_bib_id.appendTo(select_bib_id).show().size();
            var nb_con_id = displayed_con_id.appendTo(select_con_id).show().size();
            select_bib_id.parent().toggle(nb_bib_id>=1);
            select_con_id.parent().toggle(nb_con_id>=1);
        });
        $('.o_content_source').on('change', "select[name='bib_id']", function () {
            var select_con_id = $("select[name='con_id']");
            content_options.detach();
            var displayed_con_id = content_options.filter("[data-bib_id="+($(this).val() || 0)+"]");
            var nb_con_id = displayed_con_id.appendTo(select_con_id).show().size();
            select_con_id.parent().toggle(nb_con_id>=1);
        });

        $('.o_content_source').on('change', "select[name='con_id']", function () {
            $("span[name='add_source_button']").toggle();
        });

        $('.o_content_source').find("select[name='lng_id']").change();
        $('.o_content_source').find("select[name='bib_id']").change();
        $('.o_content_source').find("select[name='con_id']").change();        

        $('.o_content_source').on('change', "select[name='src_id']", function () {
            $("#select_source").click();
        });
    }

    if ($('.o_editor').length) {
        $('.o_editor').on('click', "a[id='add_new']", function () {
            $("td[name='add_new']").show();
            $("a[id='add_new']").parent().hide();
            });

        $('.o_editor').on('click', "a[id='edit_mode']", function () {
            $("div[name='editor_menu']").show();
            $("tr[name='editor_menu']").show();
            $("td[name='editor_menu']").show();
            $("span[name='editor_menu']").show();
            $("a[id='edit_mode']").parent().hide();
            $("a[name='edit_hide']").hide();
            $("h1[name='edit_hide']").hide();
            $("td[name='edit_hide']").hide();
            });
        $('.o_editor').on('click', "a[id='close_editor_mode']", function () {
            $("div[name='editor_menu']").hide();
            $("tr[name='editor_menu']").hide();
            $("td[name='editor_menu']").hide();
            $("span[name='editor_menu']").hide();
            $("a[id='edit_mode']").parent().show();
            $("a[name='edit_hide']").show();
            $("h1[name='edit_hide']").show();
            $("td[name='edit_hide']").show();
            });
        $('.o_editor').on('click', "a[id='show_source']", function () {
            $("div[name='source_item']").show();
            $("tr[name='source_item']").show();
            $("td[name='source_item']").show();
            $("th[name='source_item']").show();
            $("span[name='source_item']").show();
            $("a[id='show_source']").parent().hide();
            $("a[name='hide_source']").hide();
            });
        $('.o_editor').on('click', "a[id='close_source']", function () {
            $("div[name='source_item']").hide();
            $("tr[name='source_item']").hide();
            $("td[name='source_item']").hide();
            $("th[name='source_item']").hide();
            $("span[name='source_item']").hide();
            $("a[id='show_source']").parent().show();
            $("a[name='hide_source']").show();
            });
    }

    $('textarea.load_editor').each(function () {
        var $textarea = $(this);
        var editor_karma = $textarea.data('karma') || 30;  // default value for backward compatibility
        if (!$textarea.val().match(/\S/)) {
            $textarea.val("<p><br/></p>");
        }
        var $form = $textarea.closest('form');
        var toolbar = [
                ['style', ['style']],
                ['font', ['bold', 'italic', 'underline', 'clear']],
                ['para', ['ul', 'ol', 'paragraph']],
                ['table', ['table']],
                ['history', ['undo', 'redo']],
            ];
        if (parseInt($("#karma").val()) >= editor_karma) {
            toolbar.push(['insert', ['link', 'picture']]);
        }
        $textarea.summernote({
                height: 150,
                toolbar: toolbar,
                styleWithSpan: false
            });

        // float-left class messes up the post layout OPW 769721
        $form.find('.note-editable').find('img.float-left').removeClass('float-left');
        $form.on('click', 'button, .a-submit', function () {
            $textarea.html($form.find('.note-editable').code());
        });
    });

});