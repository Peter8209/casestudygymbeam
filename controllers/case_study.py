from odoo import http
from odoo.http import request, Response
import json

class CaseStudyController(http.Controller):

    @http.route('/case_study/applicant/get', type='json', auth='public', methods=['POST'], csrf=False)
    def create_applicant(self, **kwargs):
        try:
            data = request.jsonrequest.get('candidates')
            if not data:
                return {"error": "No candidates data found"}

            for candidate in data:
                job_api_id = candidate.get('job', {}).get('id')
                job_position = request.env['hr.job'].sudo().search([('api_id', '=', str(job_api_id))], limit=1)

                if not job_position:
                    return {"error": f"No job position found for API ID {job_api_id}"}

                # Vytvorenie uchádzača
                request.env['hr.applicant'].sudo().create({
                    'name': f"{candidate.get('firstname')} {candidate.get('surname')}",
                    'partner_name': f"{candidate.get('firstname')} {candidate.get('surname')}",
                    'email_from': candidate.get('email'),
                    'partner_phone': candidate.get('phone'),
                    'gender': candidate.get('gender'),
                    'job_id': job_position.id
                })

            return {"status": "success", "message": "Applicants created successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
