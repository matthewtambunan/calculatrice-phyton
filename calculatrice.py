print("=== CALCULATRICE DE MATTHEW ===")

while True:
    print("\n1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Quitter")

    choix = input("Choisissez une opération (1-5) : ")

    if choix == "5":
        print("Merci d'avoir utilisé la calculatrice !")
        break

    if choix not in ["1", "2", "3", "4"]:
        print("Choix invalide. Réessayez.")
        continue

    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))

    if choix == "1":
        resultat = nombre1 + nombre2
    elif choix == "2":
        resultat = nombre1 - nombre2
    elif choix == "3":
        resultat = nombre1 * nombre2
    elif choix == "4":
        if nombre2 == 0:
            print("Erreur : division par zéro impossible.")
            continue
        resultat = nombre1 / nombre2

    print("Résultat :", resultat)

print("Programme terminé.")
