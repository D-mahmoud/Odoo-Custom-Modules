# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class alaapractice(models.Model):
    _name = 'alaapractice.model'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']

    company_id = fields.Many2one(
        'res.company', required=True, default=lambda self: self.env.company
    )
