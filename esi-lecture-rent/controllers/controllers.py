# -*- coding: utf-8 -*-
# from odoo import http


# class Esi-lecture-rent(http.Controller):
#     @http.route('/esi-lecture-rent/esi-lecture-rent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/esi-lecture-rent/esi-lecture-rent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('esi-lecture-rent.listing', {
#             'root': '/esi-lecture-rent/esi-lecture-rent',
#             'objects': http.request.env['esi-lecture-rent.esi-lecture-rent'].search([]),
#         })

#     @http.route('/esi-lecture-rent/esi-lecture-rent/objects/<model("esi-lecture-rent.esi-lecture-rent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('esi-lecture-rent.object', {
#             'object': obj
#         })
