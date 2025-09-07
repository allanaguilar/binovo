# -*- coding: utf-8 -*-

{
    'name': "BINOVO - CRM",
    'summary': '',
    'description': '''
    ''',
    'author': 'Allan Aguiilar',
    'website': 'https://binovo.es/',
    'version': '2025.09.09',
    'license': 'Other proprietary',
    'maintainer': '',
    'contributors': [],
    'category': 'Sales/CRM',

    'sequence': 1050,
    'depends': [
        'crm',
        'website',
    ],
    'data': [               
        # D A T A
        'data/ir_model_fields.xml',
        
        # V I E W S
        'views/crm_lead_views.xml',
        'views/res_partner_views.xml',
        'views/website_templates_contactus.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
