# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'web_widget_x2many_2d_matrix example',
    'summary': "A small example on how to use `web_widget_x2many_2d_matrix`.",
    "version": "12.0.1.1.0",
    "author": "Camptocamp, "
              "Awkhad Community Association (ACA)",
    "website": "https://github.com/ACA/web",
    "license": "AGPL-3",
    "category": "Hidden/Dependency",
    "depends": [
        'web_widget_x2many_2d_matrix',
    ],
    "data": [
        'security/ir.model.access.csv',
        'demo/x2m.demo.csv',
        'views/x2m_demo.xml',
        'wizard/x2m_matrix.xml',
    ],
    "installable": True,
}
