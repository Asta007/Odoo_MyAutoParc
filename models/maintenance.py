from odoo import models, fields

class Maintenance(models.Model) :
    _name = 'myautoparc.maintenance'
    _description = "myautoparc maintenance object"

    car_id = fields.Many2one('myautoparc.car')
    date = fields.Date()
    type = fields.Char()
    cost = fields.Float()
    note = fields.Text()