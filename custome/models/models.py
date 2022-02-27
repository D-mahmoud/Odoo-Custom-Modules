# -*- coding: utf-8 -*-
from odoo import models, fields, api
import itertools
from logging import info
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    sale_mode = fields.Selection([('1', 'Fixed'),('2', 'Daily')],string="Sale Base")
    k9 =fields.Float(string='Karat 9k Weight (G)',compute='_compute_line_weight')
    k12 =fields.Float(string='Karat 12k Weight (G)',compute='_compute_line_weight')
    k14 =fields.Float(string='Karat 14k Weight (G)',compute='_compute_line_weight')
    k18 =fields.Float(string='Karat 18k Weight (G)',compute='_compute_line_weight')
    k21 =fields.Float(string='Karat 21k Weight (G)',compute='_compute_line_weight')
    k22 =fields.Float(string='Karat 22k Weight (G)',compute='_compute_line_weight')
    k24 =fields.Float(string='Karat 24k Weight (G)',compute='_compute_line_weight')
    
    @api.onchange('order_line')
    def _compute_line_weight(self):
        line_weight9  = 0
        line_weight12 = 0
        line_weight14 = 0
        line_weight18 = 0
        line_weight21 = 0
        line_weight22 = 0
        line_weight24 = 0

        for purchase in self:
            for line in purchase.order_line:
                if line.karats == "9":
                    line_weight9+=line.weight
                elif line.karats == "12":
                    line_weight12+=line.weight
                elif line.karats == "14":
                    line_weight14+=line.weight
                elif line.karats == "18":
                    line_weight18+=line.weight
                elif line.karats == "21":
                    line_weight21+=line.weight
                elif line.karats == "22":
                    line_weight22+=line.weight
                elif line.karats == "24":
                    line_weight24+=line.weight
            purchase.k9  = line_weight9
            purchase.k12 = line_weight12
            purchase.k14 = line_weight14
            purchase.k18 = line_weight18
            purchase.k21 = line_weight21
            purchase.k22 = line_weight22
            purchase.k14 = line_weight24
   
          
    @api.onchange('order_line')
    def serial_uniqe(self):
        self.order_line.sale_sale = self.sale_mode
        
        exist_product_list = []
        for purchase in self:
            for line in purchase.order_line:
                if line.serial.id in exist_product_list:
                    raise ValidationError('Serial should be one per line.')
                exist_product_list.append(line.serial.id)
   
class SaleOrder(models.Model):
    _inherit = 'sale.order.line'
    sale_sale = fields.Char(string="mode")
    serial = fields.Many2one(
        string='Serial',
        comodel_name='stock.production.lot',   
    )
    available = fields.Boolean(default=True)
    net_weight =fields.Float('Weight',digits=(12,4) )
    making_price =fields.Float('Cost',digits=(12,4),readonly=True)
    gold_price =fields.Float('Gold Price',digits=(12,4),readonly=True)
    karats = fields.Char('Karat',readonly=True)
    weight =fields.Float('Weight',digits=(12,4) )

    
    @api.onchange('serial')
    def _onchange_(self):
        total_gold=[]
        gold_p = self.env['gold.price']
        
        serials  = self.env['stock.production.lot'].search([('id', '=', self.serial.id)])
       
        prod = serials.product_id.id
        
        product_product = self.env['product.product'].search([('id', '=', prod)]).product_tmpl_id

        karat = product_product.karat
        making = product_product.standard_price

        serials  = self.env['stock.production.lot'].search([('id', '=', self.serial.id)])
        if self.serial.id :
            serials_qty  = self.env['stock.move.line'].search([('lot_id', '=', self.serial.id)]).qty_done
        else:
            serials_qty = 0.00
        
        for rec in self:
            rec.karats = karat
            latest_price = gold_p.search([('karat' , '=',self.karats)], limit=1, order='day desc').gold_price
            rec.gold_price = latest_price
            rec.making_price = making
            rec.product_id = prod 
            rec.weight  =  serials_qty 
            if self.sale_sale == "1":
                rec.price_subtotal = (serials_qty *  making)
                
            elif self.sale_sale =="2":
                rec.price_subtotal = (serials_qty * (making + latest_price))
            total_gold.append({rec.karats:rec.weight})


    




class Serial(models.Model):
    _inherit = 'stock.production.lot'
    gross_weight =fields.Float(
    'Gross Weight',
    digits=(12,4) )
    net_weight =fields.Float(
    'Net Weight',
    digits=(12,4) )
    




class Karat(models.Model):
    _inherit = 'purchase.order.line'
    gold_price =fields.Float('Gold Price',digits=(12,4),readonly=True,store = True)
    karats = fields.Char('Karat',store = True)
    


# class Karat(models.Model):
#     _inherit = 'purchase.order'
   

#     @api.onchange('order_line')
#     def get_data(self):
        
#         product_template = self.env['product.template']
#         product_product = self.env['product.product']
#         for rec in self.order_line:
#             product_templ = product_product.search([('id', '=', rec.product_id.id)]).product_tmpl_id.karat
#             # product_karat = product_template.search([('id', '=', rec.product_templ.id)]).karat
#             rec.karats = product_templ
#             price = self.env['gold.price'].search([('karat', '=', product_templ),('active','=', True)]).gold_price
#             rec.gold_price = price
    
#     tax_karat_json = fields.Char(compute='_compute_karat_totals_json')

#     @api.onchange('order_line')
#     def  _compute_karat_totals_json(self):
#         calc = "omaradel"
#         return calc