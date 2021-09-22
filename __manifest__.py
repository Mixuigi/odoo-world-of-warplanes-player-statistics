{
    'name': 'Statistic players WOW',
    'version': '1.0',
    'summary': 'Game',
    'sequence': 10,
    'description': """
Favourite Game
    """,
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/game.xml',
        'views/form.xml',
        'views/kanban.xml',
        'views/graph.xml',
        'views/tree.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
