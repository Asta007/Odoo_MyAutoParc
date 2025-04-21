from odoo import models, fields

class Contract(models.Model) :
    _name = 'myautoparc.contract'
    _description = "myautoparc contract object"

    number = fields.Date(string="Contract Number",required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    tarif = fields.Integer(string="Tarif",required=True)
    car_ids = fields.Many2many('myautoparc.car', string="Car Lists")
    client_id = fields.Many2one('myautoparc.client', string="Client")
