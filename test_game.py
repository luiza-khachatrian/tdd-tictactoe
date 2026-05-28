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

    def test_winner_row(self):  # тест №6: победа по горизонтали
        game = TicTacToe()
        game.make_move(0, 'X')  # X на позицию 0
        game.make_move(1, 'X')  # X на позицию 1
        game.make_move(2, 'X')  # X на позицию 2 — первая строка заполнена
        self.assertEqual(game.check_winner(), 'X')  # победитель должен быть X

    def test_winner_column(self):  # тест №7: победа по вертикали
        game = TicTacToe()
        game.make_move(0, 'O')  # O на позицию 0
        game.make_move(3, 'O')  # O на позицию 3
        game.make_move(6, 'O')  # O на позицию 6 — левый столбец заполнен
        self.assertEqual(game.check_winner(), 'O')

    def test_winner_diagonal(self):  # тест №8: победа по диагонали
        game = TicTacToe()
        game.make_move(0, 'X')  # X на позицию 0
        game.make_move(4, 'X')  # X на позицию 4 (центр)
        game.make_move(8, 'X')  # X на позицию 8 — главная диагональ
        self.assertEqual(game.check_winner(), 'X')

    def test_no_winner(self):  # тест №9: победителя нет
        game = TicTacToe()
        game.make_move(0, 'X')
        game.make_move(1, 'O')  # поле заполнено частично, победителя нет
        self.assertIsNone(game.check_winner())  # должно вернуть None

    def test_draw(self):  # тест №10: ничья
        game = TicTacToe()
        # заполняем всё поле так чтобы никто не победил
        moves = ['X', 'O', 'X',
                 'X', 'O', 'X',
                 'O', 'X', 'O']
        for i, player in enumerate(moves):  # enumerate даёт индекс и значение
            game.make_move(i, player)
        self.assertTrue(game.is_draw())  # должно вернуть True — это ничья