import random


def generate_puzzle(size=50):
    puzzle_board = [[" " for i in range(size)] for j in range(size)]
    # print(puzzle_board)
    random_rows = random.choice(range(int(size * 0.9), size))
    # print(random_rows)
    selected_rows = random.sample(range(size), k=random_rows)
    # print(selected_rows)
    for i in selected_rows:
        random_cols = random.choice(range(1, int(size * 0.8)))
        selected_cols = random.sample(range(size), k=random_cols)
        for j in selected_cols:
            puzzle_board[i][j] = 'T'
    for i in puzzle_board:
        print(i)

    add_tent2(puzzle_board, size)

    print('\n')
    for i in puzzle_board:
        print(i)
    # remove_tent(puzzle_board, size)
    # add_direction(puzzle_board, size)
    check_tent2(puzzle_board, size, i, j)

    print('\n')
    for i in range(size):
        for j in range(size):
            if puzzle_board[i][j] == 't':
                puzzle_board[i][j] = 'R'
    for i in puzzle_board:
        print(i)
    hints_top, hints_side = [0] * size, [0] * size

    for i in range(len(puzzle_board)):
        for j in range(len(puzzle_board[0])):
            if puzzle_board[i][j] == 'u' or puzzle_board[i][j] == 'd' or puzzle_board[i][j] == 'l' or puzzle_board[i][
                j] == 'r':
                hints_top[j] += 1
                hints_side[i] += 1
    # print(hints_top, hints_side)
    return puzzle_board, hints_top, hints_side


def print_layout(puzzle_board, hints_top, hints_side, type=0):
    print('\n')
    if type == 0:
        print("This is the puzzle board:")
    else:
        print("This is the answer:")
    # print(puzzle_board)
    top_string = ''
    for i in hints_top:
        top_string += str(i) + ' '
    print(top_string)
    for i in range(len(puzzle_board)):
        temp_row = ''
        for j in range(len(puzzle_board[0])):
            if type == 0:
                if puzzle_board[i][j] == 'u' or puzzle_board[i][j] == 'd' or puzzle_board[i][j] == 'l' or \
                        puzzle_board[i][
                            j] == 'r':
                    temp_row += '  '
                else:
                    temp_row += puzzle_board[i][j] + ' '
            else:

                temp_row += puzzle_board[i][j] + ' '
        temp_row += str(hints_side[i])
        print(temp_row)


def check_tent2(puzzle_board, size, i, j):
    for i in range(size):
        for j in range(size):
            if puzzle_board[i][j] == "t":
                # print(find_tree(puzzle_board, size, i, j))
                if find_tree(puzzle_board, size, i, j) != 'n':
                    puzzle_board[i][j] = find_tree(puzzle_board, size, i, j)


def find_tree(puzzle_board, size, i, j):
    flag, row, col, count = 0, i, j, 0
    while (row >= 0):
        row -= 1
        if puzzle_board[row][col] == ' ':

            count += 1
        elif puzzle_board[row][col] != 'T':
            break
        else:
            if count != 0:
                flag += 1
                direction = 'u'
            break
    row, col, count = i, j, 0
    while (col >= 0):
        col -= 1
        if puzzle_board[row][col] == ' ':

            count += 1
        elif puzzle_board[row][col] != 'T':
            break
        else:
            if count != 0:
                flag += 1
                direction = 'l'
            break
    row, col, count = i, j, 0
    while (row < size - 1):
        row += 1
        if puzzle_board[row][col] == ' ':

            count += 1
        elif puzzle_board[row][col] != 'T':
            break
        else:
            if count != 0:
                flag += 1
                direction = 'd'
            break
    row, col, count = i, j, 0
    while (col < size - 1):
        col += 1
        if puzzle_board[row][col] == ' ':

            count += 1
        elif puzzle_board[row][col] != 'T':
            break
        else:
            if count != 0:
                flag += 1
                direction = 'r'
            break
    if flag == 1:
        return direction
    else:
        return 'n'


