# -*- coding: utf-8 -*-
{
    'name': 'Importar Imagenes',
    'version': '1.0',
    'summary': """ Módulo que permite importar imagenes a cualquier modelo,
                    ubicando un campo de referencia.""",
    'author': 'Breithner Aquituari',
    'website': '',
    'category': '',
    'depends': ['base', ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/image_import.xml"
    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
