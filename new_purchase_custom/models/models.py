from odoo import models, fields, api
import itertools
from logging import info
from odoo.exceptions import ValidationError,UserError
import itertools
from decimal import Decimal
 



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
    labor_price= fields.Float('Labor Price')
    date = fields.Datetime('Date')
    active = fields.Boolean(string="Active")