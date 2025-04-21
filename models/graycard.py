from odoo import models, fields

class Graycard(models.Model) :
    _name = 'myautoparc.graycard'
    _description = "myautoparc graycard object"

    number = fields.Date(string="Gray Card Number")
    delivery_location = fields.Date(string="Delivery Location")
    delivery_date = fields.Date(string="Delivery Date")
    exp_date = fields.Date(string="Expire Date")