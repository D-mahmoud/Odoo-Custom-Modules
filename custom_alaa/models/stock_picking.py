# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime
import logging


class Stock(models.Model):
    _inherit = "stock_picking"
