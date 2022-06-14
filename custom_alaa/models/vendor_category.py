# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class vendor_category(models.Model):
    _name = 'vendorcategory.model'
    _rec_name = 'vendor_category_name'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    vendor_category_name = fields.Char(string="Vendor Category Name")
