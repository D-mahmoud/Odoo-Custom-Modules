# -*- coding: utf-8 -*-
from odoo import models, fields, api

class goldPrice(models.Model):
    _name = 'gold.price'
    _description = 'gold price'
    karat = fields.Integer(string="Karat", required=True)
    gold_price = fields.Float(string='Gold Price' ,required=True,help="set gold price to day")
    day = fields.Date(string="Active From Date",required=True)
    

   
