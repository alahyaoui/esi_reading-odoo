from datetime import datetime
from odoo import fields, models, api, exceptions


class Member(models.Model):
    _inherit = 'res.partner'

    number = fields.Char(string="Matricule")
    rent_ids = fields.One2many('reading.rent', 'member_id', string="Prêts")
