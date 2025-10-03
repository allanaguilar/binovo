# -*- coding: utf-8 -*-

{
    'name': "BINOVO - Website Blog",
    'summary': '',
    'description': '''
    ''',
    'author': 'Allan Aguiilar',
    'website': 'https://binovo.es/',
    'version': '2025.09.05',
    'license': 'Other proprietary',
    'maintainer': '',
    'contributors': [],
    'category': 'Website/Website',

    'sequence': 1050,
    'depends': [
        'website_blog',
    ],
    'data': [               
        
        'security/security.xml',
        
        # V I E W S
        'views/website_blog_views.xml',
        'views/blog_post_add.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
