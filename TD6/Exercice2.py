"""
2.1
"""

ma_liste = [3, 4, 12, 7, 14, 8]

print(ma_liste[1:-1])

# Sinon (si on est c**):
nouvelle_liste_beaucoup_plus_nulle = []
for i in range(len(ma_liste)):
    if i != 0 and i != len(ma_liste) - 1:
        nouvelle_liste_beaucoup_plus_nulle.append(ma_liste[i])
print(nouvelle_liste_beaucoup_plus_nulle)
