# -*- coding: utf-8 -*-
# from odoo import http


# class Custom-module(http.Controller):
#     @http.route('/custom-module/custom-module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-module/custom-module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-module.listing', {
#             'root': '/custom-module/custom-module',
#             'objects': http.request.env['custom-module.custom-module'].search([]),
#         })

#     @http.route('/custom-module/custom-module/objects/<model("custom-module.custom-module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-module.object', {
#             'object': obj
#         })
