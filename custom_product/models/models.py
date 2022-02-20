# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
                

    # karat = fields.Many2one(
    #     string='Karat',
    #     comodel_name='gold.price',
    #     ondelete='restrict',
    #     index=True)

    # test_case = fields.Boolean('test')

    has_stones = fields.Boolean('Stones Weight Included')
    has_stones_price = fields.Boolean('Stones Price Included')

class Serial(models.Model):
    _inherit = 'stock.production.lot'
    gross_weight =fields.Float(
    'Gross Weight',
    digits=(12,4) )
    net_weight =fields.Float(
    'Net Weight',
    digits=(12,4) )
    
class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    karats = fields.Char(
        string='Karat',
        readonly=True
    )
    gold_price = fields.Float(
        string='Gold Price',
        readonly=True
    )
    
    @api.onchange('product_qty')
    def product_change(self):
        # prod = self.product_id.id
        product_karat = self.env['product.template'].search([('id', '=', self.product_id.id)])
      
     
        self.karats = product_karat.karat2
    
