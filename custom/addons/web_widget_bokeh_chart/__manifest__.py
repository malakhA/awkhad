# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Web Widget Bokeh Chart",
    "category": "Hidden",
    "summary": "This widget allows to display charts using Bokeh library.",
    "author": "Eficent, "
              "Awkhad Community Association (ACA)",
    "version": "12.0.1.0.1",
    "maintainers": ["lreficent"],
    "development_status": "Production/Stable",
    "website": "https://github.com/ACA/web",
    "depends": ["web"],
    "data": [
        "views/web_widget_bokeh_chart.xml",
    ],
    "external_dependencies": {
        "python": ['bokeh'],
    },
    "auto_install": False,
    "license": "LGPL-3",
}
