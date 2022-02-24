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
    

   

        # account_move = self.env['account.move']
        # for order in self:
        #     tax_lines_data = account_move._prepare_tax_lines_data_for_totals_from_object(order.order_line, compute_karat)
        #     tax_totals = account_move._get_tax_totals(order.partner_id, tax_lines_data, order.amount_total, order.amount_untaxed, order.currency_id)
        #     order.tax_totals_json = json.dumps(tax_totals)


    
    # @api.onchange('product_qty')
    # def product_change(self):
    #     # prod = self.product_id.id
    #     product_karat = self.env['product.template'].search([('id', '=', self.product_id.id)])
      
     
    
