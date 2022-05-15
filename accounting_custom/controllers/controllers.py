# -*- coding: utf-8 -*-
# from odoo import http


# class AccountingCustom(http.Controller):
#     @http.route('/accounting_custom/accounting_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/accounting_custom/accounting_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('accounting_custom.listing', {
#             'root': '/accounting_custom/accounting_custom',
#             'objects': http.request.env['accounting_custom.accounting_custom'].search([]),
#         })

#     @http.route('/accounting_custom/accounting_custom/objects/<model("accounting_custom.accounting_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('accounting_custom.object', {
#             'object': obj
#         })
