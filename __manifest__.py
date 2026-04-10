# -*- coding: utf-8 -*-
{
    'name': 'Employee Transfer',
    'version': '19.0.1.0.0',
    'installable': True,
    'auto_install': False,
    'application': True,
    'depends': ['hr', 'mail'],
    'data': [
        'security/employee_transfer_group.xml',
        'security/ir_rules_employee.xml',
        'security/ir.model.access.csv',
        'views/employee_transfer_view.xml',
        'views/employee_transfer_menus.xml'
    ],
    'sequence': 0,
}
