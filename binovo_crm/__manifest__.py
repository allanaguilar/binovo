# -*- coding: utf-8 -*-

{
    'name': "BINOVO - CRM",
    'summary': '',
    'description': '''
    ''',
    'author': 'Allan Aguiilar',
    'website': 'https://binovo.es/',
    'version': '2025.09.03',
    'license': 'Other proprietary',
    'maintainer': '',
    'contributors': [],
    'category': 'Sales/CRM',

    'sequence': 1050,
    'depends': [
        'crm',
    ],
    'data': [               
        
        # V I E W S
        'views/crm_lead_views.xml',
        'views/res_partner_views.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
