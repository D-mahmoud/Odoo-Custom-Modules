# -*- coding: utf-8 -*-
# from odoo import http


# class NewPurchaseCustom(http.Controller):
#     @http.route('/new_purchase_custom/new_purchase_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_purchase_custom/new_purchase_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_purchase_custom.listing', {
#             'root': '/new_purchase_custom/new_purchase_custom',
#             'objects': http.request.env['new_purchase_custom.new_purchase_custom'].search([]),
#         })

#     @http.route('/new_purchase_custom/new_purchase_custom/objects/<model("new_purchase_custom.new_purchase_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_purchase_custom.object', {
#             'object': obj
#         })
