{
    'name': "Web Widget Plotly",
    'summary': """Allow to draw plotly charts.""",
    'description': """Allow to draw plotly charts.""",
    'author': "LevelPrime srl, "
              "Awkhad Community Association (ACA)",
    "website": "https://github.com/ACA/web",
    'category': 'Web',
    'version': '12.0.1.0.0',
    'depends': ['web'],
    'data': [
        'views/web_widget_plotly_chart.xml',
    ],
    "external_dependencies": {
        "python": ['plotly'],
    },
    "auto_install": False,
    "license": "LGPL-3",
}
