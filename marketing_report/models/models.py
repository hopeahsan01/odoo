from odoo import models, fields, api


class CrmExtInh(models.Model):
    _inherit = 'crm.lead'
