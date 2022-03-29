# -*- coding: utf-8 -*-

from odoo import models, fields, api
from logging import info


class group(models.Model):
    _name = 'group.group'
    _description = 'group.group'
    _rec_name = 'group_name'

    group_sel = fields.Selection(
        selection=  [('1', 'Vendor'),
                    ('2', 'Customer')],

        string="Group Type",
        required=True)

    group_id = fields.Integer(string="Group ID",required=True)
    group_name = fields.Char(string="Group Name",required=True)

 
  

class vendor(models.Model):
    _inherit = 'res.partner'


    # group  = fields.Many2one(comodel_name='group.group',domain=_getUserGroupId, string= 'Group', required=True)
    type_contact = fields.Char(string="types")

    sale_mode = fields.Selection([('1', 'Fixed'),('2', 'Daily')],string="Sale Base",required=True)
    
    group  = fields.Many2one(comodel_name='group.group', string= 'Group')

    
    @api.onchange('name','customer_rank','supplier_rank')
    def _onchange_group(self):
        if self.supplier_rank==1 :
              self.type_contact = 1

        elif self.customer_rank==1 :
              self.type_contact = 2

            
    