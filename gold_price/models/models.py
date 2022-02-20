# -*- coding: utf-8 -*-
from email.policy import default
import string
from odoo import models, fields, api

class goldPrice(models.Model):
    _name = 'gold.price'
    _description = 'gold price'
    karat = fields.Selection([('21K','21K'),('18K','18K')],string="Karat", required=True)
    gold_price = fields.Float(string='Gold Price' ,required=True,help="set gold price to day")
    day = fields.Datetime(string="Active From Date",required=True , default = lambda self : fields.datetime.now()   )
    active = fields.Boolean(string="Active")
    text = fields.Char(string='TEXT')

    @api.constrains()
    def create_record(self):
        
        self.env['gold.price'].search([('karat','=',self.karat),('id' ,'!=',self.id)]).write({'active': False })
        # self.text = last_id
        # self.active = True
