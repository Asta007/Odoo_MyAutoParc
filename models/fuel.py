from odoo import models, fields

class Fuel(models.Model) :
    _name = 'myautoparc.fuel'
    _description = "myautoparc fuel object"

    car_id = fields.Many2one('myautoparc.car')
    date = fields.Date()
    quantite = fields.Float()
    cost = fields.Float()