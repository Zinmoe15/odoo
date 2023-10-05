from odoo import models, fields

class employment_history(models.Model):
	_name = "employment.history.model"
	_description = "employment.history.model.sample"
	_inherit = ['mail.thread', 'mail.activity.mixin']

	cv_image = fields.Binary(string="CV_Image", attachment="True")
	job_type = fields.Selection([
		('odoo developer', 'ODOO Developer'),
		('software developer', 'Software Developer'),
		('content writer', 'Content Writer'),
	], string="Job_Type", default="software developer", required="True")

	name = fields.Char(string="Name")
	education = fields.Char(string="Education")
	other_experience = fields.Char(string="Other_Experience")
	my_project = fields.Char(string="My_Project")
	interest = fields.Char(string="Interest")

	kyaw_view_id = fields.Many2one('kyaw.model')