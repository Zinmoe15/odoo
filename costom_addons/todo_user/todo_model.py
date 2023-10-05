from odoo import models, fields
from odoo.exceptions import UserError
class TodoTask(models.Model):
	# _inherit = 'todo.task'
	_name = 'todo.task'
	_inherit = ['todo.task', 'mail.thread']

	user_id = fields.Many2one('res.users', 'Responsible')
	date_deadline = fields.Date('Deadline')
	name = fields.Char(help="What needs to be done?")

	def do_clear_done(self):
		print('todo do_clear_done start')
		domain = [('is_done', '=', True),
		'|', ('user_id', '=', self.env.uid),
		('user_id', '=', False)]
		done_recs = self.search(domain)
		done_recs.write({'active': False})
		print('todo_user do_clear_done end')
		return True

	def do_toggle_done(self):
		print('todo_user do_toggle_done start')
		if self.user_id != self.env.user:
			raise UserError('Only the responsible can do this!')
		else:
			print('todo_user do_toggle_done end')
			return super(TodoTask, self).do_toggle_done()