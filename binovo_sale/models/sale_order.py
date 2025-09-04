# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            if order.order_line.filtered(lambda line: line.product_id and line.product_uom_qty == 0):
                raise ValidationError(_("You cannot confirm a sales order with lines having a product quantity equal to 0. Please remove those lines and try again."))
        return super().action_confirm()

    def action_delete_zero_qty_lines(self):
        for order in self:
            zero_qty_lines_ids = order.order_line.filtered(lambda line: line.product_id and line.product_uom_qty == 0)
            if zero_qty_lines_ids:
                zero_qty_lines_ids.unlink()
        return True