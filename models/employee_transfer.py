# -*- coding: utf-8 -*-
"""Employee Transfer Model"""
from odoo import fields, models, api


class EmployeeTransfer(models.Model):
    """Employee Transfer Model"""
    _name = 'employee.transfer'
    _description = 'Employee Company Transfer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', string='Employee',
            domain="['|', ('company_id', '=', False), ('company_id', 'in', allowed_company_ids)]")
    company_id = fields.Many2one('res.company', string='Previous Company')
    transfer_date = fields.Date(default=fields.Date.today())
    new_company_id = fields.Many2one('res.company', string='New Company')
    state = fields.Selection([
        ('draft', 'Draft'), ('requested', 'Requested'),
        ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='draft', string='Status')

    @api.onchange('employee_id')
    def _onchange_user_id(self):
        """Onchange the user_id field"""
        if self.employee_id:
            self.company_id = self.employee_id.company_id

    def action_submit(self):
        """Submit an employee transfer"""
        self.state = 'requested'

    def action_approve(self):
        """Approve an employee transfer"""
        employee = self.employee_id
        print(self)
        new_company = self.new_company_id
        employee.company_id = new_company
        if employee.user_id:
            user = employee.user_id
            if new_company.id not in user.company_ids.ids:
                user.write({'company_ids': [fields.Command.link(new_company.id)]})
            user.write({'company_id': new_company.id})
        self.state = 'approved'

    def action_reject(self):
        """Reject an employee transfer"""
        self.state = 'rejected'
