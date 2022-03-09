# -*- coding: utf-8 -*-
# from odoo import http


# class Custom-lot(http.Controller):
#     @http.route('/custom-lot/custom-lot', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-lot/custom-lot/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-lot.listing', {
#             'root': '/custom-lot/custom-lot',
#             'objects': http.request.env['custom-lot.custom-lot'].search([]),
#         })

#     @http.route('/custom-lot/custom-lot/objects/<model("custom-lot.custom-lot"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-lot.object', {
#             'object': obj
#         })
