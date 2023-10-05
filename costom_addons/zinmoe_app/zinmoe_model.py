from odoo import models, fields

class zinmoe(models.Model):

	_name= 'zinmoe.model'
	_description= 'zinmoe.models.sample.format'
	_inherit= ['mail.thread', 'mail.activity.mixin']

	cv_image = fields.Binary(string="CV_Image", attachment=True)
	job_type = fields.Selection([
		('odoo_developer', 'odoo Developer'),
		('software_developer', 'Software Developer'),
		('content_writer', 'Content Writer'),
		('data_analyst', 'Data Analyst')
	], string="Job_Type", default="odoo_developer", required=True)

	name = fields.Char(string="name")
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