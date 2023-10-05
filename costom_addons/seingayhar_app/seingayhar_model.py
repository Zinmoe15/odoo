from odoo import models, fields

class seingayhar(models.Model):
	_name = 'seingayhar.task'
	_description = 'seingayhar.task.simple'

	name = fields.Char(string="Name")