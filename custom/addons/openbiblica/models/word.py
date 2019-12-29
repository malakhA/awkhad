from awkhad import api, fields, models

class Words(models.Model):

    _name = "open.word"
    _description = "Words"
    _inherit = ['mail.thread', 'website.seo.metadata', 'website.multi.mixin']
    _order = "name"

    name = fields.Char('name', required=True)
    description = fields.Text('Description')
    lang_id = fields.Many2one('res.lang', 'Language', required=True)
    trans_ids = fields.Many2many('open.word', 'trans_ids_rel', 'origin_id', 'translate_id', string='Translation')

    create_id = fields.Many2one('res.users', string='Author', index=True)
    write_id = fields.Many2one('res.users', string='Editor', index=True)

    create_date = fields.Datetime('Started on', index=True, readonly=True)
    write_date = fields.Datetime('Updated on', index=True, readonly=True)

    active = fields.Boolean(default=True)

    forum_id = fields.Many2one('forum.forum', string='Discussion Forum')
    post_ids = fields.One2many('forum.post', 'biblica_id', string='Comments')

