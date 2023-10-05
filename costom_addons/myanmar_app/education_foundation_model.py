from odoo import models, fields

class education_foundation(models.Model):
	_name = "education.foundation.model"
	_description = "education.foundation.model.sample"

	job_type = fields.Selection([
		('odoo developer', 'ODOO Developer'),
		('dancer modern', 'Dancer Modern'),
		('actor', 'Actor'),
	], string="Job_Type", default="odoo developer", required=True)

	name = fields.Char(string="Name")
	cv_image = fields.Binary(string="CV_Image")
	education = fields.Char(string="Education")
	level = fields.Char(string="Level")
	skill = fields.Char(string="Skill")

	education_foundation_id= fields.Many2one('singapore.model')