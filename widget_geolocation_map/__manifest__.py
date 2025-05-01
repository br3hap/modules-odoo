# -*- coding: utf-8 -*-
{
    'name': 'Widget Geolocation LeaFlet',
    'version': '1.0',
    'summary': """ Modulo que agrega un widgwet de geolocalizacion, utilizando leaflet """,
    'author': 'Breithner Aquituari',
    'website': '',
    'category': '',
    'depends': ['base', ],
    "data": [
        "views/res_partner_views.xml"
    ],

    'assets': {
        'web.assets_backend': [
            'widget_geolocation_map/static/src/**/*'
        ],
    },
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
