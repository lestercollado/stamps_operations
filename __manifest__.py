# -*- coding: utf-8 -*-
{
    'name': "Sellos Operaciones",

    'summary': "Módulo para la gestión de entrega/recepción sellos de la Dirección de Operaciones.",

    'description': """
        Breve descripción
    """,

    'author': "Dirección de Operaciones",
    'website': "https://tcmariel.cu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Stamps',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/stamps_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}

