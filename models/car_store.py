from odoo import models, fields

class CarStore(models.Model):
    _name = "model_car_store"
    
    name = fields.Char(string='Name', required=True)
    year = fields.Date(string="Date of production")
    photo = fields.Binary(string='Photo')
    Price = fields.Integer(string='Price')
    Count = fields.Integer(string='Count')
    Color = fields.Selection([('r', 'Red'), ('b', 'Black'), ('w', 'White')], string='Gender')
