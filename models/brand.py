from odoo import models, fields

class Brand(models.Model) :
    _name = 'myautoparc.brand'
    _description = "myautoparc brand object"

    name = fields.Char(string="label",required=True)
    country_id = fields.Many2one('res.country',string="Country")
    foundation_date = fields.Date(string="Foundation Date",required=True)
    model_ids = fields.One2many('myautoparc.model','brand_id',string="List of cars")