# -*- coding: utf-8 -*-
# from odoo import http


# class GrandlivreEtBalance(http.Controller):
#     @http.route('/grandlivre_et_balance/grandlivre_et_balance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grandlivre_et_balance/grandlivre_et_balance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('grandlivre_et_balance.listing', {
#             'root': '/grandlivre_et_balance/grandlivre_et_balance',
#             'objects': http.request.env['grandlivre_et_balance.grandlivre_et_balance'].search([]),
#         })

#     @http.route('/grandlivre_et_balance/grandlivre_et_balance/objects/<model("grandlivre_et_balance.grandlivre_et_balance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grandlivre_et_balance.object', {
#             'object': obj
#         })

