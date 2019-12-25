# Copyright (C) 2019 - TODAY, Patrick Wilson
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service - CRM',
    'version': '12.0.1.0.1',
    'summary': 'Create Field Service orders from the CRM',
    'category': 'Field Service',
    'author': 'Patrick Wilson, Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/field-service',
    'depends': [
        'fieldservice',
        'crm',
    ],
    'data': [
        'views/crm_lead.xml',
        'views/fsm_location.xml',
        'views/fsm_order.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': [
        'patrickrwilson',
    ],
    'installable': True,
}
