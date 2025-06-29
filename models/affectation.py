from odoo import models, fields

class Affectation(models.Model) :
    _name = 'myautoparc.affectation'
    _description = "myautoparc affectation object"

    car_id = fields.Many2one('myautoparc.car',string="Car")
    #employee_id = fields.Many2one('hr.employee')
    employee_name = fields.Char(string="Employee Name",required=True)
    start_date = fields.Date()
    end_date = fields.Date()