# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_lot(models.Model):
    _name = 'custom_lot.custom_lot'
    _description = 'custom_lot.custom_lot'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class lot(models.Model):
    _inherit = 'stock.move'
    

    fixed_qty = fields.Boolean(string='Fixed Quantity')
    number_of_pieces= fields.Integer(string='Number of Pieces')


