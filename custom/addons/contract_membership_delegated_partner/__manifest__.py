# Copyright 2017-18 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Contract Membership Delegate Partner',
    'version': '12.0.1.0.0',
    'category': 'Membership',
    'author': 'Tecnativa, '
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/oca/vertical-association',
    'license': 'AGPL-3',
    'summary': 'Set delegate membership on the contract',
    'depends': [
        'membership_delegated_partner',
        'contract',
    ],
    'data': [
        'views/contract.xml',
    ],
    'installable': True,
}
