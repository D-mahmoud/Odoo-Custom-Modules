# -*- coding: utf-8 -*-

from odoo import models, fields, api


class group(models.Model):
    _name = 'group.group'
    _description = 'group.group'
    _rec_name = 'type'

    group = fields.Selection(
        selection=  [('Vendor', 'Vendor'),
                    ('Customer', 'Customer')],
        string="Group",
        required=True)



    type = fields.Char()


class vendor(models.Model):
    _inherit = 'res.partner'


    group  = fields.Many2one(comodel_name='group.group',domain="[('group','=','Vendor')]", string= 'Group', required=True)
