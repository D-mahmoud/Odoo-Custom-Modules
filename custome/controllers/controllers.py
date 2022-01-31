# -*- coding: utf-8 -*-
# from odoo import http


# class Custome(http.Controller):
#     @http.route('/custome/custome', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custome/custome/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custome.listing', {
#             'root': '/custome/custome',
#             'objects': http.request.env['custome.custome'].search([]),
#         })

#     @http.route('/custome/custome/objects/<model("custome.custome"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custome.object', {
#             'object': obj
#         })
