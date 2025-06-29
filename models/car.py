from odoo import models, fields

class Car(models.Model) :
    _name = 'myautoparc.car'
    _description = "myautoparc car object"

    immatriculation = fields.Char(required=True)
    numero_chassis = fields.Char()
    date_acquisition = fields.Date()
    type_vehicule = fields.Selection([('voiture', 'Voiture'), ('utilitaire', 'Utilitaire'), ('moto', 'Moto'), ('camion', 'Camion')])
    statut = fields.Selection([('service', 'En service'), ('maintenance', 'En maintenance'), ('vendu', 'Vendu')])
    brand_id = fields.Many2one('myautoparc.brand',string="Car brand")
    model_id = fields.Many2one('myautoparc.model',string="Assaciated Model", required=True)
    center_id = fields.Many2one('myautoparc.center',string="Assaciated Center", required=True)
