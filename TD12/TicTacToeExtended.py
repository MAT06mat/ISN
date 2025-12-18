SIZE = (7, 5)
ALIGN = 3

P = {0: "⬝", 1: "O", 2: "X"}

grid = [[0 for _ in range(SIZE[0])] for _ in range(SIZE[1])]


def display_grid(grid: list[list[int]]):
    for row in grid[::-1]:
        print(*[P[p] for p in row])


def choose_coords():
    while True:
        text = input("Choisissez un x et un y : ")
        if text == "":
            return None
        try:
            x, y = text.split(",")
            x, y = int(x), int(y)
            if grid[y][x] != 0:
                raise Exception("Non autorisé")
            return x, y
        except Exception as e:
            print("Mauvaise entrée :", e)


def is_same(l: list):
    return l.count(l[0]) == len(l)


def check_line(line: list):
    for i in range(len(line) - ALIGN + 1):
        l = [line[j] for j in range(i, i + ALIGN)]
        if is_same(l) and l[0] != 0:
            return True


def is_game_over(grid):
    # Row - check
    for row in grid:
        if check_line(row):
            return True

    # Cols | check
    for c in range(SIZE[0]):
        col = [grid[r][c] for r in range(SIZE[1])]
        if check_line(col):
            return True

    # Diag / check
    start_diag = []
    for i in range(SIZE[0] - ALIGN + 1):
        start_diag.append((i, 0))
    for i in range(1, SIZE[1] - ALIGN + 1):
        start_diag.append((0, i))
    for x, y in start_diag:
        diag = [grid[y + t][x + t] for t in range(min(SIZE[0] - x, SIZE[1] - y))]
        if check_line(diag):
            return True

    # Diag \ check
    start_diag = []
    for i in range(SIZE[0] - ALIGN + 1):
        start_diag.append((SIZE[0] - i - 1, 0))
    for i in range(1, SIZE[1] - ALIGN + 1):
        start_diag.append((SIZE[0] - 1, i))
    for x, y in start_diag:
        diag = [grid[y + t][x - t] for t in range(min(x + 1, SIZE[1] - y))]
        if check_line(diag):
            return True


print("\n" * 5)
print("=======================")
print("      TIC TAC TOE      ")
print("=======================")


player = 1
while True:
    print("\nAu tour de", P[player], "de jouer :")
    display_grid(grid)
    x, y = choose_coords()
    grid[y][x] = player
    print()
    if is_game_over(grid):
        print("Partie terminée")
        display_grid(grid)
        print("Le gagnant est :", P[player])
        break
    player = {1: 2, 2: 1}[player]
