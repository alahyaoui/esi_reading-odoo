from odoo import fields, models, api, exceptions


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    #product_books = fields.One2many('reading.book','product_id', string="Livre(s)")
    books_ids = fields.Many2many('reading.book', string="Livre(s)")
