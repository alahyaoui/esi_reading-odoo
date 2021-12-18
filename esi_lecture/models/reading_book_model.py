from datetime import datetime
import logging

_logger = logging.getLogger(__name__)
from odoo import fields, models, api, exceptions


class Book(models.Model):
    _name = 'reading.book'
    _description = 'Books'

    name = fields.Char(string="Titre", compute="_get_title")
    title = fields.Char(string="Titre")
    description = fields.Html(string="Description")
    cover = fields.Binary(string="Cover")
    publication_date = fields.Date(string="Date de publication")
    page_number = fields.Integer(string="Nombre de pages")

    likes_count = fields.Integer(string="Like", compute="_get_likes_count")
    like_status = fields.Char(string="Has Liked ?", compute="_get_like_status")
    users_likes = fields.Many2many('res.users', string="User likes of Book")

    authors_ids = fields.Many2many('res.partner', string="Auteurs")

    # product_id = fields.Many2one('product.template', string="Product")
    products_ids = fields.Many2many('product.template', string="Product(s)")

    _sql_constraints = [
        (
            'esi_lecture_tag_name_unique',
            'UNIQUE (title)',
            'Book title must be unique!'
        )
    ]

    @api.constrains('publication_date')
    def _check_dates(self):
        current_date = datetime.now().date()
        for book in self:
            publication_date = book.publication_date
            if publication_date and current_date:
                if publication_date >= current_date:
                    raise exceptions.ValidationError('The publication date must be anterior to the current date.')

    def _get_title(self):
        for book in self:
            book.name = book.title

    def _get_likes_count(self):
        for book in self:
            book.likes_count = len(book.users_likes)

    def like_unlike(self):
        if self.env.user in self.users_likes:
            self.users_likes -= self.env.user
        else:
            self.users_likes += self.env.user

    def _get_like_status(self):
        if self.env.user in self.users_likes:
            self.like_status = "Vous avez liké"
        else:
            self.like_status = ""

    def __str__(self):
        return f"Book(title={self.title}, description={self.description}, publication_date={self.publication_date}, page_number={self.page_number}, authors_ids={self.authors_ids}"
