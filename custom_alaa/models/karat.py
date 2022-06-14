# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime
import logging


class karat(models.Model):
    _name = 'karat.model'
    _rec_name = 'karat'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    karat = fields.Integer(required=True, string="Karat")
    price = fields.Float(string="Price")
    karat_date = fields.Datetime(string="Active From Date",
                             default=lambda self: fields.Datetime.to_string(datetime.datetime.now()))
    main_karat = fields.Boolean(string="Main Karat")
    last_date = fields.Char(string="Last Date")
    _logger = logging.getLogger(__name__)

    _sql_constraints = [
        ('unique_karat', 'unique (karat)', 'This karat already exists!'),
    ]
    #
    # @api.onchange("karat_date")
    # def _get_last_date(self):
    #     record_ids = self.search([('karat_date', '=', self.karat_date.id)], order='id desc', limit=1)
    #     self.last_date = record_ids.id

    @api.onchange('karat_date')
    def _check_date(self):
        """ Validation for karat date """
        if self.karat_date and self.karat_date < datetime.date.today():
            raise ValidationError('Active date must be after today.')

    @api.model
    @api.onchange('price', 'main_karat')
    def _onchange_price(self):
        """ Function to generate price for other karats """
        self.karat_date = datetime.date.today()
        for mainKaratid in self:
            if (mainKaratid.main_karat == True):
                main_karat_price = mainKaratid.price
                main_karat_name = mainKaratid.karat
            else:
                main_karat_price = 1
                main_karat_name = 1
        not_main_karats = self.search([('main_karat', '=', False)])
        for i in not_main_karats:
            i.price = (i.karat / main_karat_name) * main_karat_price

    @api.onchange('main_karat')
    def check_main_karat(self):
        """ Function to make only one main karat """
        self.karat_date = datetime.date.today()
        main_karat_true = self.search([('main_karat', '=', True)])
        for i in main_karat_true:
            i.main_karat = False
