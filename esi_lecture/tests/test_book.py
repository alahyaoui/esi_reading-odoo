from odoo.exceptions import UserError, AccessError
from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestBook, self).setUp(*args, **kwargs)
        # Création d’un nouvel utilisateur pour les tests
        self.fresh_user = self.env['res.users'].create({
            'login': 'bob',
            'name': "Bob Bobman"
        })
        self.book_manager = self.env.ref('esi_lecture.book_manager')
        self.newBook = self.env['reading.book'].create({
            'title': 'New book',
            'page_number': '100'
        })

    def test_create(self):
        "Create a simple Book."
        Book = self.env['reading.book']
        book = Book.create(
            {
                'title': 'Test Book',
                'page_number': '100',
                'authors_ids': {self.fresh_user}
            }
        )
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.page_number, 100)
        self.assertEqual(book.authors_ids[0], self.fresh_user)
        self.assertEqual(len(book.authors_ids), 1)


    def test_update(self):
        "Update a book."
        Book = self.env['reading.book']
        book = Book.create({'name': 'Test Task'})
        book.title = 'Test Task Updated'
        self.assertEqual(book.title, 'Test Task Updated')

    def test_sqlConstraint(self):
        "Sql constraint unique title"
        Book = self.env['reading.book']
        with self.assertRaises(Exception) :
            book = Book.create(
                {
                    'title': 'New Book',
                    'page_number': '100'
                }
            )

    def test_publication_date(self):
        "Publication is anterior to now"
        Book = self.env['reading.book']
        with self.assertRaises(Exception):
            book = Book.create(
                {
                    'title': 'New Book',
                    'page_number': '100'
                }
            )

