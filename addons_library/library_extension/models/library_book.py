from odoo import models, fields

class LibraryBook(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one(
        comodel_name="res.partner",
        string="Author",
        required=True,
        ondelete="restrict",
    )

    category_id = fields.Many2many(
        comodel_name="library.book.category",
        relation="library_book_category_rel",
        column1="book_id",
        column2="category_id",
        string="Categories",
    )
