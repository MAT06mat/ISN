liste = [0, 0, 0, 2, 1, 3, 0, 1]

i = 0
while i < len(liste) and liste[i] == 0:
    i += 1

print(f"i: {i}, liste[{i}]: {liste[i]}")
