'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields, api
import datetime

class borrow(models.Model):
    _name = 'library.borrow'
    _description = "Book's Borrowing"

    user_id = fields.Many2one('res.users', string = "Partner",default=lambda self:self.env.user.id, store = True)
    borrower_id = fields.Many2one('res.partner', string = "Borrower", default=lambda  self: self.env.user.partner_id)

    name = fields.Char(string = "Name", readonly = True)

    borrow_date = fields.Date(string="Borrow date", default = fields.Date.today())
    due_date = fields.Date(string="Due date", default = fields.Date.today() + datetime.timedelta(days=14))

    borrowing = fields.Many2one('library.copies', string ="Borrowing")

    status = fields.Selection([
        ('unconfirmed', 'Unconfirmed'),
        ('confirmed', 'Confirmed'),
        ('borrowing', 'Borrowing'),
        ('returned', 'Returned'),
        ('late returned', 'Late Returned'),
        ('late', 'Late'),
    ], string="Status", default='unconfirmed')

    base_price = fields.Float(string="Base Price", related = "borrowing.base_price")
    price = fields.Float(string="Price", compute="_calculate_price")

    is_returned = fields.Boolean()
    is_late = fields.Boolean(compute="_compute_is_late")
    is_confirmed = fields.Boolean(default = False)
    is_not_confirmed = fields.Boolean(default = True)

    @api.depends("due_date")
    def _compute_is_late(self):
        for record in self:
            if(record.due_date):
                record.is_late = record.due_date <= fields.Date.today()
            else:
                record.is_out_of_date = False

    @api.depends('is_late', 'due_date')
    def _calculate_price(self):
        for record in self:
            if (not record.is_late) or (not record.due_date):
                record.price = False
            record.price = record.base_price + record.base_price * 0.1*(fields.Date.today() - record.due_date).days


    @api.onchange('is_returned')
    def _onchange_is_returned(self):
        if(self.is_returned):
            self.status = 'returned'
        else:
            self.status = 'borrowing'

    def confirm(self):
        self.status = 'borrowing'
        self.is_confirmed = True
        self.is_not_confirmed = False

    def cancel(self):
        self.status = 'unconfirmed'
        self.is_confirmed = False
        self.is_not_confirmed = True


