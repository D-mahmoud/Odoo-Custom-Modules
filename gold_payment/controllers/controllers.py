# -*- coding: utf-8 -*-
# from odoo import http


# class GoldPayment(http.Controller):
#     @http.route('/gold_payment/gold_payment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gold_payment/gold_payment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gold_payment.listing', {
#             'root': '/gold_payment/gold_payment',
#             'objects': http.request.env['gold_payment.gold_payment'].search([]),
#         })

#     @http.route('/gold_payment/gold_payment/objects/<model("gold_payment.gold_payment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gold_payment.object', {
#             'object': obj
#         })
