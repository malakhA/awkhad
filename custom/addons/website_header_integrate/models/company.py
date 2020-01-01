# -*- coding: utf-8 -*-


from awkhad import api, fields, models



class WebsiteInsertionLine(models.Model):
    _name = 'website.insertion.line'
    _description = 'Insert Code in Web pages header'

    name = fields.Char('Name')
    description = fields.Char('Description')
    code = fields.Text('Code', help="Pase code here")
    company_id = fields.Many2one('res.company')




class Company(models.Model):
    _inherit = 'res.company'

    website_insertion_ids = fields.One2many('website.insertion.line','company_id', 'Add code to Website Header', help="Create record and add integration code to code field")
