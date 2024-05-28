# -*- coding: utf-8 -*-
# from odoo import http


# class HotelJh(http.Controller):
#     @http.route('/hotelitic/hotelitic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotelitic/hotelitic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotelitic.listing', {
#             'root': '/hotelitic/hotelitic',
#             'objects': http.request.env['hotelitic.hotelitic'].search([]),
#         })

#     @http.route('/hotelitic/hotelitic/objects/<model("hotelitic.hotelitic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotelitic.object', {
#             'object': obj
#         })
