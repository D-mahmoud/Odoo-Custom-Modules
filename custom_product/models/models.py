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
                
    # karat2 = fields.Char(
    #     string='Karat',
    #     readonly=True
    # )
    # karat = fields.Many2one(
    #     string='Karat',
    #     comodel_name='gold.price',
    #     ondelete='restrict',
    #     index=True)

    # test_case = fields.Boolean('test')

    has_stones = fields.Boolean('Stones Weight Included')
    has_stones_price = fields.Boolean('Stones Price Included')
    
    @api.onchange('seller_ids')
    def _onchange_(self):
       num_vend = len(self.seller_ids)
       if num_vend > 1 :
            raise ValidationError("Please select now or future date")

class Serial(models.Model):
    _inherit = 'stock.production.lot'
    gross_weight =fields.Float(
    'Gross Weight',
    digits=(12,4) )
    net_weight =fields.Float(
    'Net Weight',
    digits=(12,4) )
    
# class PurchaseOrderLine(models.Model):
#     _inherit = 'purchase.order.line'
#     karats = fields.Char(
#         string='Karat',
#         readonly=True
#     )
    
#     gold_price = fields.Float(
#         string='Gold Price',
#         readonly=True
#     )
    
#     @api.onchange('product_qty')
#     def product_change(self):
#         # prod = self.product_id.id
#         product_karat = self.env['product.template'].search([('id', '=', self.product_id.id)])
      
     
    
