# Copyright 2017 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Maintenance Equipments Scrap',
    'summary': 'Enhance the functionality for Scrapping Equipments',
    'author': 'Onestein, Awkhad Community Association (ACA)',
    'website': 'http://github.com/ACA/maintenance',
    'category': 'Human Resources',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'maintenance',
        'mail',
    ],
    'data': [
        'views/maintenance_equipment.xml',
        'views/maintenance_equipment_category.xml',
        'wizard/scrap_equipment.xml',
        'data/maintenance_data.xml',
    ],
}
