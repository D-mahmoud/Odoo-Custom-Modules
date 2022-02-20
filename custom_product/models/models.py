# -*- coding: utf-8 -*-

from odoo import models, fields, api




class Product(models.Model):
    _inherit = 'product.template'
    

    karat = fields.Selection([
                        ('21', '21K'),
                        ('18', '18K')], string="Karat")
    karat2 = fields.Char(string="Karat")
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
    
