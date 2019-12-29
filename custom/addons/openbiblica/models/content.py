from awkhad import api, fields, models

class Contents(models.Model):

    _name = "open.content"
    _description = "Contents"
    _inherit = ['mail.thread', 'website.seo.metadata', 'website.multi.mixin']
    _order = "sequence"

    name = fields.Char(string="Section Name", required=True)
    description = fields.Text('Description')
    title_id = fields.Char(string="File Identifier")
    title_ide = fields.Char(string="Encoding specification")
    title = fields.Char(string="Section Title")
    title_short = fields.Char(string="Section Short")
    title_abrv = fields.Char(string="Section Abbreviation")
    sequence = fields.Integer('Sequence')
    status = fields.Selection([
        ('draft', 'First Draft'),
        ('team', 'Team Draft'),
        ('review', 'Reviewed Draft'),
        ('clean', 'Clean Text')
    ], string='Status', track_visibility='onchange', help='Status of this content', default='draft')

    bundle = fields.Selection([
        ('old', 'Old Testament'),
        ('deu', 'Deuterokanonika'),
        ('new', 'New Testament'),
        ('no', 'None')
    ], string='Bundle', track_visibility='onchange', help='Bible bundle of this content')

    biblica_id = fields.Many2one('open.biblica', 'Biblica Project')
    part_ids = fields.One2many('open.part', 'content_id', string='Parts in this Content', ondelete='cascade')
    line_ids = fields.One2many('open.line', 'content_id', string='Lines in this Content', ondelete='cascade')

    lang_id = fields.Many2one(related='biblica_id.lang_id')
    lang_help_id = fields.Many2one('res.lang', 'Help Language')

    create_id = fields.Many2one('res.users', string='Author', index=True)
    team_ids = fields.Many2many('res.users', string='colaborators')
    approver_ids = fields.Many2many('res.users', string='approvers')

    create_date = fields.Datetime('Started on', index=True, readonly=True)
    write_date = fields.Datetime('Updated on', index=True, readonly=True)

    active = fields.Boolean(default=True)
    open_project = fields.Boolean(default=True)
    forum_id = fields.Many2one(related='biblica_id.forum_id')
    post_ids = fields.One2many('forum.post', 'content_id', string='Comments')

    reputation = fields.Integer('Reputation')
    reputation_total = fields.Integer('Reputation Total')
    favourite_ids = fields.Many2many('res.users', string='Favourite')
    favourite_count = fields.Integer('Favorite Count')
    views = fields.Integer('Views')

    files = fields.Binary('File Attachment', attachment=True)
    rest = fields.Binary('Undone File Attachment', attachment=True)

    source_ids = fields.Many2many('open.content', 'content_source_ids_rel', 'source_id', 'derivative_id',
                                  string='Sources')
    source_id = fields.Many2one('open.content', 'Main Source')

    is_transcription = fields.Boolean('Transcription')
    manuscript_ids = fields.Many2many('slide.slide', string='Manuscript Sources')
    manuscript_id = fields.Many2one('slide.slide', string='Main Manuscript Source')






