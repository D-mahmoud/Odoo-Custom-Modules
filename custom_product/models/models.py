# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError


class Product(models.Model):
    _inherit = 'product.template'
    
    karat = fields.Selection(
    string='Karat',
    selection=  [('9', '9'),
                ('12', '12'),
                ('14', '14'),
                ('18', '18'),
                ('21', '21'),
                ('22', '22')],)
         
 


    has_stones = fields.Boolean('Stones Weight Included')
    has_stones_price = fields.Boolean('Stones Price Included')
    product_type_name = fields.Many2one(string='Product Stone Type',comodel_name='product.type')
    item_cat = fields.Selection([
        ('1', 'Gold'),('2', 'Stone')
    ], string='Item Category')
    @api.onchange('seller_ids')
    def _onchange_(self):
       num_vend = len(self.seller_ids)
       if num_vend > 1 :
            raise ValidationError("Please one Vendor")

class Serial(models.Model):
    _inherit = 'stock.production.lot'
    gross_weight =fields.Float(
    'Gross Weight',
    digits=(12,4) )
    net_weight =fields.Float(
    'Net Weight',
    digits=(12,4) )
    # gold_ids = fields.One2many('gold_price', 'karat', string='Gold Calc')
    

