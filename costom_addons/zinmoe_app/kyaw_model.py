from odoo import models, fields

class kyaw(models.Model):
	_name = "kyaw.model"
	_description = "kyaw.models.sample"
	_inherit = ['mail.thread', 'mail.activity.mixin']

	cv_image = fields.Binary(string="CV_Image", attachment=True)
	job_type = fields.Selection([
		('odoo developer', 'ODOO Developer'),
		('content writer', 'Content Writer'),
		('it programming', 'IT Programming'),
	], string="Job_Type", default="", required=True)
	name = fields.Char(string="Name")
	nrc = fields.Char(string="NRC")
	dob = fields.Date(string="DoB")
	nationality = fields.Char(string="Nationality")

	race = fields.Char(string="Race")
	religion = fields.Char(string="Religion")
	sex = fields.Selection([
		('male', 'Male'),
		('female', 'Female'),
		('other', 'Other')
	], string="Sex", default="other", required=True)

	height = fields.Char(string="Height")
	weight = fields.Char(string="Weight")
	marital_status = fields.Char(string="Marital_Status")

	education= fields.Char(string="Education")
	language = fields.Char(string="Language")
	phone = fields.Char(string="Phone")
	address = fields.Text(string="Address")

	background_education_lines = fields.One2many('background.education.model', 'kyaw_view_id')

	employment_history_lines = fields.One2many('employment.history.model', 'kyaw_view_id')