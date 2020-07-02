coordinates = [
    (1, 3), (2, 3), (3, 3),
    (1, 2), (2, 2), (3, 2),
    (1, 1), (2, 1), (3, 1)
]
cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
game_count = 9
player1x = "X"
player2o = "O"
your_turn = True
win_player1 = ("X", "X", "X")  # To check if in possible winning lines
win_player2 = ("O", "O", "O")


def get_winning_line():
    global cells, win_player1, win_player2, game_count
    indexes = [
        [cells[0], cells[1], cells[2]],
        [cells[3], cells[4], cells[5]],
        [cells[6], cells[7], cells[8]]
    ]
    lines = [
        tuple(line) for line in indexes
    ]  # gets all the rows
    for i in range(3):
        tem_line = [
            line[i] for line in indexes
        ]  # gets the columns one by one
        lines.append(tuple(tem_line))
    tem_line = []
    tem_line2 = []
    index = -1
    for i in range(3):
        tem_line.append(indexes[i][i])
        tem_line2.append(indexes[i][index])
        index -= 1
    lines.extend([tuple(tem_line), tuple(tem_line2)])  # gets the diagonals
    if win_player1 in set(lines) and win_player2 not in set(lines):
        print("X wins")
        game_count = 0
    elif win_player2 in set(lines) and win_player1 not in set(lines):
        print("O wins")
        game_count = 0
    else:
        if game_count == 0:
            print("Draw")


def assign_coordinates():  # this function creates a unique data structure with coordinates associated
    """the function associates the coordinates with the cells"""
    global coordinates, cells  # with cells. [ [ [coordinates], cell ] ] a nested list
    assign_coord = []
    coord = 0
    for item in cells:
        assign_coord.append([(coordinates[coord]), item])
        coord += 1
    return assign_coord


def create_field():
    """Creates the games field"""
    global cells
    print(
        f"""
    ---------
    | {cells[0]} {cells[1]} {cells[2]} |
    | {cells[3]} {cells[4]} {cells[5]} |
    | {cells[6]} {cells[7]} {cells[8]} |
    ---------
    """
    )


def check_and_fill_space_with_move(move, player):  # move is tuple
    global cells, game_count, your_turn
    possible_moves = assign_coordinates()
    for item in possible_moves:  # item structure ((coord), cell)
        index = possible_moves.index(item)
        if move in item:
            if item[1] == " ":
                possible_moves[index][1] = player
                game_count -= 1
                cells[index] = player
                create_field()
            else:
                print("This cell is occupied! Choose another one!")


def validate_move(move):
    global coordinates
    move = move.split()
    try:
        coord = [int(i) for i in move]
        if tuple(coord) in coordinates:
            return tuple(coord)
        else:
            print("Coordinates should be from 1 to 3!")
    except ValueError:
        print("You should enter numbers!")


def play_game():
    global your_turn, game_count
    create_field()
    while game_count > 0:
        if game_count > 0 and game_count % 2 != 0:
            player1 = input("Enter the coordinates: ")
            val_move = validate_move(player1)
            if val_move is not None:
                check_and_fill_space_with_move(val_move, player1x)
                get_winning_line()
        if game_count > 0 and game_count % 2 == 0:
            player2 = input("Enter the coordinates: ")
            val_move = validate_move(player2)
            if val_move is not None:
                check_and_fill_space_with_move(val_move, player2o)
                get_winning_line()


play_game()
