from odoo import models, fields, api
import base64
import pandas as pd
from io import BytesIO

class Employee(models.Model):
    _inherit = "hr.employee"

    i_love_gb = fields.Boolean(string="I Love GymBeam")
    special_phone = fields.Char(string="Special Phone")
    salary = fields.Integer(string="Salary")
    tax = fields.Integer(string="Tax")
    total_salary = fields.Integer(string="Total Salary", compute="_compute_total_salary", store=True)
    employee_contacts = fields.Binary(string="Employee Contacts", attachment=True)
    employee_contacts_filename = fields.Char()

    @api.depends('salary', 'tax')
    def _compute_total_salary(self):
        for rec in self:
            rec.total_salary = (rec.salary or 0) + (rec.tax or 0)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('special_phone'):
                vals['special_phone'] = "0901123456"
        return super().create(vals_list)

    def write(self, vals):
        if 'special_phone' in vals and not vals['special_phone']:
            vals['special_phone'] = "0901123456"
        return super().write(vals)

    def action_send_emails(self):
        for employee in self:
            if employee.employee_contacts:
                try:
                    data = base64.b64decode(employee.employee_contacts)
                    df = pd.read_excel(BytesIO(data), header=None)

                    if df.shape[1] < 2:
                        raise Warning("Excel file must have at least two columns: Email and Subject.")

                    for _, row in df.iterrows():
                        email_to = row[0]
                        subject = row[1] or "Welcome in GymBeam"

                        if not email_to:
                            continue

                        mail = self.env['mail.mail'].create({
                            'subject': subject,
                            'body_html': "Welcome in GymBeam",
                            'email_to': email_to,
                            'email_from': self.env.user.email,
                        })
                        mail.send()
                except Exception as e:
                    raise Warning(f"Failed to parse and send emails: {str(e)}")