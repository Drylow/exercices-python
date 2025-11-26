bac = float(input("Entrez votre note au baccalauréat : "))


if bac < 10:
    print("Note insuffisante, bac non obtenu.")
elif 10 <= bac < 12:
    print("Bac obtenu sans mention.")
elif 12 <= bac < 14:
    print("Bac obtenu avec mention assez bien.")
elif 14 <= bac < 16:
    print("Bac obtenu avec mention bien.")
elif 16 <= bac <= 18:
    print("Bac obtenu avec mention très bien.")
elif 18 < bac <= 20:
    print("Bac obtenu avec les félicitations du jury.")
else:
    print("Note invalide, veuillez entrer une note entre 0 et 20.")