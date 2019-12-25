# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author: Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Point Of Sale - Invoicing',
    'summary': 'Handle invoicing from Point Of Sale',
    'version': '12.0.3.0.0',
    'category': 'Point of Sale',
    'author': 'GRAP, Awkhad Community Association (ACA)',
    'website': 'http://www.github.com/ACA/pos',
    'license': 'AGPL-3',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'views/view_account_invoice.xml',
    ],
    'installable': True,
}
