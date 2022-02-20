# -*- coding: utf-8 -*-

from odoo import models, fields, api
from logging import NullHandler,info
import itertools


class custom_lot(models.Model):
    _name = 'custom_lot.custom_lot'
    _description = 'custom_lot.custom_lot'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class lot(models.Model):
    _inherit = 'stock.move'
    

    fixed_qty = fields.Boolean(string='Fixed Quantity')
    number_of_pieces= fields.Integer(string='Number of Pieces')


    seq = fields.Char(
        string='Start serial sequence',
    )
    hide =  fields.Boolean(string='hide')
    @api.onchange('fixed_qty')
    def confirm(self):
        
       
        if self.fixed_qty == True:
            self.hide = False
        else:
           self.hide = True
           
    @api.onchange('seq')
    def get_serial(self):
        
            def separate(string):
                return ["".join(group) for key, group in itertools.groupby(string, str.isdigit)]
            
            
            sequence2   = separate(self.seq)
            
            first_len   = len(sequence2)-2
            last_len    = len(sequence2)-1
            first_seq   = sequence2[first_len]
            last_seq    = sequence2[last_len]
            
            
            # self.env['stock.move.line'].new
            
            number_of_pe = self.number_of_pieces 
            if number_of_pe != 0 :
                seq_num = number_of_pe
            elif number_of_pe == 0 or number_of_pe == "" :
                seq_num = 1
            piece_qty = (self.product_uom_qty) / seq_num
            num_seq = int(last_seq)
               
            for rec in range(seq_num):
                sequ_str = str(first_seq)
               
               
                sequ = str("%0002d" % num_seq)
                seqy=(sequ_str + sequ)
                self.move_line_nosuggest_ids = [(0, 0, {'product_id': self.product_id.id,
                'lot_name': seqy,
                'move_id' : self.id,
                'picking_id': self.picking_id.id,
                'qty_done': piece_qty,
                'product_uom_id' : self.product_uom.id})]
        
                num_seq+=1
            
            


