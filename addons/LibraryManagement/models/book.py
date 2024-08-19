from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _description = 'Books information'
    _rec_name = 'title'

    title = fields.Char(string ="Book's Title", required = True)
    publish_date = fields.Date(string="Publish Date", required = True)
    language = fields.Char(string="Language", required = True)
    description = fields.Text(string="Description")

    authors = fields.Many2many(
        'library.book.author',  # Correct model name
        'library_book_author_rel',  # Unique relation table
        'book_id',  # Column in relation table for the current model
        'author_id',  # Column in relation table for the related model
        string="Authors",
        required=True
    )

    genre = fields.Many2many(
        'library.book.genre',  # Correct model name
        'library_book_genre_rel',  # Unique relation table
        'book_id',  # Column in relation table for the current model
        'genre_id',  # Column in relation table for the related model
        string="Genre",
        required=True
    )
    publisher = fields.Many2one('library.book.publisher', string="Publisher", required=True)
    copies = fields.One2many('library.copies','book_id', string="Copies")
    copies_count = fields.Integer(string="Count", default = 1)


class Authors(models.Model):
    _name = 'library.book.author'
    _description = "Book's Authors"
    _rec_name = "author_name"

    author_name = fields.Char(string="Author Name", required=True)




class Genre(models.Model):
    _name = "library.book.genre"
    _description ="Book's Genres"

    name = fields.Char(string = "Genre")


class Publisher(models.Model):
    _name = "library.book.publisher"
    _description = "Book's Publisher"

    name = fields.Char(string = "Publisher Name", required=True)


class Area(models.Model):
    _name = "library.area"
    _description = "Book's Area"

    name = fields.Char(string="Area", readonly=True, compute="_compute_location")

    floor = fields.Integer(string = "Floor",default=0)
    shelf = fields.Char(string = "Shelf" ,default="A0")
    row = fields.Integer(string = "Row", default=0)

    @api.depends('floor','shelf','row')
    def _compute_location(self):
        for record in self:
            if(record.floor and record.shelf and record.row):
                area = f"FLoor  {record.floor} - Shelf {record.shelf} - Row {record.row}"
                record.name = area
            else:
                record.name = False