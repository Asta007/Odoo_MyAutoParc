
from odoo import models, fields

class Center(models.Model):
    _name = 'myautoparc.center'
    _description = 'myautoparc Center object'

    name = fields.Char(required=True)
    adresse = fields.Char()
    responsable = fields.Many2one('res.users', string='Responsable')
    telephone = fields.Char()