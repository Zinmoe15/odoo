from odoo import models, fields

class zinmoekyaw(models.Model):
	_name = "zinmoekyaw.model"
	_description = "zinmoekyaw.model.sample"
	_inherit = ['mail.thread', 'mail.activity.mixin']

	active = fields.Boolean(string="Active", default="True")

	cv_image = fields.Binary(string="CV_Image", required="True")

	job_type = fields.Selection([
		('odoo developer', 'ODOO Developer'),
		('software developer', 'Software Developer'),
		('content writer', 'Content Writer'),
	], string="Job_Type", default="content writer", required="True")

	name = fields.Char(string="Name")
	dob = fields.Date(string="DOB")
	pob = fields.Char(string="POB")
	sex = fields.Selection([
		('male', 'Male'),
		('female', 'Female'),
		('other', 'Other'),
	], string="Sex", default="other", required="True")
	religion = fields.Char(string="Religion")
	race = fields.Char(string="Race")
	nationality = fields.Char(string="Nationality")
	martial_status = fields.Selection([
		('single', 'Single'),
		('married', 'Married'),
		('relationship', 'Relationship'),
	], string="Martial_Status", default="single", required="True")
	education = fields.Char(string="Education")
	working_experience = fields.Char(string="Working_Experience")
	phone = fields.Char(string="Phone")

	education_background_lines = fields.One2many('education.background.model', 'education_background_id')
	employment_management_lines = fields.One2many('employment.management.model', 'employment_management_id')

	def print_zinmoekyaw_report(self):
		return self.env.ref('zinmoekyaw_app.zinmoekyaw_report').report_action(self)

	state = fields.Selection([
		('draft', 'Draft'),
		('confirm', 'Confirm'),
		('done', 'Done'),
	], string="State", default="draft", readonly=True)

	def action_draft(self):
		for rec in self:
			rec.state="draft"

	def action_confirm(self):
		for rec in self:
			rec.state="confirm"

	def action_done(self):
		for rec in self:
			rec.state="done"

	# def _compute_ebl_count(self):
	# 	count = self.env['education.background.model'].search_count([{'zinmoekyaw_app_id', 'm', 'self.id'}])
	# 	for rec in self:
	# 		rec.ebl_count = count

	ebl_count = fields.Integer(string="EBL_Count")