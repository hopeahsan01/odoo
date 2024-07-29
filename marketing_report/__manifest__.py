# -*- coding: utf-8 -*-
{
    'name': "marketing_report",

    'summary': "Excel Report",

    'description': """
        Marketing Report Through Wizard.
    """,

    'author': "HAK Technologies",
    'website': "https://www.HAKTechnologies.com",
    'version': '0.1',
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'xlsx_reporting', 'scrubz_custom'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'wizard/stock_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
