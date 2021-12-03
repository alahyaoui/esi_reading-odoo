from datetime import datetime, timedelta

from psycopg2 import IntegrityError

from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestBook, self).setUp(*args, **kwargs)
        # Création d’un nouvel utilisateur pour les tests
        self.fresh_user = self.env['res.users'].create({
            'login': 'bob',
            'name': "Bob Bobman"
        })


    def test_create(self):
        "Create a simple Book."
        Book = self.env['reading.book']
        book = Book.create(
            {
                'title': 'Test Book',
                'page_number': '100',
            }
        )
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.page_number, 100)
        self.assertEqual(len(book.authors_ids), 0)


    def test_update(self):
        "Update a book."
        Book = self.env['reading.book']
        book = Book.create({'title': 'Test Task'})
        book.title = 'Test Task Updated'
        self.assertEqual(book.title, 'Test Task Updated')

    def test_sqlConstraint(self):
        "Sql constraint unique title"
        Book = self.env['reading.book']
        Book.create({
            'title': 'New book',
            'page_number': '100'
        })
        with self.assertRaises(IntegrityError):
            Book.create({'title': 'New book'})

    def test_publication_date(self):
        "Publication is anterior to now"
        Book = self.env['reading.book']
        with self.assertRaises(ValidationError):
            book = Book.create(
                {
                    'title': 'New Book',
                    'publication_date': datetime.now() + timedelta(days=4)
                }
            )

