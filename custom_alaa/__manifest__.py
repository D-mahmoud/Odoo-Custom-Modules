# -*- coding: utf-8 -*-
{
    'name': "custom-alaa",
    'sequence': '10',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'license': 'LGPL-3',

    'author': "Alaa Farouk",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management','purchase', 'stock', 'sale_stock' , 'delivery', 'attachment_indexation'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/karat_view.xml',
        'views/product_view.xml',
        'views/vendor_view.xml',
        'views/templates.xml',
        'views/payment_vendor_gold_view.xml',
        'views/purchase_inherit_view.xml',
        'views/sales_inherit_view.xml',
        'views/lot_inherit_view.xml',
        'views/vendor_category_view.xml',
        'views/alaa_practice_view.xml',
        'views/accounting_inherit_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install':True ,




}
