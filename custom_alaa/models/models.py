# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# RD BG RT RH

class Product(models.Model):
    _inherit = 'product.template'
    contain_stones = fields.Boolean(string="Contain Stones")
    include_stone_weight = fields.Boolean(string="Include Stone Weight")
    karat = fields.Many2one("karat.model")
    category_name = fields.Char(related='categ_id.name')
    stone_type = fields.Selection([('certified stones', 'Certified Stones'), ('rd', 'RD'), ('bg', 'BG'), ('rt', 'RT'),('rh','RH')],
                                  default='certified stones')
    gold_jewelry = fields.Selection([('rings', 'Rings'), ('bracelet', 'Bracelet')], default="rings")
    diamonds_jewelry = fields.Selection([('rings', 'Rings'), ('bracelet', 'Bracelet')], default="rings")

    price = fields.Float(string="Price", related='karat.price')
    labor_price_total = fields.Float(string="Labor Price Total", compute="_compute_labor_price_total")
    gold_price_total = fields.Float(string="Gold Price Total", compute="_compute_gold_price_total")

    @api.onchange('seller_ids')
    def _onchange_(self):
        """ Function to disallow multiple vendors for a product """
        number_of_vendors = len(self.seller_ids)
        if number_of_vendors > 1:
            raise ValidationError("Disallowed Add Multiple Vendor")
