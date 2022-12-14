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
    'depends': ['base','report_xlsx','sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/cron.xml',
        'wizard/create_appointment_view.xml',
        'views/patient_view.xml',
        'views/sale_order.xml',
        'views/invoice.xml',
        'views/doctors_view.xml',
        'views/blood_bank_view.xml',
        'views/appointment.xml',
        'views/patient_menu.xml',
        'report/patient_card.xml',
        'report/report.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
