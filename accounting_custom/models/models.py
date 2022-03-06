from odoo import models, fields, api
from odoo.exceptions import ValidationError
from logging import info


class AccountMoveCustom(models.Model):
    
    _inherit = 'account.move'
    
    sale_mode = fields.Selection([('1', 'Fixed'),('2', 'Daily')],string="Sale Base",compute='_compute_line_mode' ,store=True)
    credit_gold      = fields.Float('Gold Cre.',digits=(12,4),compute='_compute_line_mode' ,store=True)
    @api.depends('invoice_date')
    def _compute_line_mode(self):
        # self.credit_gold = 15569
        sale_orderk = self.env['sale.order'].search([('name','=',self.invoice_origin)]).sale_mode
        self.sale_mode = sale_orderk   
        
    # def action_post(self):
    #     account_sale_mode = self.env['account.move.line'].search([('move_id','=',self.id)])
    #     account_line = self.env['account.move.line'].search([('move_id','=',96)])
        
    #     for rec in account_sale_mode :
    #         self.credit_gold = rec.id
    #         # rec.write({'credit_gold':self})
    #     # info("=---------------================================",account_sale_mode)
    #     # for rec in self.invoice_line_ids
    #     # raise ValidationError(account_moved.id)
    #     return super(AccountMoveCustom, self).action_post()


        
class AccountMoveLineCustom(models.Model):
    
    _inherit = 'account.move.line'
    
    testf = fields.Char(string="Testing")
    credit_gold      = fields.Float('Gold Cre.',digits=(12,4) ,compute='_compute_line_weight',store=True )
    debit_gold       = fields.Float('Gold De.',digits=(12,4) ,compute='_compute_line_weight',store=True)
    
    @api.depends('create_date')
    def _compute_line_weight(self):
        if self.move_id.sale_mode == "1" :
            sum_qty=0
            for rec in self :
                if rec.credit > 0 and rec.debit <=0 :
                    rec.credit_gold = rec.quantity
                    sum_qty +=rec.quantity
                    rec.debit_gold = 0
                elif rec.credit <= 0 and rec.debit >0 :
                    rec.credit_gold = 0
                    rec.debit_gold = sum_qty
    # def action_post(self):
    #     account_sale_mode = self.env['account.move.line'].search([('move_id','=',self.id)])
    #     account_line = self.env['account.move.line'].search([('move_id','=',96)])
        
    #     for rec in account_sale_mode :
    #         raise ValidationError(rec.id)
    #         # self.credit_gold = rec.id
    #         # rec.write({'credit_gold':self})
    #     # info("=---------------================================",account_sale_mode)
    #     # for rec in self.invoice_line_ids
    #     # raise ValidationError(account_moved.id)
    #     return super(AccountMoveLineCustom, self).action_post()