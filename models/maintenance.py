from odoo import models, fields

class Maintenance(models.Model) :
    _name = 'myautoparc.maintenance'
    _description = "myautoparc maintenance object"

    car_id = fields.Many2one('myautoparc.car', string="Car", required=True)
    date = fields.Date(string="Date")
    maintenance_type = fields.Selection([
        ('routine', 'Routine Maintenance'),
        ('oil_change', 'Oil Change'),
        ('brake_check', 'Brake Check'),
        ('tire_maintenance', 'Tire Maintenance'),
        ('ac_cooling_check', 'Cooling System Check')], string="Maintenance Type", required=True)
    tarif = fields.Integer(string="Tarif",required=True)
    description = fields.Date(string="Description",required=True)
    next_date = fields.Date(string="Next maintenance")