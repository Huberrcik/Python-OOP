def get_number(a, b, text):
    while True:
        try:
            data = input(f"{text} (zakres od {a} do {b}: )")
            n = int(data)
            if a <= n <= b:  # n>=a and n<=b:
                return n
            else:
                print(f"Cos ci sie jeblo chyba kolezko, liczba {n} jest spoza zakresu") 
        except ValueError:
            print(f"{data} - to nie jest liczba")


def lay_mines(number_of_mines, rows, columns):
    from random import randrange
    mines = set()
    
    while len(mines) < number_of_mines:
        i = randrange(rows)
        j = randrange(columns)
        mines.add((i, j))
    
    return mines


def number_of_neighbouring_mines(field, mines):
    i = field[0]
    j = field[1]
    count = 0
    for x in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if x in mines:
            count += 1
    return count


def create_board(rows, columns, mines, mine='*'):
    board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if (i, j) in mines:
                row.append(mine)
            else:
                row.append(number_of_neighbouring_mines((i, j), mines))
        board.append(row)

    return board


def reveal_fields(field, board, rows, columns, printable_fields):
    i = field[0]
    j = field[1]

    if not (0 <= i < rows and 0 <= j < columns) or (i, j) in printable_fields:
        return

    printable_fields.add(field)
    if board[i][j] != 0:
        return
    else:
        for x in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                  (i + 1, j + 1)]:
            reveal_fields(x, board, rows, columns, printable_fields)


def print_board(board, rows, columns, printable_fields, print_all = False):
    print(" "*4, end ="")
    for i in range(columns):
        print(f"{i:^3}", end = " ")
    print()
    for i in range(rows):
        print(f"{i:<3}|", end = "")

        for j in range(columns):
            if(i, j) in printable_fields or print_all:
                print(f" {board[i][j]} |", end = "")
            else:
                print(f" # |", end = "")

        print()


r = 10
c = 10
n = 10
s = lay_mines(n, r, c)
board = create_board(r, c, s)

printable_fields = set()


print_board(board, r, c, printable_fields)
while len(printable_fields) < r * c - n:
    i = get_number(0, r - 1, "podaj nr wiersza")
    j = get_number(0, c - 1, "podaj nr kolumny")
    if (i, j) in s:
        print("trafiles mine")
        break
    else:
        reveal_fields((i, j), board, r, c, printable_fields)

    print_board(board, r, c, printable_fields)
else:
    print("Wygrales!")