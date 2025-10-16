from random import randint
from math import dist

n = 5
lapin = (randint(0, n - 1), randint(0, n - 1))


def prairie(n):
    for i in range(n):
        print(2 * n * "░")


while True:
    print("Cherchez le lapin !")
    x = int(input("Coord X: "))
    y = int(input("Coord Y: "))
    prairie(n)

    if (x, y) == lapin:
        break
    print(f"Vous n'avez pas trouvé le lapin... il est a {dist((x, y), lapin)}m de vous")

print("Vous avez trouvé le lapin !")
print(f"Il était bien en {lapin}")
