# -*- coding: utf-8 -*-
# from odoo import http


# class Group(http.Controller):
#     @http.route('/group/group', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/group/group/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('group.listing', {
#             'root': '/group/group',
#             'objects': http.request.env['group.group'].search([]),
#         })

#     @http.route('/group/group/objects/<model("group.group"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('group.object', {
#             'object': obj
#         })
