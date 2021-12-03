from odoo import fields, models, api, exceptions


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_author = fields.Boolean(string='Is Author?', default=False)

    books_ids = fields.Many2many('reading.book', string="Books")
    books_count = fields.Integer(string="Books count", compute='_get_books_count', store=True)

    @api.depends('books_count')
    def _get_books_count(self):
        for r in self:
            r.books_count = len(r.books_ids)
