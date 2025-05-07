from odoo import http
from odoo.http import request, Response
import json

class ApplicantAPIController(http.Controller):

    @http.route('/case_study/applicant/get', type='json', auth='public', methods=['POST'], csrf=False)
    def create_applicant(self, **kwargs):
        try:
            data = request.jsonrequest
            candidates = data.get('candidates', [])
            created_applicants = []

            for candidate in candidates:
                job_position = request.env['hr.job'].sudo().search([('api_id', '=', candidate['job']['id'])], limit=1)
                if not job_position:
                    return Response("Job position with specified API ID not found.", status=404)

                applicant = request.env['hr.applicant'].sudo().create({
                    'name': f"{candidate['firstname']} {candidate['surname']}",
                    'partner_name': f"{candidate['firstname']} {candidate['surname']}",
                    'email_from': candidate['email'],
                    'partner_phone': candidate['phone'],
                    'job_id': job_position.id,
                    'gender': candidate['gender'],
                })
                created_applicants.append(applicant.id)

            return {
                "status": "success",
                "message": f"{len(created_applicants)} applicants created successfully.",
                "applicant_ids": created_applicants
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
