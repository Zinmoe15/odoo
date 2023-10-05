from odoo import models, fields

class employee_admin(models.Model):
	_name = "employee.admin.model"
	_description = "employee.admin.model.sample"

	job_type = fields.Selection([
		('odoo developer', 'ODOO Developer'),
		('dancer modern', 'Dancer Modern'),
		('actor', 'Actor'),
	], string="Job_Type", default="odoo developer", required=True)

	name = fields.Char(string="Name")
	cv_image = fields.Binary(string="CV_Image")
	position = fields.Char(string="Position")
	salary = fields.Char(string="Salary")
	bonus = fields.Char(string="Bonus")

	employee_admin_id = fields.Many2one('singapore.model')