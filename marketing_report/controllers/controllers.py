# -*- coding: utf-8 -*-
# from odoo import http


# class MarketingReport(http.Controller):
#     @http.route('/marketing_report/marketing_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/marketing_report/marketing_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('marketing_report.listing', {
#             'root': '/marketing_report/marketing_report',
#             'objects': http.request.env['marketing_report.marketing_report'].search([]),
#         })

#     @http.route('/marketing_report/marketing_report/objects/<model("marketing_report.marketing_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('marketing_report.object', {
#             'object': obj
#         })

