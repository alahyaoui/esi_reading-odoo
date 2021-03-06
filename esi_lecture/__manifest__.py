# -*- coding: utf-8 -*-
{
    'name': "esi_lecture",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/reading_menu.xml',
        'views/reading_view.xml',
        'views/authors_view.xml',
        'views/product_view.xml',
        'demo/author_demo.xml',
        'demo/book_demo.xml',
        'demo/product_demo.xml',
        'demo/supplier_demo.xml',
        'demo/lot_product_demo.xml',
        'demo/stock_demo.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/author_demo.xml',
        'demo/book_demo.xml',
        'demo/product_demo.xml',
        'demo/supplier_demo.xml',
        'demo/lot_product_demo.xml',
        'demo/stock_demo.xml',
    ],
    'application': True,
}
