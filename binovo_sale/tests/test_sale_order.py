from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

# -*- coding: utf-8 -*-

class TestSaleOrder(TransactionCase):

    def setUp(self):
        super().setUp()
        self.product = self.env['product.product'].create({
            'name': 'Test Product',
            'type': 'consu',
        })
        self.sale_order = self.env['sale.order'].create({
            'partner_id': self.env.ref('base.res_partner_1').id,
        })

    def test_action_confirm_with_zero_qty_line_raises(self):
        self.env['sale.order.line'].create({
            'order_id': self.sale_order.id,
            'product_id': self.product.id,
            'product_uom_qty': 0,
            'name': 'Zero Qty Line',
        })
        with self.assertRaises(ValidationError):
            self.sale_order.action_confirm()

    def test_action_confirm_without_zero_qty_line_succeeds(self):
        self.env['sale.order.line'].create({
            'order_id': self.sale_order.id,
            'product_id': self.product.id,
            'product_uom_qty': 2,
            'name': 'Valid Line',
        })
        # Should not raise
        self.sale_order.action_confirm()

    def test_action_delete_zero_qty_lines_removes_lines(self):
        line1 = self.env['sale.order.line'].create({
            'order_id': self.sale_order.id,
            'product_id': self.product.id,
            'product_uom_qty': 0,
            'name': 'Zero Qty Line',
        })
        line2 = self.env['sale.order.line'].create({
            'order_id': self.sale_order.id,
            'product_id': self.product.id,
            'product_uom_qty': 1,
            'name': 'Non-zero Qty Line',
        })
        self.sale_order.action_delete_zero_qty_lines()
        self.assertFalse(line1.exists())
        self.assertTrue(line2.exists())

    def test_action_delete_zero_qty_lines_no_zero_lines(self):
        line = self.env['sale.order.line'].create({
            'order_id': self.sale_order.id,
            'product_id': self.product.id,
            'product_uom_qty': 3,
            'name': 'Valid Line',
        })
        result = self.sale_order.action_delete_zero_qty_lines()
        self.assertTrue(result)
        self.assertTrue(line.exists())