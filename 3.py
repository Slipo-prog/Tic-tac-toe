board = [1,2,3,4,5,6,7,8,9]
def print_board():
    """игровое поле"""
    for i in range(3):
        print(board[i * 3], board[1 + i * 3], board[2 + i * 3])


def game_step(index, char):
    if (index > 9 or index < 0 or board[index - 1] in ("X", "O")):
        return False
    board[index - 1] = char
    return True

def cheak_win():
    win = False
    win_comb = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )
    for pos in win_comb:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win

def game_start():
    #текущий игрок
    current_player = 'X'
    #первый ход
    step = 1
    print_board()
    while (step < 10 ) and (cheak_win() == False):
        index = input(f"Ходит игрок "  + current_player + ". Введите номер поля(0 - выход): " )
        if index == '0':
            break

        try:
            num = int(index)
        except ValueError:
            print("Вы ввели не число! Попробуйте снова.")
            continue

        if (game_step(int(index), current_player)):
            print("Ход выполнен")
            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'
            print_board()
            step += 1
        else:
            print("Номер занят")
    if step == 10:
        print("Игра окончена. Ничья")
    print("Выиграл игрок " + cheak_win())

game_start()