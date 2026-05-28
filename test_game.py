import unittest
from game import TicTacToe  # импортируем класс игры из файла game.py


class TestTicTacToe(unittest.TestCase):  # класс с тестами, наследуется от unittest

    def test_board_creation(self):  # тест №1: проверяем что игровое поле создаётся
        game = TicTacToe()  # создаём объект игры
        self.assertIsNotNone(game.board)  # проверяем что поле существует (не None)

    def test_board_has_9_cells(self):  # тест №2: поле должно иметь 9 клеток
        game = TicTacToe()
        self.assertEqual(len(game.board), 9)  # проверяем что длина списка равна 9