# -*- coding: utf-8 -*-
{
    'name': "Atani Modulos",

    'summary': """Modulos personalizados para Atani""",

    'description': """
        Modificación de vistas y modelos para el proyecto  
    """,

    'author': "soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_crm','account'],

    # always loaded
    'data': [
        'views/vista_partner.xml',
        'views/vista_products.xml',
        'views/vista_crm.xml',
        'views/vista_marcas.xml',
        #'views/vista_ssp2.xml',
        #'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo_curso.xml',
    ],
    'intallable': True,
    'auto_install': False,
}
