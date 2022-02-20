# -*- coding: utf-8 -*-
from odoo import models, fields, api
from logging import NullHandler,info
import itertools



class SaleOrder(models.Model):
    _inherit = 'sale.order.line'
    serial = fields.Many2one(
        string='Serial',
        comodel_name='stock.production.lot',   
    )
    available = fields.Boolean(default=True)
    net_weight =fields.Float('Weight',digits=(12,4) )
    making_price =fields.Float('Making Price',digits=(12,4),readonly=True)
    gold_price =fields.Float('Gold Price',digits=(12,4),readonly=True)
    karats = fields.Char('Karat',readonly=True)
    @api.onchange('serial')
    def _onchange_(self):
        gold_p = self.env['gold.price']
        latest_price = gold_p.search([], limit=1, order='today desc').gold_price
        
        serials  = self.env['stock.production.lot'].search([('id', '=', self.serial.id)])
        nets_weight = serials.net_weight
        gross_weight = serials.gross_weight
        prod = serials.product_id.id
        
        product = self.env['product.template'].search([('id', '=', prod)])
        stone_inc =product.has_stones
        karat = product.karat
        making = product.standard_price
        for rec in self:
            
            if stone_inc == True :
                rec.net_weight = nets_weight
            else:
                rec.net_weight = gross_weight
            rec.gold_price = latest_price
            rec.price_subtotal = rec.product_uom_qty * (rec.net_weight * (rec.making_price * latest_price))
            rec.making_price = making
            rec.karats = karat
            rec.product_id=prod 



    




class Serial(models.Model):
    _inherit = 'stock.production.lot'
    gross_weight =fields.Float(
    'Gross Weight',
    digits=(12,4) )
    net_weight =fields.Float(
    'Net Weight',
    digits=(12,4) )
    