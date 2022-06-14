# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PaymentVendorGold(models.Model):
    _name = "paymentvendorgold.model"
    _description = "Payment Vendor Gold Model"
    _rec_name = "transaction_ID"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    transaction_ID = fields.Char(string="Transaction Number",
                                 default=lambda self: self.env['ir.sequence'].next_by_code(
                                     'increment_transaction_ID'))
    payment_date = fields.Date(string="Date", default=lambda self: fields.Date.today())
    vendor_name = fields.Many2one("res.partner", string="Vendor Name")
    ware_house = fields.Many2one("stock.warehouse", string="Ware House")
    product_template_id = fields.Many2one(
        'product.template', 'Items')
    karat = fields.Many2one("karat.model", related="product_template_id.karat")
    debit = fields.Integer(string="Debit", help="200 G")
    credit = fields.Integer(string="Credit")
    credit_21 = fields.Float(string="Equivalent to 21 Karat", compute="_conversion_to_karat21")

    _sql_constraints = [
        ('unique_transaction_ID', 'unique (transaction_ID)', 'Transaction Number already exists!')
    ]


    @api.depends('debit', 'karat')
    def _conversion_to_karat21(self):
        """ Formula for Ta7eef Gold """
        for record in self:
            record.credit_21 = ((int(record.karat.karat) * record.debit) / 21)

    @api.onchange('debit')
    def _debit_credit(self):
        """ Function to make credit bel Negative """
        self.credit = self.debit * -1
