from django.test import TestCase

from ..models import Board


class BoardTest(TestCase):
    def test_save_board(self):
        board = Board()
        board.name = 'Pre-Production'
        board.slug = 'pre-production'
        board.save()

        board = Board.objects.last()

        self.assertEqual(board.name, 'Pre-Production')
        self.assertEqual(board.slug, 'pre-production')

    def test_board_should_represent_name_by_default(self):
        board = Board.objects.create(
            name='Pre-Production',
            slug='pre-production'
        )
        self.assertEquals(board.__str__(), 'Pre-Production')

    def test_slug_should_be_autogenerated_from_board_name(self):
        board = Board.objects.create(
            name='Pre-Production')

        self.assertEquals(board.slug, 'pre-production')
