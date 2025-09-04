# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import re

class Partner(models.Model):
    _inherit = 'res.partner'

    source_type = fields.Selection([
        ('third_party', 'Terceros'),
        ('social_networks', 'Redes sociales'),
        ('internet_search', 'Búsqueda en Internet')
    ], string='Tipo de Fuente',
    required=True,
    help="Indicar a través de que fuente ha dado con la empresa")
    
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and not self._is_valid_email(record.email):
                raise ValidationError(_("El correo electrónico no es válido."))

    def _is_valid_email(self, email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email)