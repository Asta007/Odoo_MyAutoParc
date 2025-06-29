from odoo import models, fields

class Brand(models.Model) :
    _name = 'myautoparc.brand'
    _description = "myautoparc brand object"

    name = fields.Char(string="label",required=True)
    #model_ids = fields.One2many('myautoparc.model','brand_id',string="List of cars")