# -*- coding: utf-8 -*-
{
    'name': 'Agregar registros al inicio',
    'version': '1.0',
    'summary': """ Módulo que permite colocar la funcion de agregar linea en la parte inicial 
                    de la vista tree en los detalles de una vista form """,
    'author': 'Breithner Aquituari',
    'website': '',
    'category': 'Web',
    'depends': ['web','base' ],
    "data": [
        "views/res_users_views.xml"
    ],

    'assets': {
        'web.assets_backend': [
            'list_add_record_start/static/src/views/**/*',
        ]
    },

    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
