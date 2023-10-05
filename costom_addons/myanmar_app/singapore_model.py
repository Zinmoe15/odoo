from odoo import models, fields

class singapore(models.Model):
	_name = "singapore.model"
	_description = "singapore.model.sample"
	_inherit = ['mail.thread', 'mail.activity.mixin']

	job_type = fields.Selection([
		('odoo developer', 'ODOO Developer'),
		('content writer', 'Content Writer'),
		('softwart developer', 'Software Developer'),
	], string="Job_Type", default="odoo developer", required="True")
	name = fields.Char(string="Name")
	image = fields.Binary(string="Image", required="True")
	dob = fields.Datetime(string="DOB")
	pob = fields.Char(string="POB")
	race = fields.Char(string="Race")
	religion = fields.Char(string="Religion")
	nationality = fields.Char(string="Nationality")
	job_position = fields.Char(string="Job Position")
	phone = fields.Char(string="Phone")

	education_foundation_lines = fields.One2many('education.foundation.model', 'education_foundation_id')
	employee_admin_lines = fields.One2many('employee.admin.model', 'employee_admin_id')