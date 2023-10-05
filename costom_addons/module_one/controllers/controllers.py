# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleOne(http.Controller):
#     @http.route('/module_one/module_one', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_one/module_one/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_one.listing', {
#             'root': '/module_one/module_one',
#             'objects': http.request.env['module_one.module_one'].search([]),
#         })

#     @http.route('/module_one/module_one/objects/<model("module_one.module_one"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_one.object', {
#             'object': obj
#         })
