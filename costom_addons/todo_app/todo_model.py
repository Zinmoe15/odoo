from odoo import models, fields

class TodoTask(models.Model):
	_name = 'todo.task'

	name = fields.Char('Description', required=True)
	is_done = fields.Boolean('Done?')
	active = fields.Boolean('Active?', default=True)

	def do_toggle_done(self):
		print('todo_app do_toggle_done start')
		self.is_done = not self.is_done
		print('todo_app do_toggle_done end')
		return True


	def do_clear_done(self):
		done_recs = self.search([('is_done', '=', True)])
		done_recs.write({'active': False})
		return True