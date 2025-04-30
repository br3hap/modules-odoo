# -*- coding: utf-8 -*-
{
    'name': 'Product visibility on website sale',
    'version': '1.0',
    'summary': """ Módulo que permite la visibilidad por variantes de productos en el sitio web """,
    'author': 'Breithner Aquituari',
    'website': '',
    'category': '',
    'depends': ['base', 'website_sale' ],
    "data": [
        "views/res_partner_views.xml"
    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
