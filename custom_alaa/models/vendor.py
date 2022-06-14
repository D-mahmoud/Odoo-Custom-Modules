# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vendor(models.Model):
    _inherit = 'res.partner'
    vendor_id = fields.Integer(string="Vendor Id", unique=True , required=True)
    vendor_group = fields.Many2one("vendorcategory.model", string="Vendor Group")
    sale_mode = fields.Selection([('fixed', 'Fixed'), ('daily', 'Daily')], default='daily')
    labor_balance = fields.Float(string="Labor Balance", compute="_compute_labor_balance")
    gold_balance = fields.Float(string="Gold Balance", compute='_compute_gold_labor')
    gold_credit_limit = fields.Float(string="Gold Credit Limit", required=True)
    credit_limit = fields.Float(string="Credit Limit", required=True)

    _sql_constraints = [
        ('unique_vendor_id', 'unique(vendor_id)', 'Vendor Id already exists!')
    ]

    @api.depends('name')
    def _compute_labor_balance(self):
        """ Function to calculate Total Labor Price For Vendor """
        total_labor = 0
        vendor_details = self.env['purchase.order'].search([('partner_id', '=', self.name)])
        if len(vendor_details) > 1:
            for i in vendor_details:
                total_labor += float(i.total_labor_vendor)
            self.labor_balance = total_labor
        else:
            self.labor_balance = 0

    @api.depends('name')
    def _compute_gold_labor(self):
        """ Function to calculate Total Gold Weight For Vendor """
        total_gold_weights = 0
        vendor_details = self.env['purchase.order'].search([('partner_id', '=', self.name)])
        if len(vendor_details) > 1:
            for i in vendor_details:
                total_gold_weights += i.total_21_karats
            self.gold_balance = total_gold_weights
        else:
            self.gold_balance = 0
