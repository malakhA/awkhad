from awkhad import api, fields, models

class Parts(models.Model):

    _name = "open.part"
    _description = "Parts"
    _inherit = ['mail.thread', 'website.seo.metadata', 'website.multi.mixin']
    _order = "sequence"

    name = fields.Char(string="Part Name", required=True)
    description = fields.Text('Description')
    sequence = fields.Integer('Sequence')

    parent_id = fields.Many2one('open.part', string='Parent Part')
    children_ids = fields.One2many('open.part', 'parent_id', string='Children Parts')

    content_id = fields.Many2one('open.content', string='Section')
    biblica_id = fields.Many2one(related='content_id.biblica_id')
    line_ids = fields.One2many('open.line', 'part_id', string='Lines', ondelete='cascade')
    attachment = fields.Binary('Attachment', attachment=True)

    lang_id = fields.Many2one(related='content_id.lang_id')
    lang_help_id = fields.Many2one('res.lang', 'Help Language')

    create_id = fields.Many2one('res.users', string='Author', index=True)
    team_ids = fields.Many2many('res.users', string='colaborators')
    approver_ids = fields.Many2many('res.users', string='approvers')

    create_date = fields.Datetime('Started on', index=True, readonly=True)
    write_date = fields.Datetime('Updated on', index=True, readonly=True)

    active = fields.Boolean(default=True)
    open_project = fields.Boolean(default=True)
    forum_id = fields.Many2one(related='biblica_id.forum_id')
    post_ids = fields.One2many('forum.post', 'part_id', string='Comments')

    reputation = fields.Integer('Reputation')
    reputation_total = fields.Integer('Reputation Total')
    favourite_ids = fields.Many2many('res.users', string='Favourite')
    favourite_count = fields.Integer('Favorite Count')
    views = fields.Integer('Views')

    source_ids = fields.Many2many('open.part', 'part_source_ids_rel', 'source_id', 'derivative_id',
                                  string='Sources')
    source_id = fields.Many2one('open.part', 'Main Source')

    is_transcription = fields.Boolean('Transcription')
    manuscript_ids = fields.Many2many('slide.slide', string='Manuscript Sources')
    manuscript_id = fields.Many2one('slide.slide', string='Main Manuscript Source')


