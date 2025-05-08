# -*- coding: utf-8 -*-
{
    'name': 'Contacts File IA',
    'version': '1.0',
    'summary': """ Módulo que permite subir adjuntos y luego ser analizado por IA y extraer el contenido """,
    'author': 'Breithner Aquituari',
    'website': '',
    'category': '',
    'depends': ['base', 'contacts'],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_ai_settings_views.xml",
        "views/partner_document_views.xml",
        "views/res_partner_views.xml"
    ],

    'external_dependencies' : {
        'python' : ['openai==0.28','python-docx','PyMuPDF','numpy','tiktoken'],
    },
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}


# instalar 
# pip install openai
