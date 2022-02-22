# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gold_payment(models.Model):
#     _name = 'gold_payment.gold_payment'
#     _description = 'gold_payment.gold_payment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
