from odoo import models, fields, api

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The category name must be unique.'),
    ]
