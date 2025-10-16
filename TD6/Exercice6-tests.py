from Exercice6 import trier

assert trier([4, 2, 1]) == [1, 2, 4]
assert trier([]) == []
assert trier([3]) == [3]
assert trier([-5, 12, 9999, -45, 784, 0]) == [-45, -5, 0, 12, 784, 9999]

print("Tout fonctionne")
