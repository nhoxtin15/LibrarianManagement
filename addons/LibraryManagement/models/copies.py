from odoo import models, fields, api,exceptions
import datetime
class Copies(models.Model):
    _name = 'library.copies'
    _description = "Book's copies"


    name = fields.Char(string = "Name", readonly=True)

    book_id = fields.Many2one('library.book', string="Book")

    location_id = fields.Many2one('library.area', string="Location")

    status = fields.Selection([
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost'),
    ], string="Status", default='available')

    acquisition_date = fields.Date(string="Acquisition Date", default = fields.Date.today())

    condition = fields.Selection([
        ('new', 'New'),
        ('good', 'Good'),
        ('bad', 'Bad'),
    ], string="Condition", default='new')

    borrow = fields.One2many('library.borrow','borrowing', string ="Borrow")

    base_price = fields.Float(string="Price")
    is_available = fields.Boolean(default=True)
    def _compute_name(self):
        return f"{self.book_id.copies_count} - {self.book_id.title} - {self.acquisition_date}"

    @api.model
    def create(self,vals):
        res = super(Copies,self).create(vals)
        res.name = res._compute_name()
        res.book_id.copies_count = res.book_id.copies_count+1
        return res

    def create_borrow(self):

        self.env['library.borrow'].create({
            'borrowing': self.id,
            'user_id': self.env.user.id,
            'borrower_id': self.env.user.partner_id.id,  # Assuming current user as the borrower
            'borrow_date': fields.Date.today(),
            'due_date': fields.Date.today() + datetime.timedelta(days=14),
            'status': 'unconfirmed'
        })
        self.sudo().status = 'borrowed'
        self.sudo().is_available = False

    @api.onchange('status')
    def _onchange_status(self):
        if self.status == 'available':
            self.is_available = True
        else:
            self.is_available = False