def add_tents(puzzle_board, size):
    for i in range(size):
        for j in range(size):
            temp_list = []
            if puzzle_board[i][j] == "E":
                if i >= 1:
                    if puzzle_board[i - 1][j] != "E":
                        temp_list.append([i - 1, j])
                if j >= 1:
                    if puzzle_board[i][j - 1] != "E":
                        temp_list.append([i, j - 1])
                if i <= size - 2:
                    if puzzle_board[i + 1][j] != "E":
                        temp_list.append([i + 1, j])
                if j <= size - 2:
                    if puzzle_board[i][j + 1] != "E":
                        temp_list.append([i, j + 1])
            if len(temp_list) > 0:
                print(i, j, temp_list)
                tent_number = random.choice(range(1, len(temp_list) + 1))
                tent_loc_list = random.sample(temp_list, k=tent_number)
                print(tent_loc_list)
                for t in tent_loc_list:
                    puzzle_board[t[0]][t[1]] = "t"
    for i in puzzle_board:
        print(i)
    print('\n')


def add_tent2(puzzle_board, size):
    for i in range(size):
        for j in range(size):
            if puzzle_board[i][j] == "T":
                if i >= 1:
                    if check_tent(puzzle_board, i - 1, j, size):
                        puzzle_board[i - 1][j] = 't'
                if j >= 1:
                    if check_tent(puzzle_board, i, j - 1, size):
                        puzzle_board[i][j - 1] = 't'
                if i <= size - 2:
                    if check_tent(puzzle_board, i + 1, j, size):
                        puzzle_board[i + 1][j] = 't'
                if j <= size - 2:
                    if check_tent(puzzle_board, i, j + 1, size):
                        puzzle_board[i][j + 1] = 't'


def check_tent(puzzle_board, i, j, size):
    if i >= 1:
        if puzzle_board[i - 1][j] == "t": return False
    if j >= 1:
        if puzzle_board[i][j - 1] == "t": return False
    if i <= size - 2:
        if puzzle_board[i + 1][j] == "t": return False
    if j <= size - 2:
        if puzzle_board[i][j + 1] == "t": return False
    if i >= 1 and j >= 1:
        if puzzle_board[i - 1][j - 1] == "t": return False
    if i >= 1 and j <= size - 2:
        if puzzle_board[i - 1][j + 1] == "t": return False
    if i <= size - 2 and j >= 1:
        if puzzle_board[i + 1][j - 1] == "t": return False
    if i <= size - 2 and j <= size - 2:
        if puzzle_board[i + 1][j + 1] == "t": return False
    return True


def remove_tent(puzzle_board, size):
    for i in range(size):
        for j in range(size):
            if puzzle_board[i][j] == "t":
                if i >= 1:
                    if puzzle_board[i - 1][j] == "t":
                        puzzle_board[i][j] = ' '
                        continue
                if j >= 1:
                    if puzzle_board[i][j - 1] == "t":
                        puzzle_board[i][j] = ' '
                        continue
                if i <= size - 2:
                    if puzzle_board[i + 1][j] == "t":
                        puzzle_board[i][j] = ' '
                        continue
                if j <= size - 2:
                    if puzzle_board[i][j + 1] == "t":
                        puzzle_board[i][j] = ' '
                        continue
                if i >= 1 and j >= 1:
                    if puzzle_board[i - 1][j - 1] == "t":
                        puzzle_board[i][j] = ' '
                        continue
                if i >= 1 and j <= size - 2:
                    if puzzle_board[i - 1][j + 1] == "t":
                        puzzle_board[i][j] = ' '
                        continue
                if i <= size - 2 and j >= 1:
                    if puzzle_board[i + 1][j - 1] == "t":
                        puzzle_board[i][j] = ' '
                        continue
                if i <= size - 2 and j <= size - 2:
                    if puzzle_board[i + 1][j + 1] == "t":
                        puzzle_board[i][j] = ' '
                        continue
    for i in puzzle_board:
        print(i)
    print('\n')


def add_direction(puzzle_board, size):
    for i in range(size):
        for j in range(size):
            if puzzle_board[i][j] == "t":
                if i >= 1 and puzzle_board[i - 1][j] != 'E':
                    pos = i
                    while (pos >= 0):
                        if puzzle_board[pos][j] != 'E':
                            pos -= 1
                        else:
                            puzzle_board[i][j] == "u"
    for i in puzzle_board:
        print(i)
    print('\n')


# print(random.choice([1,2,3]))
puzzle_board, hints_top, hints_side = generate_puzzle()
print_layout(puzzle_board, hints_top, hints_side, 1)
print_layout(puzzle_board, hints_top, hints_side)
# print(random.sample(range(8),k=5))
