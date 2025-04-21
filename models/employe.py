from odoo import models, fields

class Employe(models.Model) :
    _name = 'myautoparc.employe'
    _description = "myautoparc employe object"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    full_name = fields.Char(string="Full Name")
    post = fields.Selection([
        ('fleet_manager', "Vehicle Fleet Manager"),
        ('auto_technician', "Automotive Technician"),
        ('paint_specialist', "Car Paint Specialist"),
        ('inventory_clerk', "Inventory Control Clerk"),
        ('logistics_coordinator', "Logistics Coordinator"),
        ('rental_agent', "Car Rental Agent"),
        ('repair_technician', "Auto Body Repair Technician"),
        ('transport_planner', "Transportation Planner"),
        ('customization_specialist', "Vehicle Customization Specialist"),
        ('sales_consultant', "Automobile Sales Consultant")], string="Occupied Post")
    department = fields.Selection([
        ('logistics', "Logistics"),
        ('maintenance', "Maintenance"),
        ('sales', "Sales"),
        ('customer_service', "Customer Service"),
        ('management', "Management")], string="Department")
    telephone = fields.Char(string="Télephone")
    email = fields.Char(string="Email")
    car_id = fields.Many2one('myautoparc.car', string="affected car")