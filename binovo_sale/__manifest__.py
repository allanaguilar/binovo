# -*- coding: utf-8 -*-

{
    'name': "BINOVO - Sale",
    'summary': '',
    'description': '''
    ''',
    'author': 'Allan Aguiilar',
    'website': 'https://binovo.es/',
    'version': '2025.09.03',
    'license': 'Other proprietary',
    'maintainer': '',
    'contributors': [],
    'category': 'Sales/Sales',

    'sequence': 1050,
    'depends': [
        'sale',
        'sale_management',
    ],
    'data': [               
        
        # 'security/security.xml',
        
        # V I E W S
        'views/sale_order_views.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
