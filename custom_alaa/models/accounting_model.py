# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Accounting(models.Model):
    _inherit = 'account.move'
