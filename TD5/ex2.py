"""
2.1
"""

ages = [22, 56, 89, 2, 72, 17, 36]
moy = sum(ages) / len(ages)
# print("Moyenne:", moy)

"""
2.2
"""

ages2 = [12, 56, 87, 101]

bon_ordre = ages == sorted(ages)
bon_ordre2 = ages2 == sorted(ages2)
# print("Bon ordre:", bon_ordre)
# print("Bon ordre 2:", bon_ordre2)


"""
2.3
"""

livre = [
    "Bonjour Arthur",
    "je suis le roi",
    "et toi tu n'es rien",
    "je suis le dieu de ce monde.",
    "Oui, peut-être...",
    "Mais moi, je suis Arthur le brave !",
    "Et je vais t'anéantir !",
]

mot = "Arthur"
pages = []

for page in range(len(livre)):
    if mot in livre[page].split():
        pages.append(str(page + 1))

# if len(pages) == 0:
#     print(f"Le mot '{mot}' n'est pas dans ce livre...")
# elif len(pages) == 1:
#     print(f"Le mot '{mot}' à été trouvé à la page {pages[0]}")
# else:
#     print(f"Le mot '{mot}' à été trouvé aux pages {", ".join(pages)}")
