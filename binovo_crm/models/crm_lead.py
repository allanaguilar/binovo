# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class Lead(models.Model):
    _inherit = 'crm.lead'

    source_type = fields.Selection([
        ('third_party', 'Terceros'),
        ('social_networks', 'Redes sociales'),
        ('internet_search', 'Búsqueda en Internet')
    ], string='Tipo de Fuente', help="Indicar a través de que fuente ha dado con la empresa")