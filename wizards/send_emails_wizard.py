from odoo import models, fields, api
import base64
import pandas as pd
from io import BytesIO

class SendEmailsWizard(models.TransientModel):
    _name = 'gymbeam.send_emails_wizard'
    _description = 'Send Emails Wizard'

    email_file = fields.Binary(string='Email File', required=True, attachment=True)
    email_file_name = fields.Char()

    def action_send_emails(self):
        if self.email_file:
            try:
                data = base64.b64decode(self.email_file)
                df = pd.read_excel(BytesIO(data), header=None)

                if df.shape[1] < 2:
                    raise Warning("Excel file must have at least two columns: Email and Subject.")

                for _, row in df.iterrows():
                    email_to = row[0]
                    subject = row[1] or "Welcome to GymBeam"

                    if not email_to:
                        continue

                    self.env['mail.mail'].create({
                        'subject': subject,
                        'body_html': 'Welcome to GymBeam',
                        'email_to': email_to,
                        'email_from': self.env.user.email,
                    }).send()
            except Exception as e:
                raise Warning(f"Failed to send emails: {str(e)}")
