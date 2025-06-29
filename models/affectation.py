from odoo import models, fields

class Affectation(models.Model) :
    _name = 'myautoparc.affectation'
    _description = "myautoparc affectation object"

    car_id = fields.Many2one('myautoparc.car',string="Car")
    employee_id = fields.Many2one('hr.employee')
    start_date = fields.Date()
    end_date = fields.Date()