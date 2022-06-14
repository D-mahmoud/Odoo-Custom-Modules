# -*- coding: utf-8 -*-
import json

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging


class purchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    karat = fields.Many2one('karat.model', string="Karat", related='product_id.product_tmpl_id.karat')
    category_id = fields.Many2one('product.category', string='Category', related='product_id.product_tmpl_id.categ_id')
    category_name = fields.Char(related='category_id.name', string="Category Name")
    weight_product = fields.Float(string="Weight")
    serial_number = fields.Char(string="Serial_Number")
    lot_number = fields.Many2one('stock.production.lot', string="Serial Number")
    price = fields.Float(string="Price", related='karat.price')
    labor_price = fields.Float(string="Labor Price", related="product_id.product_tmpl_id.standard_price")
    labor_price_total = fields.Float(string="Labor Price Total", compute="_compute_labor_price_total")
    gold_price_total = fields.Float(string="Gold Price Total", compute="_compute_gold_price_total")
    _sql_constraints = [
        ('unique_Serial_Number', 'unique (Serial_Number)', 'This Serial_Number already exists!'),
    ]

    @api.onchange('lot_number')
    def onchange_lot_number(self):
        """ Function to get product by its serial number"""
        if self.lot_number:
            serials = self.env['stock.production.lot'].search([('id', '=', self.lot_number.id)])
            if serials:
                if serials.product_id.seller_ids.name == self.partner_id:
                    prod = serials.product_id
                    _logger = logging.getLogger(__name__)
                    self.weight_product = serials['weight']
                else:
                    raise ValidationError(_('Warning ! you can not return purchase '))
            else:
                raise ValidationError("Serial Number doesnt exist")
            for rec in self:
                rec.product_id = prod
                rec.weight_product = self.weight_product * -1

    @api.onchange('price_unit', 'labor_price_total', 'gold_price_total')
    def compute_subtotal(self):
        """ function to calculate total for labor price and gold price """
        for rec in self:
            rec.price_unit = rec.labor_price_total + rec.gold_price_total

    @api.depends('labor_price', 'weight_product')
    def _compute_labor_price_total(self):
        """ Function to calculate Total labor price """
        for i in self:
            i.labor_price_total = i.weight_product * i.labor_price

    @api.depends('weight_product', 'price')
    def _compute_gold_price_total(self):
        """ Function to calculate Total Gold Price """
        for i in self:
            i.gold_price_total = i.weight_product * i.price

    @api.onchange('labor_price_total', 'gold_price_total', 'sale_mode', 'lot_number')
    def _compute_price_unit(self):
        """ For unit price """
        for i in self:
            i.price_unit = (i.labor_price_total + i.gold_price_total)

    @api.onchange("serial_number")
    def _create_lot(self):
        """ function to create a serial number """
        check_lot = self.env['stock.production.lot'].search(
            [('name', '=', self.serial_number), ('product_id', '=', self.product_id.id)])
        if check_lot:
            raise ValidationError("Serial Number Must Be Unique")
        elif self.serial_number:
            self.env['stock.production.lot'].create({
                'name': self.serial_number,
                'weight': self.weight_product,
                'product_id': self.product_id.id,
                'company_id': self.env.company.id})

            self.env['stock.move.line'].create({
                'lot_name': self.serial_number,
                'company_id': self.env.company.id,
                'product_uom_id': self.product_id.product_qty,
            })


class purchaseOrder(models.Model):
    _inherit = 'purchase.order'
    karat_9 = fields.Char(string='Karat 9K')
    karat_12 = fields.Char(string='Karat 12K')
    karat_14 = fields.Char(string='Karat 14K')
    karat_18 = fields.Char(string='Karat 18k')
    karat_21 = fields.Char(string='Karat 21k')
    karat_22 = fields.Char(string='Karat 22K')
    karat_24 = fields.Char(string='Karat 24K')
    sale_mode = fields.Selection([('fixed', 'Fixed'), ('daily', 'Daily')])
    total_21_karats = fields.Float(string="Total 21 Karats (G)")
    purchase_total = fields.Float(string="Total")
    total_price_gold = fields.Float(string="Total Gold (G) ")
    total_labor_vendor = fields.Char(string="Total Labor Price")
    return_purchase = fields.Boolean(string="Return")
    _logger = logging.getLogger(__name__)

    @api.onchange('partner_id')
    def onchange_partner(self):
        """ Function to get Sale Mode From Vendor """
        partner_id = self.env['res.partner'].search([('id', '=', self.partner_id.id)])
        self.sale_mode = partner_id.sale_mode

    @api.onchange('order_line', 'sale_mode')
    def _compute_line_weight(self):
        """ function to calculate total karat and labor price total """
        if self.sale_mode == "fixed":
            for purchase in self:
                for i in purchase.order_line:
                    i.gold_price_total = i.weight_product
                    i.labor_price_total = i.weight_product * i.labor_price
                    i.price_unit = i.labor_price_total
        elif self.sale_mode == "daily":
            for purchase in self:
                for i in purchase.order_line:
                    i.gold_price_total = i.weight_product * i.price
                    i.labor_price_total = i.weight_product * i.labor_price
                    i.price_unit = i.gold_price_total + i.labor_price_total
        weight9 = 0
        weight12 = 0
        weight18 = 0
        weight14 = 0
        weight21 = 0
        weight22 = 0
        weight24 = 0
        total_labor = 0
        total_gold = 0
        for purchase in self:
            for i in purchase.order_line:
                if i.karat.karat == 18:
                    weight18 += i.weight_product
                elif i.karat.karat == 21:
                    weight21 += i.weight_product
                elif i.karat.karat == 9:
                    weight9 += i.weight_product
                elif i.karat.karat == 14:
                    weight14 += i.weight_product
                elif i.karat.karat == 12:
                    weight12 += i.weight_product
                elif i.karat.karat == 22:
                    weight22 += i.weight_product
                else:
                    weight24 += i.weight_product

            purchase.karat_9 = str(weight9) + " G"
            purchase.karat_18 = str(weight18) + " G"
            purchase.karat_12 = str(weight12) + " G"
            purchase.karat_14 = str(weight14) + " G"
            purchase.karat_21 = str(weight21) + " G"
            purchase.karat_22 = str(weight22) + " G"
            purchase.karat_24 = str(weight24) + " G"
            karat_21_conversion_total = (((weight9 * 9) / 21) + ((weight24 * 24) / 21) + ((weight22 * 22) / 21) + (
                    (weight18 * 18) / 21) + ((weight12 * 12) / 21) + ((weight14 * 14) / 21) + weight21)
            purchase.total_21_karats = karat_21_conversion_total

            for gold in self:
                for product in gold.order_line:
                    total_gold += product.gold_price_total
                    total_labor += product.labor_price_total

            gold.total_price_gold = total_gold
            gold.total_labor_vendor = total_labor

    @api.onchange('tax_totals_json', 'partner_id')
    def _check_for_gold_credit_limit(self):
        """ Function to check if credit limit is greater than or not"""
        data_json = json.loads(self.tax_totals_json)
        amount_total = data_json['amount_total']
        if self.partner_id.credit_limit != 0:
            if amount_total > self.partner_id.credit_limit or ():
                raise ValidationError(_(" Total is greater than your Credit Limit!!"))
        if self.partner_id.gold_credit_limit != 0:
            if self.total_21_karats > self.partner_id.gold_credit_limit or ():
                raise ValidationError(_(" Total Gold is greater than your Gold Credit Limit!!"))
