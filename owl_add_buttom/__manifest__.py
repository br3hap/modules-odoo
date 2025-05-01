# -*- coding: utf-8 -*-
{
    'name': 'Owl add button',
    'version': '1.0',
    'summary': """ Modulo que permite colocar un boton en la vista tree y kanban mediante owl """,
    'author': 'Breithner Aquituari',
    'website': '',
    'category': '',
    'depends': ['base', 'web', 'product' ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
        "wizards/productt_price_wizard.xml"
    ],
    'assets': {
        'web.assets_backend': [
            'owl_add_buttom/static/**/*',

        ]
    },
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
