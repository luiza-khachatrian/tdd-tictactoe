class TicTacToe:  # класс игры крестики-нолики

    def __init__(self):  # метод инициализации, вызывается при создании объекта
        self.board = [' '] * 9  # игровое поле: список из 9 пробелов (3x3)

    def make_move(self, position, player):  # метод хода: принимает позицию и игрока
        self.board[position] = player  # записываем знак игрока в нужную клетку
        return True  # возвращаем True если ход успешен