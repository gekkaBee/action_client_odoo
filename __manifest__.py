# -*- coding: utf-8 -*-
{
    'name': "action_client_example",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/assets_backend.xml',
        'views/views.xml',
        'views/menu_item.xml'
    ],
    'qweb': ['static/src/xml/action_client_example.xml']
}
