{
    "name": "Library Extensions",
    "version": "1.0.0",
    "summary": "Extensions for the library module - author and book categories",
    "author": "Your Name",
    "depends": ["library"],   # depends on the existing library module
    "data": [
        "security/ir.model.access.csv",
        "views/library_book_category_views.xml",
        "views/library_book_views.xml",
    ],
    "installable": True,
    "application": False,
}
