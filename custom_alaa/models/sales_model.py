# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class salesOrder(models.Model):
    _inherit = "sale.order"

    # sale_type = fields.Selection([('segmental', 'Segmental'), ('wholesale', 'Wholesale')],
    #                              default='segmental', string="Sale Type")
    sale_mode = fields.Selection([('fixed', 'Fixed'), ('daily', 'Daily')],
                                 default='daily')
    gold_sale_price_total = fields.Float(string="Gold Total (G)")
    labor_sale_price_total = fields.Float(string="Total Labor Price")
    sales_total = fields.Float(string="Total", digits=(2, 0))

    @api.onchange('order_line')
    def _compute_total(self):
        """ Function to calculate Labor Total and Gold per order line """
        labor_total = 0
        gold_total = 0
        serials_numbers_list = []
        for sale in self:
            for product in sale.order_line:
                labor_total += product.labor_price_total
                gold_total += product.gold_price_total
                if product.lot_number.name in serials_numbers_list:
                    raise ValidationError("Serial Number should be Unique in Order Line")
                else:
                    serials_numbers_list.append(product.lot_number.name)

        self.gold_sale_price_total = gold_total
        self.labor_sale_price_total = labor_total

    @api.onchange('sale_mode', 'order_line')
    def _compute_sale_fixed_daily(self):
        """ Function to check about sale type and sale mode and do some calculations """
        # if self.sale_type == "segmental":
        #     for sale in self:
        #         for rec in sale.order_line:
        #             rec.labor_price_total = rec.weight_product * rec.labor_price
        #             rec.gold_price_total = rec.weight_product * rec.price
        #             rec.price_unit = rec.labor_price_total + rec.gold_price_total
        # elif self.sale_type == "wholesale":
        if self.sale_mode == "daily":
            for sale in self:
                for rec in sale.order_line:
                    rec.labor_price_total = rec.weight_product * rec.labor_price
                    rec.gold_price_total = rec.weight_product * rec.price
                    rec.price_unit = rec.labor_price_total + rec.gold_price_total
        elif self.sale_mode == "fixed":
            for sale in self:
                for rec in sale.order_line:
                    rec.labor_price_total = rec.weight_product * rec.labor_price
                    rec.price_unit = rec.labor_price_total


class saleOrderLine(models.Model):
    _inherit = "sale.order.line"
    karat = fields.Many2one('karat.model', string="Karat", related='product_id.product_tmpl_id.karat')
    category_id = fields.Many2one('product.category', string='Category', related='product_id.product_tmpl_id.categ_id')
    category_name = fields.Char(related='category_id.name', string="Category Name")
    weight_product = fields.Float(string="Weight")
    price = fields.Float(string="Price", related='karat.price')
    labor_price = fields.Float(string="Labor Price", related="product_id.product_tmpl_id.list_price")
    labor_price_total = fields.Float(string="Labor Price Total", compute="_compute_labor_price_total")
    gold_price_total = fields.Float(string="Gold Price Total", compute="_compute_gold_price_total")
    scrap = fields.Boolean(string="Gold Scrap")
    lot_number = fields.Many2one('stock.production.lot', string="Serial Number")

    @api.onchange('lot_number')
    def onchange_lot_number(self):
        """ Function to get product by its serial number """
        if self.lot_number:
            serials = self.env['stock.production.lot'].search([('id', '=', self.lot_number.id)])
            if serials:
                prod = serials.product_id
                self.weight_product = serials['weight']
            else:
                raise ValidationError("Serial Number doesnt exist")
            for rec in self:
                rec.product_id = prod
                rec.weight_product = self.weight_product

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

    @api.depends('labor_price_total', 'gold_price_total')
    def _compute_total_labor_gold(self):
        """ Function to set unit price """
        for i in self:
            i.price_unit = i.labor_price_total + i.gold_price_total

    @api.onchange('scrap')
    def _compute_unit_price_scrap(self):
        """ Function to check if is scrap or not and make some calculations """
        if self.scrap:
            self.price_unit = self.gold_price_total
        else:
            self.price_unit = self.labor_price_total + self.gold_price_total
