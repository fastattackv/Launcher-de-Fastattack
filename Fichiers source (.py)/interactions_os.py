import os
import win32com.client


def lancer(jeu: str, bonus: list):
    """
    lance le jeu et le bonus indiqués
    :param jeu: nom du jeu à lancer
    :param bonus: liste contenant les noms des bonus à lancer
    :return: rien
    """
    if jeu != "PaS_dE_Jeu_A_LANcER":
        try:
            os.startfile(dic_jeux[jeu])
        except:
            print(f"ERREUR: Le jeu {jeu} n'a pas été trouvé")
        for item in bonus:
            try:
                os.startfile(dic_bonus[item])
            except:
                print(f"ERREUR: Le bonus {item} n'a pas été trouvé")
    else:
        for item in bonus:
            try:
                os.startfile(dic_bonus[item])
            except:
                print(f"ERREUR: Le bonus {item} n'a pas été trouvé")


def add_jeu(jeu: str, chemin_jeu: str):
    """
    ajoute le jeu associé à son path dans le dictionnaire des jeux (et dans la liste du dictionnaire)
    :param jeu: jeu à ajouter
    :param chemin_jeu: chemin jeu à ajouter
    :return: rien
    """
    if jeu != "liste_jeux":
        if jeu not in dic_jeux:
            try:
                dic_jeux[jeu] = chemin_jeu
                liste_jeux = dic_jeux["liste_jeux"]
                liste_jeux.append(jeu)
                liste_jeux.sort()
                dic_jeux["liste_jeux"] = liste_jeux
                dump_txt(dic_jeux, "jeux")
            except:
                print(f"EREUR: L'ajout du jeu {jeu} à la liste des jeux a échoué")
        else:
            print("ERREUR: Jeu déjà enregistré")
    else:
        print("ERREUR: Le nom de jeu liste_jeux est impossible")


def add_bonus(bonus: str, chemin_bonus: str):
    """
    ajoute le bonus associé à son path dans le dictionnaire des bonus (et dans la liste du dictionnaire)
    :param chemin_bonus: bonus à ajouter
    :param bonus: chemin bonus à ajouter
    :return: rien
    """
    if bonus != "liste_bonus":
        if bonus not in dic_bonus:
            try:
                dic_bonus[bonus] = chemin_bonus
                liste_bonus = dic_bonus["liste_bonus"]
                liste_bonus.append(bonus)
                liste_bonus.sort()
                dic_bonus["liste_bonus"] = liste_bonus
                dump_txt(dic_bonus, "bonus")
            except:
                print(f"EREUR: l'ajout du bonus {bonus} à la liste des bonus a échoué")
        else:
            print("ERREUR: Bonus déjà enregistré")
    else:
        print("ERREUR: Le nom de bonus liste_bonus est impossible")


def check() -> list:
    """
    Vérifie si les jeux, bonus et lauchers enregistrés existent toujours
    :return: une liste contenant 2 listes qui contiennent les items qui n'existent plus, retourne 3 liste vide si tout va bien
    """
    to_return1 = []
    to_return2 = []
    for item in dic_jeux:
        if item != "liste_jeux":
            if not os.path.isfile(dic_jeux[item]):
                to_return1.append(item)
    for item in dic_bonus:
        if item != "liste_bonus":
            if not os.path.isfile(dic_bonus[item]):
                to_return2.append(item)
    return [to_return1, to_return2]


def modifier(type_item: str, item: str, chemin_item: str):
    """
    modifie un item enregistré dans le launcher
    :param type_item: type de l'item à modifier : jeux/bonus
    :param item: nom de l'item à modifer
    :param chemin_item: nouveau chemin de l'item à modifier
    :return: rien
    """
    if type_item == "jeux":
        if item in dic_jeux:
            exist = True
            if exist:
                if os.path.isfile(chemin_item):
                    dic_jeux[item] = chemin_item
                    dump_txt(dic_jeux, "jeux")
                else:
                    print("ERREUR: Le fichier indiqué n'existe pas (fonction modifier->interactions os)")
    elif type_item == "bonus":
        if item in dic_bonus:
            exist = True
            if exist:
                if os.path.isfile(chemin_item):
                    dic_bonus[item] = chemin_item
                    dump_txt(dic_bonus, "bonus")
                else:
                    print("ERREUR: Le fichier indiqué n'existe pas (fonction modifier->interactions os)")
    else:
        print("ERREUR: type_item inconnu (fonction modifier->interactions os)")


def supprimer(type_item: str, item: str, introuvable="N"):
    """
    supprime le jeu/bonus indiqué + supprime l'icone + le raccourci si besoin
    :param type_item: type de l'item à supprimer ("jeux" ou "bonus")
    :param item: nom de l'item à supprimer enregistré dans le launcher
    :return: rien
    """
    if type_item == "jeux":
        if item in dic_jeux:
            dic_jeux["liste_jeux"].remove(item)
            del dic_jeux[item]
            dump_txt(dic_jeux, "jeux")
            try:
                os.remove(rf"fichiers\Icones\{item}.png")
            except:
                print("ERREUR: icone introuvable (fonction supprimer->interactions os)")
            if introuvable == "N" and item.endswith(".url"):
                try:
                    os.remove(rf"fichiers\jeux url\{item}.url")
                except:
                        print("ERREUR: raccourci introuvable (fonction supprimer->interactions os)")
        else:
            print(f"ERREUR: {item} est introuvable (fonction supprimer->interactions os)")
    elif type_item == "bonus":
        if item in dic_bonus:
            dic_bonus["liste_bonus"].remove(item)
            del dic_bonus[item]
            dump_txt(dic_bonus, "bonus")
            try:
                os.remove(rf"fichiers\Icones\{item}.png")
            except:
                print("ERREUR: icone introuvable (fonction supprimer->interactions os)")
        else:
            print(f"ERREUR: {item} est introuvable (fonction supprimer->interactions os)")
    else:
        print("ERREUR: type_item inconnu (fonction supprimer->interactions os)")


