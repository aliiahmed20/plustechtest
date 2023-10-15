# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def write(self, vals):
        if 'state' in vals and vals['state'] != self.state:
            self.partner_id.message_post(
                body=f"The Order Ref <a href='#' data-oe-model='res.partner' data-oe-id='{self.id}'>{self.name}</a> state changed to %s" % self.state)
        if 'payment_term_id' in vals and vals['payment_term_id'] != self.payment_term_id:
            self.partner_id.message_post(body='The Payment terms for order %s have been changed' % self.name)
        if 'user_id' in vals and vals['user_id'] != self.user_id:
            self.partner_id.message_post(body='Your Salesperson have been changed from %s to %s' % (self.user_id.name, self.env['res.partner'].browse(vals['user_id']).name))
        return super(SaleOrder, self).write(vals)
        
    @api.model
    def create(self, vals):
        self.partner_id.message_post(
            body=f"<a href='#' data-oe-model='res.partner' data-oe-id='{self.id}'>{self.name}</a> Sale Order Created")
        return super(SaleOrder, self).create(vals)
