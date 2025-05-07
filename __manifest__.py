{
    'name': 'GymBeam HR Extension',
    'version': '1.0',
    'summary': 'Custom HR module for GymBeam',
    'description': 'Extends HR module with custom fields, recruitment form, email wizard, and API functionality.',
    'author': 'Peter Tutka',
    'category': 'Human Resources',
    'depends': ['hr', 'hr_recruitment'],
    'data': [
        'views/employee_view.xml',
        'views/recruitment_form_view.xml',
        'views/send_emails_wizard_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
