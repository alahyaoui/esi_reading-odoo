from datetime import datetime
from odoo import fields, models, api, exceptions


class Rent(models.Model):
    _name = 'reading.rent'
    _description = 'Book Rents'

    state = fields.Selection(
        [('rented', 'Exemplaire prêté'), ('returned', 'Exemplaire retourné'), ('lost', 'Exemplaire perdu')],
        string="State", default='rented')

    rent_date = fields.Datetime(string="Date d'emprunt", default=lambda self: fields.datetime.now())
    return_date = fields.Datetime(string="Date de retour")

    book_id = fields.Many2one('reading.book', string='Livre prêté', required=True)
    member_id = fields.Many2one('res.partner', string='Membre', required=True)

    def set_lost(self):
        self.state = 'lost'

    def set_returned(self):
        self.state = 'rented'

    def write(self, values):
        if values['state'] == 'rented' and self.state != 'returned':
            raise exceptions.ValidationError('Le livre doit etre retourné avant de pouvoir etre de nouveau emprunté.')
        return super(Rent, self).write(values)
