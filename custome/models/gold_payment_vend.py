from odoo import models, fields, api
from logging import NullHandler


class goldPaymentVendor(models.Model):
    _name = "gold.payment.vendor"
    _description = 'gold payment for vendors'

    vendor = fields.Many2one(
        string='Vendor',
        comodel_name='res.partner',
        required=True,
    )

    product = fields.Many2one(
        string='Product',
        comodel_name='product.product',
        required=True,
    )
    
    warehouse = fields.Many2one(
        string='Warehouse',
        comodel_name='stock.warehouse',
        required=True,
    )
    
    debit_qty  = fields.Float(string='Debit Quantity',digits=(12,4))
    credit_qty  = fields.Float(string='Crebit Quantity',digits=(12,4))
