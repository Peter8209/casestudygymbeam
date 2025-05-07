# casestudygymbeam
Case Study - Python Developer for GymBeam
GymBeam HR API Extension

Overview

This is a custom Odoo module designed for GymBeam, providing extended functionality for HR management. It allows the creation of job applicants through a REST API, using JSON data.

Features

Adds a custom API for creating job applicants via JSON requests.

The API endpoint is /case_study/applicant/get.

Applicants are created based on the provided JSON data.

The API connects applicants to job positions using a custom api_id field on the job position model.

Installation

Ensure you have an Odoo instance set up (Odoo 16).

Copy the gymbeam_hr module folder into your Odoo addons directory.

Restart the Odoo server.

Go to the Apps menu in Odoo backend.

Click on 'Update Apps List'.

Search for "GymBeam HR Extension" and install it.

Configuration

Ensure that the hr module is installed in Odoo.

Set up Job Positions in the HR module.

Make sure each Job Position has a unique API ID set.

Usage

API Endpoint

Endpoint URL: http://localhost:8069/case_study/applicant/get

Method: POST

Content-Type: JSON

JSON Request Example
{
    "candidates": [
        {
            "id": 12345,
            "title": "Ing",
            "firstname": "John",
            "surname": "Doe",
            "phone": "123456789",
            "email": "applicant@odoo.com",
            "gender": "male",
            "job": {
                "id": "4249974",
                "title": "Job title"
            }
        }
    ]
}
How it works

The API receives a JSON payload with candidate data.

For each candidate, it checks the provided api_id of the job position.

If a matching job position is found, an applicant is created in Odoo.

Error Handling

If the API ID is not found for a job position, the API returns an error message.

If the JSON payload is invalid, the API returns an error message.

Security

The API is publicly accessible. For production environments, it is recommended to secure it using authentication.

License

This module is developed for GymBeam and is not for public distribution.
