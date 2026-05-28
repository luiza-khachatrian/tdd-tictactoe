class TicTacToe:  # класс игры крестики-нолики

    def __init__(self):  # метод инициализации, вызывается при создании объекта
        self.board = [' '] * 9  # игровое поле: список из 9 пробелов (3x3)

    def make_move(self, position, player):      # метод хода с проверкой
        if self.board[position] != ' ':         # если клетка уже занята
            return False                        # запрещаем ход, возвращаем False
        self.board[position] = player           # иначе записываем знак игрока
        return True                             # возвращаем True — ход успешен