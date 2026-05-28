import unittest
from game import TicTacToe  # импортируем класс игры из файла game.py


class TestTicTacToe(unittest.TestCase):  # класс с тестами, наследуется от unittest

    def test_board_creation(self):  # тест №1: проверяем что игровое поле создаётся
        game = TicTacToe()  # создаём объект игры
        self.assertIsNotNone(game.board)  # проверяем что поле существует (не None)

    def test_board_has_9_cells(self):  # тест №2: поле должно иметь 9 клеток
        game = TicTacToe()
        self.assertEqual(len(game.board), 9)  # проверяем что длина списка равна 9

    def test_board_is_empty(self):  # тест №3: поле изначально пустое
        game = TicTacToe()
        self.assertTrue(all(cell == ' ' for cell in game.board))  # все клетки = пробел

    def test_player_x_can_move(self):  # тест №4: игрок X может сделать ход
        game = TicTacToe()
        game.make_move(0, 'X')  # делаем ход на позицию 0
        self.assertEqual(game.board[0], 'X')  # проверяем что клетка 0 теперь = 'X'

    def test_cannot_move_to_occupied_cell(self):  # тест №5: нельзя ходить на занятую клетку
        game = TicTacToe()
        game.make_move(0, 'X')  # X занимает клетку 0
        result = game.make_move(0, 'O')  # O пытается занять ту же клетку
        self.assertFalse(result)  # должно вернуть False — ход запрещён



