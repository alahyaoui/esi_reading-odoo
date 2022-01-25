from odoo import fields, models, api


class Book(models.Model):
    _inherit = 'reading.book'

    rent_count = fields.Integer(string="Nombre d'emprunts", compute="_get_rent_count")
    rent_ids = fields.One2many('reading.rent', 'book_id', string="Emprunts")

    @api.depends('rent_count')
    def _get_rent_count(self):
        for book in self:
            book.rent_count = len(book.rent_ids)
