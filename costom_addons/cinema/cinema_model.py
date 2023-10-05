from odoo import models, fields

class cinema(models.Model):
	_name = 'cinema.task'
	_description = 'cinema.task.simple'

	# active = fields.Boolean(string="Active", default=True)

	cv_image = fields.Binary(string="CV Image", attachment=True)
	job_type = fields.Selection([
		('odoo_developer', 'ODOO Developer'),
		('software_developer', 'Software Developer'),
		('content_writer', 'Content Writer'),
		('data_analysis', 'Data Analysis'),
		('web_developer', 'Web Developer')
	], string="Job Type", default='odoo_developer', required=True)

	name = fields.Char(string="Name")
	movie_name = fields.Char(string="Movie_Name")
	price = fields.Selection([
		('3000mmk', '3000mmk'),
		('3500mmk', '3500mmk'),
		('4000mmk', '4000mmk'),
		('4500mmk', '4500mmk'),
		('5000mmk', '5000mmk')
	],	string="Price", default='3000mmk', required=True)

	seat_number = fields.Char(string="Seat_Number")
	quantity = fields.Selection([
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8')
	], string="Quantity", default='1', required=True)
	
	time_show = fields.Char(datetime="Time_Show")
	cinema_phone = fields.Char(integer="Cinema_Phone")
	website = fields.Char(string="Website")