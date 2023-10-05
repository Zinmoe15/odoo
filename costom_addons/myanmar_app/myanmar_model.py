from odoo import models, fields

class myanmar(models.Model):
	_name = "myanmar.model"
	_description = "myanmar.model.sample"
	_inherit = ['mail.thread', 'mail.activity.mixin']

	active = fields.Boolean(string="Active", default=True)

	job_type = fields.Selection([
		('odoo developer', 'ODOO Developer'),
		('content writer', 'Content Writer'),
		('softwart developer', 'Software Developer'),
	], string="Job_Type", default="odoo developer", required=True)
	name = fields.Char(string="Name")
	image = fields.Binary(string="Image", required="True")
	dob = fields.Datetime(string="DOB")
	pob = fields.Char(string="POB")
	race = fields.Char(string="Race")
	religion = fields.Char(string="Religion")
	nationality = fields.Char(string="Nationality")
	job_position = fields.Char(string="Job Position")
	phone = fields.Char(string="Phone")

	def print_myanmar_report(self):
		return self.env.ref('myanmar_app.myanmar_report').report_action(self)

	state = fields.Selection([
		('draft', 'Draft'),
		('confirm', 'Confirm'),
		('done', 'Done'),
	], string="state", default="draft", readonly="True")

	def action_draft(self):
		for rec in self:
			rec.state="draft"

	def action_confirm(self):
		for rec in self:
			rec.state="confirm"

	def action_done(self):
		for rec in self:
			rec.state="done"