from odoo import fields, models, api, exceptions


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_books = fields.One2many('reading.book', string="Livres associées")
