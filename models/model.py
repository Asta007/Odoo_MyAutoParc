from odoo import models, fields

class Brand(models.Model) :
    _name = 'myautoparc.model'
    _description = "myautoparc model Object"

    name = fields.Char(string="label",required=True)
    brand_id = fields.Many2one('myautoparc.brand', string="Associated brand")
    #body = fields.Selection([ ('berling','Berling'),('suv','SUV'), ('4x4','4x4')], string="Body")