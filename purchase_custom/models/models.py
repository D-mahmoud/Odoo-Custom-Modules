from odoo import models, fields, api
import itertools
from logging import info
from odoo.exceptions import ValidationError,UserError
import itertools
from decimal import Decimal


class SaleOrder(models.Model):
    _inherit = 'purchase.order'
    sale_mode   = fields.Selection([('1', 'Fixed'),('2', 'Daily')],string="Sale Base")
    k9          = fields.Float(string='Karat 9k Weight  (G)',compute='_compute_line_weight',store= True)
    k12         = fields.Float(string='Karat 12k Weight (G)',compute='_compute_line_weight',store= True)
    k14         = fields.Float(string='Karat 14k Weight (G)',compute='_compute_line_weight',store= True)
    k18         = fields.Float(string='Karat 18k Weight (G)',compute='_compute_line_weight',store= True)
    k21         = fields.Float(string='Karat 21k Weight (G)',compute='_compute_line_weight',store= True)
    k22         = fields.Float(string='Karat 22k Weight (G)',compute='_compute_line_weight',store= True)
    k24         = fields.Float(string='Karat 24k Weight (G)',compute='_compute_line_weight',store= True)
    c_karat     = fields.Float(string='Converted Karat Weight (G)',compute='_compute_line_weight',store= True)
    
    tesxt = fields.Char(string="tesxt")

    @api.onchange('sale_mode')
    def _onchange_base(self):
        for red in self :
            red.invoice_ids.sale_mode = self.sale_mode
        
        
    
    @api.onchange('partner_id')
    def _onchange_sale_base(self):
        self.sale_mode = self.partner_id.sale_mode
        
    @api.depends('order_line')
    def _compute_line_weight(self):
      
        line_weight9  = 0
        line_weight12 = 0
        line_weight14 = 0
        line_weight18 = 0
        line_weight21 = 0
        line_weight22 = 0
        line_weight24 = 0
        convert_karat = 0
        karatn        = ""
        for purchase in self:
            for line in purchase.order_line:
                convert_karat = int(line.c_karats)
                karatn        = line.karats
                if line.karats == "9":
                    line_weight9  += line.product_uom_qty
                elif line.karats  == "12":
                    line_weight12 +=  line.product_uom_qty
                elif line.karats  == "14":
                    line_weight1  +=  line.product_uom_qty
                elif line.karats  == "18":
                    line_weight18 +=  line.product_uom_qty
                elif line.karats  == "21":
                    line_weight21 +=  line.product_uom_qty
                elif line.karats  == "22":
                    line_weight22 += line.product_uom_qty
                elif line.karats  == "24":
                    line_weight24 += line.product_uom_qty
            purchase.k9  = line_weight9
            purchase.k12 = line_weight12
            purchase.k14 = line_weight14
            purchase.k18 = line_weight18
            purchase.k21 = line_weight21
            purchase.k22 = line_weight22
            purchase.k24 = line_weight24

            if convert_karat and karatn :
                purchase.c_karat = (((line_weight9 * 9)/convert_karat)
                                        +((line_weight12 * 12)/convert_karat)
                                        +((line_weight14 * 14)/convert_karat)
                                        +((line_weight18 * 18)/convert_karat)
                                        +((line_weight21 * 21)/convert_karat)
                                        +((line_weight22 * 22)/convert_karat)
                                        +((line_weight24 * 24)/convert_karat))

          
    @api.onchange('order_line')
    def serial_uniqe(self):
        self.order_line.update({
                    'sale_sale':  self.sale_mode

                }) 
 
    # @api.onchange('partner id')
    # def onchange_partner_id(self):
    #     for rec in self.order_line:
    #         return {'domain': {'product_id': [('partner_id', '=', rec.saller_ids.name)]}}
   
        
class SaleOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    sale_sale       = fields.Char(string="mode")
    available       = fields.Boolean(default=True)
    net_weight      = fields.Float('Weight',digits=(12,4) )
    making_price    = fields.Float('Cost',digits=(12,4),readonly=True)
    gold_price      = fields.Float('Gold Price',digits=(12,4),readonly=True)
    karats          = fields.Char('Karat',readonly=True)
    weight          = fields.Float('Weight',digits=(12,4) )
    c_karats        = fields.Char(string='C Karat',store= True)

    

  
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        return {'domain': {'product_id': [('seller_ids.name', '=',self.partner_id.id)]}}
   
           
    @api.onchange('product_id','product_qty')
    def product_change(self):
        self.sale_sale  = self.order_id.sale_mode
        gold_p          = self.env['gold.price']
        prod            = self.product_id.id
        product_product = self.env['product.product'].search([('id', '=', prod)]).product_tmpl_id
        karat           = product_product.karat
        making          = product_product.standard_price

        
        for rec in self:
                rec.karats          = karat
                latest_price        = gold_p.search([('karat' , '=',rec.karats)], limit=1, order='day desc').gold_price
                convert_karat       = gold_p.search([('karat' , '=',rec.karats)], limit=1, order='day desc').conversion_karat
                rec.c_karats        = convert_karat
                rec.gold_price      = latest_price
                rec.making_price    = making
                rec.product_id      = prod 
                serials_qty         = rec.product_qty
                convert_int = float(convert_karat)
                qty_m_karat  =  serials_qty * float(karat) 
                if convert_karat and karat:
                    rec.weight          = qty_m_karat / convert_int
                
                if rec.sale_sale == "1" :
                    
                    rec.update({
                            'price_unit' : rec.making_price 
                        })
                elif rec.sale_sale == "2" :
                    rec.update({
                            'price_unit' :  rec.making_price + latest_price
                     })
                     