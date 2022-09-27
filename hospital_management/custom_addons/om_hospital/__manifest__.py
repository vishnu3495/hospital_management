# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",
    'summary': """Hospital Management Software""",
    'sequence': 0,
    'description': """Hospital Management Software""",
    'author': "ULTS",
    'website': "https://ults.in",
    'category': 'Productivity',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/doctors_view.xml',
        'views/blood_bank_view.xml',
        'views/appointment.xml',
        'views/patient_menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
