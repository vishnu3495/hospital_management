from odoo import models, fields,_,api

class SaleOrderInherit(models.Model):
    _inherit='sale.order'

    patient_name=fields.Char(string='Patient Name')



class SaleMoveLine(models.Model):
    _inherit='sale.order.line'

    reference = fields.Integer(string='Reference')