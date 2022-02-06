# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_product(models.Model):
    _name = 'custom_product.custom_product'
    _description = 'custom_product.custom_product'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class Product(models.Model):
    _inherit = 'product.template'
    

    karat = fields.Selection([
        ('9', '9k'),
        ('18', '18k'), 
        ('21', '21k')], string='Karat')

   
    # test_case = fields.Boolean('test')

    has_stones = fields.Boolean('Stones Weight Included')




class Serial(models.Model):
    _inherit = 'stock.production.lot'
    gross_weight =fields.Float(
    'Gross Weight',
    digits=(12,4) )
    net_weight =fields.Float(
    'Net Weight',
    digits=(12,4) )
    