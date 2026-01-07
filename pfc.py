import random
liste = ["pierre","feuille","ciseaux"]
somme_user = 0
somme_bot = 0
resultat= ""
for i in range(10):
    element = random.choice(liste)
    choix_user = input("choisissez entre pierre, feuille, ciseaux:")
    if choix_user == element:
        resultat="égalité"
        print("égalité")
    elif choix_user == "feuille" and element == "ciseaux":
        resultat="défaite"
        print("défaite")
    elif choix_user == "ciseaux" and element == "pierre":
        resultat="défaite"
        print("défaite")
    elif choix_user == "pierre" and element == "feuille":
        resultat="défaite"
        print("défaite")


    elif choix_user == "ciseaux" and element == "feuille":
        resultat="victoire"
        print("victoire")
    elif choix_user == "pierre" and element == "ciseaux":
        resultat="victoire"
        print("victoire")
    elif choix_user == "feuille" and element == "pierre":
        resultat="victoire"
        print("victoire")

    if resultat == "victoire":
        somme_user+=1
    elif resultat == "défaite":
        somme_bot+=1
    print(f"score du bot:{somme_bot}")
    print(f"ton score:{somme_user}")
    print(element)

