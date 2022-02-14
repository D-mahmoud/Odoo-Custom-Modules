# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.template'
    

    karat = fields.Many2one(string='Karat', comodel_name='gold.price',)

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
    

# class due(models.Model):
#     _inherit = 'res.partner'
#     total_due =fields.Float(
#     'Gross Weight',
#     digits=(12,4) )
    

# class Karat(models.Model):
#     _name = 'custom_product.karat'

#     karat = fields.Integer(string="Karat", required=True)
#     price = fields.Float(string="Price", required=True,  digits=(12,4),  ondelete='restrict',)
#     date = fields.Date(string="Active From Date",required=True, ondelete='restrict',)
    