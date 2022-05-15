from odoo import models, fields, api
import itertools
from logging import info
from odoo.exceptions import ValidationError,UserError
import itertools
from decimal import Decimal
 
# class PurchaseOrder(models.Model):
#     _inherit = 'purchase.order'
   
         
        
class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    serial          = fields.Many2one(string='Serial',comodel_name='stock.production.lot')

class productCalc(models.Model):
    _name = 'product.calc'
    _description = 'product calcolation'
    # _rec_name = ''
    
    calc_id = fields.Many2one('stock.production.lot', string='calc_id', required=True, ondelete='cascade', index=True, copy=False)
    item_cat = fields.Selection([
        ('1', 'Gold'),('2', 'Stone')
    ], string='Item Category')
    item_group = fields.Selection([
        ('1', 'RD')
    ], string='Item Group')
    karat = fields.Selection(
        selection=  [('9', '9k'),
                ('12', '12K'),
                ('14', '14k'),
                ('18', '18k'),
                ('21', '21k'),
                ('22', '22k')],
        string="Karat")
    
    item_groups = fields.Many2one('product.product', string='Item Group')
    item_id = fields.Char('Item Id')
    qty = fields.Float('Quantity')
    size= fields.Float('Size')
    count = fields.Integer(string='Count')
    price= fields.Float('Price')
    consume_qty = fields.Float('Consume Qty')
    
    @api.onchange('count','consume_qty')
    def _onchange_count_qty(self): 
        if self.item_cat == '2':
            if self.consume_qty > 0 and self.count > 0 :
                stone_size = self.consume_qty/self.count
                self.size = stone_size
                prod_type  = self.env['product.type'].search([('item_group', '=', self.item_groups.name)])
                for rec in prod_type :
                    
                    if stone_size >= rec.size_from and stone_size <= rec.size_to :
                        self.price = rec.purchase_price
                        self.item_id = rec.item_name


class Serial(models.Model):
    _inherit = 'stock.production.lot'
    
    calc_ids = fields.One2many('product.calc', 'calc_id', string='Product Calcolation', copy=True, auto_join=True)
    vn = fields.Char('vn')
    @api.onchange('product_id')
    def _onchange_product_id(self):
        number_line = len(self.calc_ids)
        if  number_line > 0 :
            self.calc_ids.unlink()
        self.company_id = self.env.company.id

        if self.product_id :
            bom  = self.env['mrp.bom'].search([('product_tmpl_id', '=', self.product_id.product_tmpl_id.id)]).id

            boms  = self.env['mrp.bom.line'].search([('bom_id', '=', bom)])

            # self.vn = self.product_id.id
            
            for rec in boms :
                    self.calc_ids = [(0, 0, {
                            'item_cat': rec.product_id.item_cat,
                            'item_groups':  rec.product_id.id,
                            'item_id' : '',
                            'qty':rec.product_qty,
                            'size': 0,
                            'count':0 ,
                            'price' :0 })]

class productType(models.Model):
    _name = 'product.type'
    _description = 'productType'
    _rec_name = 'item_group'
    # product_type_name = fields.Char(string='Name')
    item_group = fields.Selection([
        ('RD', 'RD')
    ], string='Item Group')
    item_name = fields.Char('Item Name')
    size_from = fields.Float('Size From')
    size_to = fields.Float('Size To')
    sale_price= fields.Float('Sale Price')
    purchase_price= fields.Float('Purchase Price')
    date = fields.Datetime('Date')
    active = fields.Boolean(string="Active")
    
    
    