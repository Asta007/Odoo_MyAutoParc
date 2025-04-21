from odoo import models, fields

class Assurance(models.Model) :
    _name = 'myautoparc.assurance'
    _description = "myautoparc assurance object"

    company = fields.Char(string="Company")
    type = fields.Selection([
        ('car_insurance', 'Car Insurance'),
        ('third_party', 'Third-Party Liability'),
        ('comprehensive', 'Comprehensive Insurance'),
        ('collision', 'Collision Insurance'),
        ('theft', 'Theft Insurance')], string='Type', default='sante')
    start_date = fields.Date(string="Start Date",required=True)
    end_date = fields.Date(string="End Date",required=True)
    amount = fields.Integer(string="Annual Amount")
    car_ids = fields.One2many('myautoparc.car','assurance_id',string="Car List", required=True)