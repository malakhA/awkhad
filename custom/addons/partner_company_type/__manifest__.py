# Copyright 2017-2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner Company Type',
    'summary': 'Adds a company type to partner that are companies',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/partner-contact',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/res_partner_company_type.xml',
        'views/res_partner_company_type.xml',
        'views/res_partner.xml',
    ],
    'demo': [
        'demo/res_partner_company_type.xml',
    ],
}
