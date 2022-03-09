# -*- coding: utf-8 -*-
# from odoo import http


# class GoldPrice(http.Controller):
#     @http.route('/gold_price/gold_price', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gold_price/gold_price/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gold_price.listing', {
#             'root': '/gold_price/gold_price',
#             'objects': http.request.env['gold_price.gold_price'].search([]),
#         })

#     @http.route('/gold_price/gold_price/objects/<model("gold_price.gold_price"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gold_price.object', {
#             'object': obj
#         })
