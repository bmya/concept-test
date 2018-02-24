# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import _, api, fields, models
from odoo.exceptions import UserError
import api2


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api2.localization('cl', True)
    def action_invoice_open(self):
        raise UserError('CONCEPT 02 cl')
