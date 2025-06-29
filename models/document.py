from odoo import models, fields

class Document(models.Model) :
    _name = 'myautoparc.document'
    _description = "myautoparc document object"

    car_id = fields.Many2one('myautoparc.car')
    type_document = fields.Selection([('carte_grise', 'Carte Grise'), ('assurance', 'Assurance'), ('ct', 'Contrôle Technique'), ('vignette', 'Vignette')])
    date_expiration = fields.Date()
    files = fields.Binary()