from odoo import models, fields

class Car(models.Model) :
    _name = 'myautoparc.car'
    _description = "myautoparc car object"

    name = fields.Char(string="CarName",required=True)
    serial_number = fields.Char(string="Serial number",required=True)
    colors = fields.Selection([
        ('black',"Black"),
        ('yellow',"yellow"),
        ('grey',"Grey"),
        ('red',"Red")],
        string="Car color",default='black')
    release_date = fields.Date(string="Release Date",required=True)
    meter = fields.Char(string="Meter")
    state = fields.Selection ([
        ('new',"New"),
        ('out',"Out of Service"),
        ('on',"On Service")],
        string="Car State")
    lastcare = fields.Date(string="Last care date")
    brand_id = fields.Many2one('myautoparc.brand',string="Car brand")
    image = fields.Binary(string="photo")
    document_ids = fields.Many2many('ir.attachment', 'attachment_100', 'attachment_id', string="Documents")
    model_id = fields.Many2one('myautoparc.model',string="Assaciated Model", required=True)
    graycard_id = fields.Many2one('myautoparc.graycard',string="Gray Card", required=True)
    assurance_id = fields.Many2one('myautoparc.assurance',string="Gray Card", required=True)