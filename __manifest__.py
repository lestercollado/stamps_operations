# -*- coding: utf-8 -*-
{
    'name': "Sellos Operaciones",

    'summary': "Entrega/recepción sellos de la Dirección de Operaciones.",

    'description': """
        Módulo para la gestión de entrega/recepción sellos de la Dirección de Operaciones. \n
        Registrar quien recibe y entrega los sellos.
    """,

    'author': "Dirección de Operaciones",
    'website': "https://tcmariel.cu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Stamps',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/stamps_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}

