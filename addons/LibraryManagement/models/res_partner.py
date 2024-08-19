'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields


class Customer (models.Model):

    _description = ''
    _inherit='res.partner'

    borrowing = fields.One2many('library.borrow', 'borrower_id', string ="Borrowing")


class User(models.Model):
    _description = ''
    _inherit='res.users'


    def _default_customer(self):
        return self.env['res.partner'].search([('id','=',self.env.user.partner_id.id)])
