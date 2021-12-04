from datetime import datetime

from odoo import fields, models, api, exceptions


class Book(models.Model):
    _name = 'reading.book'
    _description = 'Books'

    title = fields.Char(string="Titre")
    description = fields.Html(string="Description")
    cover = fields.Binary(string="Cover")
    publication_date = fields.Date(string="Date de publication")
    page_number = fields.Integer(string="Nombre de pages")

    likes_count = fields.Integer(string="Like", compute="_get_likes_count")
    like_status = fields.Char(string="Has Liked ?", compute="_get_like_status")
    users_likes = fields.Many2many('res.users', string="User likes of Book")

    authors_ids = fields.Many2many('res.partner', string="Auteurs")

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
