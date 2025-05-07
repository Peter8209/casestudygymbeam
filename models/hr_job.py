from odoo import models, fields, api

class JobPosition(models.Model):
    _inherit = "hr.job"

    api_id = fields.Integer(string="API ID", help="API Identifier for Job Position")
