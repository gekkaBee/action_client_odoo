# -*- coding: utf-8 -*-
# from odoo import http


# class ../healthsuite-addons/action-client-example(http.Controller):
#     @http.route('/../healthsuite-addons/action-client-example/../healthsuite-addons/action-client-example/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../healthsuite-addons/action-client-example/../healthsuite-addons/action-client-example/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../healthsuite-addons/action-client-example.listing', {
#             'root': '/../healthsuite-addons/action-client-example/../healthsuite-addons/action-client-example',
#             'objects': http.request.env['../healthsuite-addons/action-client-example.../healthsuite-addons/action-client-example'].search([]),
#         })

#     @http.route('/../healthsuite-addons/action-client-example/../healthsuite-addons/action-client-example/objects/<model("../healthsuite-addons/action-client-example.../healthsuite-addons/action-client-example"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../healthsuite-addons/action-client-example.object', {
#             'object': obj
#         })
