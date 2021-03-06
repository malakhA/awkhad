# Copyright 2014-2015 Tecnativa S.L. - Jairo Llopis
# Copyright 2016 Tecnativa S.L. - Vicent Cubells
# Copyright 2017 Tecnativa S.L. - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Partner Contact Department',
    "summary": "Assign contacts to departments",
    'version': '12.0.1.0.0',
    'category': 'Customer Relationship Management',
    'author': 'Tecnativa, '
              'Awkhad Community Association (ACA)',
    "license": "AGPL-3",
    'website': 'https://github.com/ACA/partner-contact',
    "application": False,
    'depends': [
        'contacts',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_department_view.xml',
        'views/res_partner_view.xml',
    ],
    "installable": True,
}