def get_exe_from_lnk(chemin_lnk: str) -> str:
    """
    renvoie le chemin d'un .exe à partir d'un .lnk
    :param chemin_lnk: chemin du raccourci (.lnk)
    :return: path du .exe
    """
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(chemin_lnk)
    return shortcut.Targetpath


def reset_vars(a_reset: str):
    """
    reset les variables des jeux/bonus enregistrés
    :param a_reset: jeux pour reset les jeux/bonus pour reset les bonus/tout pour reset les jeux et bonus
    :return: rien
    """
    global dic_jeux, dic_bonus
    if a_reset == "jeux":
        for item in dic_jeux["liste_jeux"]:
            try:
                os.remove(rf"fichiers\icones\{item}.png")
            except:
                print("ERROR: icone introuvable (fonction reset->interactions os)")
        dic_jeux = {'liste_jeux': []}
        dump_txt(dic_jeux, "jeux")
    elif a_reset == "bonus":
        for item in dic_bonus["liste_bonus"]:
            try:
                os.remove(rf"fichiers\icones\{item}.png")
            except:
                print("ERROR: icone introuvable (fonction reset->interactions os)")
        dic_bonus = {'liste_bonus': []}
        dump_txt(dic_bonus, "bonus")
    elif a_reset == "tout":
        reset_vars("jeux")
        reset_vars("bonus")


def dump_txt(a_dump: dict, fichier: str):
    """
    Dump le dictionnaire indiqué, ligne par ligne dans le fichier .txt indiqué (jeux ou bonus)
    :param a_dump: dictionnaire à dump dans le fichier .txt
    :param fichier: fichier dans lequel dump le dictionnaire (jeux ou bonus)
    :return: rien
    """
    str_a_dump = ""
    if fichier == "jeux" and "liste_jeux" in a_dump:
        for item in a_dump["liste_jeux"]:
            chemin_a_dump = a_dump[item]
            str_a_dump += f"{item}*{chemin_a_dump}\n"
        str_a_dump.removesuffix("\n")
        with open("jeux.txt", "w") as b:
            b.write(str_a_dump)
    elif fichier == "bonus" and "liste_bonus" in a_dump:
        for item in a_dump["liste_bonus"]:
            chemin_a_dump = a_dump[item]
            str_a_dump += f"{item}*{chemin_a_dump}\n"
        str_a_dump.removesuffix("\n")
        with open("bonus.txt", "w") as b:
            b.write(str_a_dump)
    else:
        print("ERROR: la variable fichier n'est pas une option possible (jeux ou bonus) (fonction dump_txt->interactions_os)")


# load les varaiables des jeux enregistrés dans le launcher
with open("jeux.txt", "r") as b:
    dic_jeux = {"liste_jeux": []}
    for line in b.readlines():
        if "\n" in line:
            line = line.replace("\n", "")
        if line != "":
            if "*" in line:
                etoile_p = False
                nom = ""
                chemin = ""
                for lettre in line:
                    if etoile_p:
                        chemin += lettre
                    elif lettre == "*":
                        etoile_p = True
                    else:
                        nom += lettre
                if nom != "":
                    if os.path.isfile(chemin):
                        if nom not in dic_jeux:
                            dic_jeux["liste_jeux"].append(nom)
                            dic_jeux[nom] = chemin
                        else:
                            print(f"Warning: Le jeu {nom} est défini deux fois, seule la première définition sera utilisée")
                    else:
                        print(f"ERROR: Le chemin du fichier à la ligne [{line}] n'existe pas (fichier jeux.txt)")
                else:
                    print(f"ERROR: Le nom du fichier à la ligne [{line}] est impossible (fichier jeux.txt)")
            else:
                print(f"ERROR: Lecture de la ligne [{line}] impossible: la ligne ne contient pas * (fichier jeux.txt)")


with open("bonus.txt", "r") as b:
    dic_bonus = {"liste_bonus": []}
    for line in b.readlines():
        if "\n" in line:
            line = line.replace("\n", "")
        if line != "":
            if "*" in line:
                etoile_p = False
                nom = ""
                chemin = ""
                for lettre in line:
                    if etoile_p:
                        chemin += lettre
                    elif lettre == "*":
                        etoile_p = True
                    else:
                        nom += lettre
                if nom != "":
                    if os.path.isfile(chemin):
                        if nom not in dic_bonus:
                            dic_bonus["liste_bonus"].append(nom)
                            dic_bonus[nom] = chemin
                        else:
                            print(f"Warning: Le bonus {nom} est défini deux fois, seule la première définition sera utilisée")
                    else:
                        print(f"ERROR: Le chemin du fichier à la ligne [{line}] n'existe pas (fichier bonus.txt)")
                else:
                    print(f"ERROR: Le nom du fichier à la ligne [{line}] est impossible (fichier bonus.txt)")
            else:
                print(f"ERROR: Lecture de la ligne [{line}] impossible: la ligne ne contient pas * (fichier bonus.txt)")
