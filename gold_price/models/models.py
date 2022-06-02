# -*- coding: utf-8 -*-
from email.policy import default
import string
from odoo import models, fields, api
from logging import NullHandler,info
from odoo.exceptions import ValidationError

class goldPrice(models.Model):
    _name = 'gold.price'
    _description = 'gold price'
    karat = fields.Selection(
        selection=  [('9', '9'),
                ('12', '12'),
                ('14', '14'),
                ('18', '18'),
                ('21', '21'),
                ('22', '22')],
        string="Karat",
        required=False)
    conversion_karat = fields.Selection(
        selection=  [('9', '9'),
                ('12', '12'),
                ('14', '14'),
                ('18', '18'),
                ('21', '21'),
                ('22', '22')],
        string="Conversion Karat",
        required=False)
    gold_price = fields.Float(string='Gold Price' ,required=True,help="set gold price to day")
    daily_gold_price = fields.Float(string='Sale Gold Price' ,required=True,help="set Daily gold price to day")
    fixed_gold_price = fields.Float(string='Purchase Gold Price' ,required=True,help="set Fixed gold price to day")
    labor_gold_price = fields.Float(string='Labor Gold Price' ,required=True,help="set Labor gold price to day")

    
    day= fields.Datetime(string="Active From Date",required=True , default = lambda self : fields.datetime.now()   )
    active = fields.Boolean(string="Active")
    text = fields.Char(string='TEXT')


    @api.constrains('day')
    def val_date(self):
        date = self.day
        if date.date() < fields.datetime.now().date():
            raise ValidationError("Please select now or future date")
        else :
            self.env['gold.price'].search([('karat','=',self.karat),('id' ,'!=',self.id)]).write({'active': False })
        
    # @api.constrains()
    # def create_record(self):
        
    #     self.env['gold.price'].search([('karat','=',self.karat),('id' ,'!=',self.id)]).write({'active': False })
        # self.text = last_id
        # self.active = True

