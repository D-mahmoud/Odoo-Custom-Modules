# -*- coding: utf-8 -*-
from odoo import models, fields, api

class goldPrice(models.Model):
    _name = 'gold.price'
    _description = 'gold price'

    gold_price = fields.Float(string='Gold Price' ,required=True,help="set gold price to day")
    today = fields.Datetime(string='Gold Price Date', required=True, default= fields.datetime.now())
    name = fields.Char(string="Name", required=False, help="Write your name")

#osama
