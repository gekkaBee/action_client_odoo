# -*- coding: utf-8 -*-
# from odoo import http


# class ActionClientOdoo(http.Controller):
#     @http.route('/action_client_odoo/action_client_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/action_client_odoo/action_client_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('action_client_odoo.listing', {
#             'root': '/action_client_odoo/action_client_odoo',
#             'objects': http.request.env['action_client_odoo.action_client_odoo'].search([]),
#         })

#     @http.route('/action_client_odoo/action_client_odoo/objects/<model("action_client_odoo.action_client_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('action_client_odoo.object', {
#             'object': obj
#         })
