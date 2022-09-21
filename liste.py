import sys
LISTE = []

MENU = """Choisissez parmi les 5 options suivante :
1: Ajouter un element a la liste
2: Retirer un elemet de la liste
3:Afficher la liste
4: Vider la liste
5: Quitter
---> Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide")
    
    if user_choice == "1":   # Ajouter un élément
        item = input("Enter le nom de l'élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté à la Liste. ")
    elif user_choice == "2": #Retirer un élément    
        item = input("Entrer le nom de l'élément à retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la Liste. ")
        else:
            print(f"L'élément {item} n'est pas dans la Liste.")    
    elif user_choice == "3":   #Afficher la liste
        if LISTE:
            print("Voici le contenu de la Liste : ")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste es vide")       
    elif user_choice == "4":   # Vider la liste
        LISTE.clear()
        print("La Liste a été vidé de son contenue.")
    elif user_choice == "5":   #Quitter
        print("A Bientot   !")
        sys.exit()
    print("-" * 50)    