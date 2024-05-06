# -*- coding: utf-8 -*-
# from odoo import http


# class Sellos(http.Controller):
#     @http.route('/sellos/sellos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sellos/sellos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sellos.listing', {
#             'root': '/sellos/sellos',
#             'objects': http.request.env['sellos.sellos'].search([]),
#         })

#     @http.route('/sellos/sellos/objects/<model("sellos.sellos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sellos.object', {
#             'object': obj
#         })

