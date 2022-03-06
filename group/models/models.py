# -*- coding: utf-8 -*-

from odoo import models, fields, api
from logging import info


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


    # group  = fields.Many2one(comodel_name='group.group',domain=_getUserGroupId, string= 'Group', required=True)
    type_contact = fields.Char(string="types")

    sale_mode = fields.Selection([('1', 'Fixed'),('2', 'Daily')],string="Sale Base")
    
    group  = fields.Many2one(comodel_name='group.group', string= 'Group', required=True)

    
    # @api.depends('customer_rank','supplier_rank')
    # def change_group(self):
    #     if self.supplier_rank==1 :
    #           self.type_contact = 1

    #     elif self.customer_rank==1 :
    #           self.type_contact = 2

            
    