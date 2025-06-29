from odoo import models, fields

class Employee(models.Model) :
    _name = "myautoparc.employee"
    _description = "myautoparc employee Object"

    last_name = fields.Char(string="Last Name", required=True)
    first_name = fields.Char(string="First Name", required=True)
    phone_number = fields.Char(string="Phone Number")
    adress = fields.Char(string="Adress")
    email = fields.Char(string="Email")
