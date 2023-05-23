"""
Le terminal du launcher de Fastattack sert à debug/lancer des fonctions sans passer par l'UID
Il n'utilise aucun autre fichier .py pour éviter les erreurs liées aux autres fichiers
"""
import os

var_maint = True


def launch():
    """Lance l'interface utilisateur du Terminal dans la console de l'app
    """
    global var_maint
    var_maint = True
    print("Terminal du launcher de Fastattack")
    print("WARNING: Les commandes exécutées depuis ce terminal peuvent endommager votre application: n'exéctutez pas de commandes sans connaissance de leurs effets")
    while var_maint:
        com = input(">>>")
        com = com.split()
        commande(com)
    print("Fermeture du terminal")


def commande(com: list, hide=False):
    """Exécute une commande de la console

    :param com: Commande à exécuter (liste contenant chaque paramètre séparément des autres)
    :param hide: True s'il faut chacher les infos (ne cache pas les erreurs) à l'utilisateur, False si hide n'est pas modifié
    """
    global var_maint
    if com[0] == "quit":
        var_maint = False
    elif com[0] == "reset":
        if len(com) > 1:
            if len(com) <= 2:
                if com[1] == "jeux":
                    with open("jeux.txt", "r") as b:
                        for ligne in b.readlines():
                            nom = ""
                            if "*" in ligne:
                                for lettre in ligne:
                                    if lettre != "*":
                                        nom += lettre
                                    else:
                                        break
                                try:
                                    os.remove(rf"fichiers\icones\{nom}.png")
                                except:
                                    print(f"ERROR: Suppression de l'icone de {nom} impossible")
                                else:
                                    info(f"Icone de {nom} supprimé", hide)
                            else:
                                info("Ligne sans *", hide)
                    for raccourci in os.listdir(r"fichiers\jeux url"):
                        try:
                            os.remove(rf"fichiers\jeux url\{raccourci}")
                        except:
                            print(f"ERROR: Suppression du raccourci de {raccourci}")
                        else:
                            raccourci = raccourci.removesuffix(".url")
                            info(f"Raccourci de {raccourci} supprimé", hide)
                    with open("jeux.txt", "w") as b:
                        b.write("")
                    info("Reset du fichier jeux.txt", hide)
                    info("Redémarrage du launcher conseillé", hide)
                elif com[1] == "bonus":
                    with open("bonus.txt", "r") as b:
                        for ligne in b.readlines():
                            nom = ""
                            if "*" in ligne:
                                for lettre in ligne:
                                    if lettre != "*":
                                        nom += lettre
                                    else:
                                        break
                                try:
                                    os.remove(rf"fichiers\icones\{nom}.png")
                                except:
                                    print(f"ERROR: Suppression de l'icone de {nom} impossible")
                                else:
                                    info(f"Icone de {nom} supprimé", hide)
                            else:
                                info("Ligne sans *", hide)
                    with open("bonus.txt", "w") as b:
                        b.write("")
                    info("Reset du fichier bonus.txt", hide)
                    info("Redémarrage du launcher conseillé", hide)
                elif com[1] == "all":
                    for item in os.listdir(r"fichiers\jeux url"):
                        os.remove(rf"fichiers\jeux url\{item}")
                        info(f"Raccourci url {item} supprimé", hide)
                    for item in os.listdir(r"fichiers\icones"):
                        os.remove(rf"fichiers\icones\{item}")
                        info(f"Icone {item} supprimée", hide)
                    with open("jeux.txt", "w") as b:
                        b.write("")
                    info("Reset du fichier jeux.txt", hide)
                    with open("bonus.txt", "w") as b:
                        b.write("")
                    info("Reset du fichier bonus.txt", hide)
                    info("Redémarrage du launcher conseillé", hide)
                else:
                    print("ERROR: Argument pour la commande reset inconnu")
            else:
                print("ERROR: Trop d'arguments entrés pour la commande reset")
        else:
            print("ERROR: Pas d'argument entré pour la commande reset")
    elif com[0] == "delete":
        if len(com) > 1:
            if len(com) > 3:
                num = 0
                for argument in com:
                    if num > 2:
                        com[2] += f" {argument}"
                    num += 1
            if com[1] == "jeux":
                with open("jeux.txt", "r") as b:
                    lignes = b.readlines()
                nombre = 0
                trouve = False
                for item in lignes:
                    if item.startswith(com[2]):
                        trouve = True
                        break
                    else:
                        nombre += 1
                if trouve:
                    lignes.pop(nombre)
                    with open("jeux.txt", "w") as b:
                        b.writelines(lignes)
                    info(f"Jeu {com[2]} supprimé du launcher", hide)
                else:
                    info("Objet introuvable", hide)
            elif com[1] == "bonus":
                with open("bonus.txt", "r") as b:
                    lignes = b.readlines()
                nombre = 0
                trouve = False
                for item in lignes:
                    if item.startswith(com[2]):
                        trouve = True
                        break
                    else:
                        nombre += 1
                if trouve:
                    lignes.pop(nombre)
                    with open("bonus.txt", "w") as b:
                        b.writelines(lignes)
                    info(f"Bonus {com[2]} supprimé du launcher", hide)
                else:
                    info("Objet introuvable", hide)
            elif com[1] == "icone":
                icones = os.listdir(r"fichiers\icones")
                if f"{com[2]}.png" in icones:
                    try:
                        os.remove(rf"fichiers\icones\{com[2]}.png")
                    except:
                        info("La suppression de l'icone a échoué", hide)
                    else:
                        info("Icone supprimée", hide)
                else:
                    info(f"Icone de {com[2]} introuvable", hide)
            elif com[1] == "raccourci":
                raccourcis = os.listdir(r"fichiers\jeux url")
                if f"{com[2]}.url" in raccourcis:
                    try:
                        os.remove(rf"fichiers\jeux url\{com[2]}.url")
                    except:
                        info("La suppression du raccourci a échoué", hide)
                    else:
                        info("Raccourci supprimé", hide)
                else:
                    info(f"Raccourci de {com[2]} introuvable", hide)
            else:
                print("ERROR: Argument de la commande delete inconnu")
        else:
            print("ERROR: Pas d'argument entré pour la commande delete")
    elif com[0] == "show":
        if len(com) > 1:
            if len(com) <= 2:
                if com[1] == "jeux":
                    with open("jeux.txt", 'r') as b:
                        lignes = b.readlines()
                    if lignes == []:
                        print("Fichier vide")
                    else:
                        print("---Début du fichier---")
                        for ligne in lignes:
                            print(ligne)
                        print("---Fin du fichier---")
                elif com[1] == "bonus":
                    with open("bonus.txt", 'r') as b:
                        lignes = b.readlines()
                    if lignes == []:
                        print("Fichier vide")
                    else:
                        print("---Début du fichier---")
                        for ligne in lignes:
                            print(ligne)
                        print("---Fin du fichier---")
                elif com[1] == "infos":
                    with open("Infos.txt", 'r') as b:
                        lignes = b.readlines()
                    if lignes == []:
                        print("Fichier vide")
                    else:
                        print("---Début du fichier---")
                        for ligne in lignes:
                            print(ligne)
                        print("---Fin du fichier---")
                elif com[1] == "commandes":
                    with open("Commandes.txt", 'r') as b:
                        lignes = b.readlines()
                    if lignes == []:
                        print("Fichier vide")
                    else:
                        print("---Début du fichier---")
                        for ligne in lignes:
                            print(ligne)
                        print("---Fin du fichier---")
                else:
                    print("ERROR: 1er argument de la commande show inconnu")
            else:
                print("ERROR: Trop d'arguments entrés pour la commande show")
        else:
            print("ERROR: Pas d'argument entré pour la commande show")
    else:
        print("ERROR: Commande inconnue")


def info(com: str, hide: bool):
    if not hide:
        print(com)
