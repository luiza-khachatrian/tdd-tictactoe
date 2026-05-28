class TicTacToe:  # класс игры крестики-нолики

    def __init__(self):
        self.board = [' '] * 9  # игровое поле 3x3
        self.current_player = 'X'  # первым всегда ходит X

    def make_move(self, position, player):
        if position < 0 or position > 8:  # если позиция вне диапазона 0-8
            return False  # запрещаем ход
        if self.board[position] != ' ':  # если клетка занята
            return False  # запрещаем ход
        self.board[position] = player  # записываем знак игрока
        return True  # ход успешен

    def check_winner(self):
        # все возможные выигрышные комбинации (строки, столбцы, диагонали)
        wins = [
            (0, 1, 2),  # верхняя строка
            (3, 4, 5),  # средняя строка
            (6, 7, 8),  # нижняя строка
            (0, 3, 6),  # левый столбец
            (1, 4, 7),  # средний столбец
            (2, 5, 8),  # правый столбец
            (0, 4, 8),  # диагональ слева направо
            (2, 4, 6),  # диагональ справа налево
        ]
        for a, b, c in wins:  # перебираем все комбинации
            if self.board[a] == self.board[b] == self.board[c] != ' ':  # три одинаковых непустых
                return self.board[a]  # возвращаем знак победителя
        return None  # если победителя нет — None

    def is_draw(self):  # метод проверки ничьей
        return ' ' not in self.board and self.check_winner() is None
        # ничья если: нет пустых клеток И нет победителя

    def switch_player(self):  # метод смены текущего игрока
        if self.current_player == 'X':  # если сейчас X
            self.current_player = 'O'  # меняем на O
        else:  # если сейчас O
            self.current_player = 'X'  # меняем на X

    def reset(self):  # метод сброса игры в начальное состояние
        self.board = [' '] * 9  # очищаем поле
        self.current_player = 'X'  # возвращаем первого игрока

    def empty_cells(self):  # метод подсчёта свободных клеток
        return self.board.count(' ')  # считаем сколько пробелов осталось в списке


# этот блок запускается только если файл запускают напрямую (не через тесты)
if __name__ == '__main__':
    # Создаём экземпляр игры (реализует итерации 1-15)
    game = TicTacToe()

    print("Крестики-нолики!")
    print("Позиции на поле:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")
    print("----------")

    # Основной игровой цикл
    while True:
        # Отображаем текущее состояние доски (итерация 2: доска из 9 клеток)
        print(f"\n{game.board[0]} | {game.board[1]} | {game.board[2]}")
        print(f"{game.board[3]} | {game.board[4]} | {game.board[5]}")
        print(f"{game.board[6]} | {game.board[7]} | {game.board[8]}")

        # Запрашиваем ход у текущего игрока (итерация 4: игрок может сделать ход)
        move = input(f"Игрок {game.current_player}, введи позицию (0-8): ")

        # Проверка: ввод должен быть цифрой (итерация 13: проверка недопустимой позиции)
        if not move.isdigit():
            print("Введи число от 0 до 8!")
            continue

        # Пытаемся выполнить ход.
        # make_move() проверяет:
        # - выход за границы (итерация 13)
        # - занята ли клетка (итерация 5: нельзя ходить на занятую клетку)
        if not game.make_move(int(move), game.current_player):
            print("Клетка занята или позиция неверная!")
            continue

        # Проверяем, есть ли победитель после хода.
        # check_winner() проверяет по строкам (итерация 6),
        # столбцам (итерация 7) и диагоналям (итерация 8)
        winner = game.check_winner()
        if winner:
            # Показываем финальное состояние доски
            print(f"\n{game.board[0]} | {game.board[1]} | {game.board[2]}")
            print(f"{game.board[3]} | {game.board[4]} | {game.board[5]}")
            print(f"{game.board[6]} | {game.board[7]} | {game.board[8]}")
            print(f"Игрок {winner} победил!")
            break

        # Проверка на ничью (итерация 10: определение ничьей)
        # is_draw() использует подсчёт пустых клеток (итерация 15)
        if game.is_draw():
            print("Ничья!")
            break

        # Меняем игрока (итерация 11 и 12: смена игрока после хода)
        game.switch_player()
