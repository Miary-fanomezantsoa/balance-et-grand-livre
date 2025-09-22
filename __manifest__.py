# -*- coding: utf-8 -*-
{
    'name': "grandlivre_et_balance",

    'summary': "Module balance et grand livre",

    'description': """
CECI EST LE MODULE COMPTABLE DE ODOO 18
    """,

    'author': "Miary ",
    'website': "miaryfanomezantsoa14@gmail.com",
    'application':True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/grandlivre.xml', 
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

