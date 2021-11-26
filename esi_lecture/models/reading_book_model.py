from datetime import time

from odoo import fields, models, api
from odoo.fields import Datetime


class Book(models.Model):
    _name = 'reading.book'
    _description = 'Books'

    title = fields.Char(string="Titre")
    description = fields.Html(string="Description")
    cover = fields.Binary(string="Cover")
    publication_date = fields.Date(string="Date de publication")
    page_number = fields.Integer(string="Nombre de pages")

    authors_ids = fields.Many2many('res.partner', string="Auteurs")

    _sql_constraints = [
        (
            'esi_lecture_tag_name_unique',
            'UNIQUE (title)',
            'Book title must be unique!'
        )
    ]

    #@api.constrains('publication_date')
    def _check_dates(self):
        publication_date = self.publication_date
        current_date = Datetime.now()# .strftime('%d-%m-%Y')
        if publication_date and current_date:
            if publication_date < current_date:
                return True
        return False

    _constraints = [
        (_check_dates, 'The publication date must be anterior to the current date.', ['publication_date'])
    ]
