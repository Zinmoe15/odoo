from odoo import models, fields

class zinmoeaung(models.Model):
	_name=	"jdonut.model"
	_description=	"jdonut.model.format"

	name = fields.Char(string="Name")
	shop_name = fields.Char(string="Shop_Name")
	price =	fields.Char(string="Price")
	quantity = fields.Char(string="Quantity")
	total_price = fields.Char(string="Total_Price")