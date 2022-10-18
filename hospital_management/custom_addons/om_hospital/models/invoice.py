from odoo import models,fields

class AccountMoveLine(models.Model):
    _inherit='account.move.line'

    line_number=fields.Integer(string='Line Number')

