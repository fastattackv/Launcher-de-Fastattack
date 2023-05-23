# vérification des fichiers et execution des commandes de lancement
import init

# autres importations:
import interactions_os as IntOS
import get_icons as getI
import Terminal

import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import os
import shutil
import random


# définition des variables globales
type_selectionne = None
liste_affiche = []
dic_selectionne = {"liste_jeux_selectionne": [], "liste_bonus_selectionne": []}
page_active = 1


# variables d'affichage d'images
var_aff_img1 = None
var_aff_img2 = None
var_aff_img3 = None
var_aff_img4 = None
var_aff_img5 = None
var_aff_img6 = None
var_aff_img7 = None
var_aff_img8 = None
var_aff_img9 = None
var_aff_img10 = None
var_aff_img11 = None
var_aff_img12 = None
var_aff_img13 = None
var_aff_img14 = None
var_aff_img15 = None
var_aff_img16 = None
liste_var_aff_images = [var_aff_img1, var_aff_img2, var_aff_img3, var_aff_img4, var_aff_img5, var_aff_img6,
                        var_aff_img7, var_aff_img8, var_aff_img9, var_aff_img10, var_aff_img11, var_aff_img12,
                        var_aff_img13, var_aff_img14, var_aff_img15, var_aff_img16]


# fonctions de select des boutons tkinter
def select_1():
    select_glo(1)
def select_2():
    select_glo(2)
def select_3():
    select_glo(3)
def select_4():
    select_glo(4)
def select_5():
    select_glo(5)
def select_6():
    select_glo(6)
def select_7():
    select_glo(7)
def select_8():
    select_glo(8)
def select_9():
    select_glo(9)
def select_10():
    select_glo(10)
def select_11():
    select_glo(11)
def select_12():
    select_glo(12)
def select_13():
    select_glo(13)
def select_14():
    select_glo(14)
def select_15():
    select_glo(15)
def select_16():
    select_glo(16)


def select_glo(num: int):
    num -= 1
    if liste_affiche[num] in dic_selectionne[type_selectionne]:
        dic_selectionne[type_selectionne].remove(liste_affiche[num])
    else:
        dic_selectionne[type_selectionne].append(liste_affiche[num])
    up_select()


def up_select():
    texte_jeu = "Jeux selectionnés: "
    for jeu in dic_selectionne["liste_jeux_selectionne"]:
        texte_jeu += f"{jeu}, "
    label_jeu = tk.Label(fen, text=texte_jeu)
    label_jeu.grid(column=1, row=11, sticky="nswe", padx=5, pady=5, columnspan=2)
    texte_bonus = "Bonus selectionnés: "
    for bonus in dic_selectionne["liste_bonus_selectionne"]:
        texte_bonus += f"{bonus}, "
    label_bonus = tk.Label(fen, text=texte_bonus)
    label_bonus.grid(column=3, row=11, sticky="nswe", padx=5, pady=5, columnspan=2)


# Fonctions d'affichage des jeux et bonus
def show_jeux(page=1):
    cacher()
    global liste_affiche, type_selectionne, page_active
    page_active = page
    liste_affiche = []
    type_selectionne = "liste_jeux_selectionne"
    dic_jeux = IntOS.dic_jeux
    liste_jeux = dic_jeux["liste_jeux"]
    liste_fonctions = [select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9,
                       select_10, select_11, select_12, select_13, select_14, select_15, select_16]
    num_max_jeu = len(liste_jeux)
    num_jeu = 0
    row = 1
    column = 6
    num_fonction = 0
    num_img = 0
    compteur_cols = 0
    check_boutons = IntOS.check()[0]
    etat = "normal"
    if num_max_jeu > page * 16:
        num_max_jeu = 16
    elif num_max_jeu == 0:
        label_1 = tk.Label(fen, text="Pas de jeux enregistrés dans le launcher")
        label_1.grid(column=1, row=2)
    else:
        num_max_jeu = 16 - (page * 16 - num_max_jeu)
        if num_max_jeu < 0:
            num_max_jeu = 0
    if len(liste_jeux) > 16:
        debut = (page - 1) * 16
        liste_a_aff = []
        for x in range(num_max_jeu):
            liste_a_aff.append(liste_jeux[debut])
            debut += 1
    else:
        liste_a_aff = liste_jeux
    for x in range(num_max_jeu):
        if column > 3:
            column = 1
            row += 1
        else:
            column += 1
        if compteur_cols == 4:
            row += 3
        if compteur_cols <= 3:
            rowspan = 4
        else:
            rowspan = 1
        if liste_a_aff[num_jeu] in check_boutons:
            etat = "disabled"
        if os.path.isfile(rf"fichiers\Icones\{liste_a_aff[num_jeu]}.png"):
            liste_var_aff_images[num_img] = tk.PhotoImage(file=rf"fichiers\Icones\{liste_a_aff[num_jeu]}.png")
            bouton_jeu = tk.Button(fen, image=liste_var_aff_images[num_img], text=liste_a_aff[num_jeu], command=liste_fonctions[num_fonction], compound="top", state=etat)
        else:
            bouton_jeu = tk.Button(fen, text=liste_a_aff[num_jeu], command=liste_fonctions[num_fonction], state=etat)
        bouton_jeu.grid(column=column, row=row, sticky="nswe", padx=5, pady=5, rowspan=rowspan)
        num_fonction += 1
        num_img += 1
        liste_affiche.append(liste_a_aff[num_jeu])
        num_jeu += 1
        compteur_cols += 1
        etat = "normal"


def show_bonus(page=1):
    cacher()
    global liste_affiche, type_selectionne, page_active
    page_active = page
    liste_affiche = []
    type_selectionne = "liste_bonus_selectionne"
    dic_bonus = IntOS.dic_bonus
    liste_bonus = dic_bonus["liste_bonus"]
    liste_fonctions = [select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9,
                       select_10, select_11, select_12, select_13, select_14, select_15, select_16]
    num_max_bonus = len(liste_bonus)
    num_bonus = 0
    row = 1
    column = 6
    num_fonction = 0
    num_img = 0
    compteur_cols = 0
    check_boutons = IntOS.check()[1]
    etat = "normal"
    if num_max_bonus > page * 16:
        num_max_bonus = 16
    elif num_max_bonus == 0:
        label_1 = tk.Label(fen, text="Pas de bonus enregistrés dans le launcher")
        label_1.grid(column=1, row=2)
    else:
        num_max_bonus = 16 - (page * 16 - num_max_bonus)
        if num_max_bonus < 0:
            num_max_bonus = 0
    if len(liste_bonus) > 16:
        debut = (page - 1) * 16
        liste_a_aff = []
        for x in range(num_max_bonus):
            liste_a_aff.append(liste_bonus[debut])
            debut += 1
    else:
        liste_a_aff = liste_bonus
    for x in range(num_max_bonus):
        if column > 3:
            column = 1
            row += 1
        else:
            column += 1
        if compteur_cols == 4:
            row += 3
        if compteur_cols <= 3:
            rowspan = 4
        else:
            rowspan = 1
        if liste_a_aff[num_bonus] in check_boutons:
            etat = "disabled"
        if os.path.isfile(rf"fichiers\Icones\{liste_a_aff[num_bonus]}.png"):
            liste_var_aff_images[num_img] = tk.PhotoImage(file=rf"fichiers\Icones\{liste_a_aff[num_bonus]}.png")
            bouton_bonus = tk.Button(fen, image=liste_var_aff_images[num_img], text=liste_a_aff[num_bonus], command=liste_fonctions[num_fonction], compound="top", state=etat)
        else:
            bouton_bonus = tk.Button(fen, text=liste_a_aff[num_bonus], command=liste_fonctions[num_fonction], state=etat)
        bouton_bonus.grid(column=column, row=row, sticky="nswe", padx=5, pady=5, rowspan=rowspan)
        num_fonction += 1
        num_img += 1
        liste_affiche.append(liste_a_aff[num_bonus])
        num_bonus += 1
        compteur_cols += 1


def reset():
    global dic_selectionne, type_selectionne, page_active
    dic_selectionne = {"liste_jeux_selectionne": [], "liste_bonus_selectionne": []}
    page_active = 1
    if type_selectionne == "liste_jeux_selectionne":
        show_jeux()
    elif type_selectionne == "liste_bonus_selectionne":
        show_bonus()
    up_select()
    up_page()


def cacher():
    bouton_destroy = tk.Label(fen, text="", borderwidth=0)
    bouton_destroy.grid(column=1, row=2, sticky="nswe", columnspan=4, rowspan=8)


# Fonctions des boutons de contrôle d'affichage
def page_suivante():
    cacher()
    page_a_donner = page_active + 1
    if type_selectionne == "liste_jeux_selectionne":
        show_jeux(page=page_a_donner)
    elif type_selectionne == "liste_bonus_selectionne":
        show_bonus(page=page_a_donner)
    up_page()


def page_precedente():
    page_a_donner = page_active - 1
    if page_a_donner <= 0:
        return
    if type_selectionne == "liste_jeux_selectionne":
        show_jeux(page=page_a_donner)
    elif type_selectionne == "liste_bonus_selectionne":
        show_bonus(page=page_a_donner)
    up_page()


def up_page():
    label_page_a = tk.Label(fen, text=f"Page {page_active}")
    label_page_a.grid(column=0, row=5)


# Fonctions des ajouts
def ajout():
    type_add = simpledialog.askstring("Ajout", "Que voulez vous ajouter ?\rAjouter un jeu [J]\rAjouter un jeu .url [U]\rAjouter plusieurs jeux [M]\rAjouter un bonus [B]")
    if type_add == "J":
        add_jeu()
    elif type_add == "U":
        add_jeu2()
    elif type_add == "M":
        add_jeux_multiples()
    elif type_add == "B":
        add_bonus()


def add_jeu():
    path_jeu = filedialog.askopenfilename(title="Ajout jeu")
    jeu = get_nom_jeu(path_jeu)
    if jeu != "" and path_jeu != "":
        IntOS.add_jeu(jeu, path_jeu)
        rep = getI.get_icone(path_jeu, jeu)
        if rep == "ERROR":
            messagebox.showwarning("Launcher de Fastattack", "L'importation de l'icone a échouée")
        elif rep == "OK":
            reset()
    elif jeu == "" and path_jeu != "":
        messagebox.showerror("Ajout de jeu", "La récupération du nom du fichier a échoué")


def add_jeu2():
    path_jeu = simpledialog.askstring("Launcher de Fastattack", "chemin du jeu/raccourci")
    if path_jeu is not None:
        if path_jeu.startswith('"') and path_jeu.endswith('"'):
            path_jeu = path_jeu.removeprefix('"')
            path_jeu = path_jeu.removesuffix('"')
        jeu = get_nom_jeu(path_jeu)
        if jeu != "":
            if path_jeu.endswith(".url"):
                shutil.copyfile(path_jeu, rf"fichiers\jeux url\{jeu}.url")
                path_jeu = rf"fichiers\jeux url\{jeu}.url"
                IntOS.add_jeu(jeu, path_jeu)
                rep = getI.get_icone(path_jeu, jeu)
                if rep == "ERROR":
                    messagebox.showwarning("Launcher de Fastattack", "L'importation de l'icone a échouée")
                elif rep == "OK":
                    reset()
            else:
                messagebox.showwarning("Launcher de Fastattack", "Le fichier séléctionné n'est pas un raccourci .url")
        elif jeu == "":
            messagebox.showerror("Ajout de jeu", "La récupération du nom du fichier a échoué")


def add_jeux_multiples():
    dossier = filedialog.askdirectory()
    if dossier != "":
        fichiers = os.listdir(dossier)
        liste_ajouts = []
        for item in fichiers:
            path = rf"{dossier}/{item}"
            nom = get_nom_jeu(path)
            if nom != "":
                if item.endswith(".url"):
                    shutil.copyfile(path, rf"fichiers\jeux url\{nom}.url")
                    path_jeu = rf"fichiers\jeux url\{nom}.url"
                    IntOS.add_jeu(nom, path_jeu)
                    rep = getI.get_icone(path_jeu, nom)
                    if rep == "ERROR":
                        messagebox.showerror("Ajout de jeux", f"La récupération de l'icone de {nom} a échoué")
                    liste_ajouts.append(nom)
                elif item.endswith(".lnk"):
                    chemin_exe = IntOS.get_exe_from_lnk(path)
                    IntOS.add_jeu(nom, chemin_exe)
                    rep = getI.get_icone(chemin_exe, nom)
                    if rep == "ERROR":
                        messagebox.showerror("Ajout de jeux", f"La récupération de l'icone de {nom} a échoué")
                    liste_ajouts.append(nom)
                elif item.endswith(".exe"):
                    IntOS.add_jeu(nom, path)
                    rep = getI.get_icone(path, nom)
                    if rep == "ERROR":
                        messagebox.showerror("Ajout de jeux", f"La récupération de l'icone de {nom} a échoué")
                    liste_ajouts.append(nom)
        show_jeux()


def add_bonus():
    path_bonus = filedialog.askopenfilename()
    bonus = get_nom_jeu(path_bonus)
    if bonus != "" and path_bonus != "":
        IntOS.add_bonus(bonus, path_bonus)
        rep = getI.get_icone(path_bonus, bonus)
        if rep == "ERROR":
            messagebox.showwarning("Launcher de Fastattack", "L'importation de l'icone a échouée")
        elif rep == "OK":
            reset()
    elif bonus == "" and path_bonus != "":
        messagebox.showerror("Ajout de bonus", "La récupération du nom du fichier a échoué")


# Fonctions de modifications des jeux/bonus
def supprimer():
    jeux_a_supp = dic_selectionne["liste_jeux_selectionne"]
    bonus_a_supp = dic_selectionne["liste_bonus_selectionne"]
    if jeux_a_supp != []:
        if messagebox.askyesno("Launcher de Fastattack", f"Voulez vous supprimer les jeux {jeux_a_supp}"):
            for item in jeux_a_supp:
                IntOS.supprimer("jeux", item)
                reset()
    if bonus_a_supp != []:
        if messagebox.askyesno("Launcher de Fastattack", f"Voulez vous supprimer les bonus {bonus_a_supp}"):
            for item in bonus_a_supp:
                IntOS.supprimer("bonus", item)
                reset()
    if jeux_a_supp == [] and bonus_a_supp == []:
        if messagebox.askyesno("Launcher de Fastattack", "Pas de jeux/bonus séléctionné\rVoulez-vous en supprimer un par son nom ?"):
            jeu_a_supp = simpledialog.askstring("Launcher de Fastattack", "Entrez le nom du jeu/bonus à supprimer")
            if jeu_a_supp in IntOS.dic_jeux:
                if messagebox.askyesno("Launcher de Fastattack", f"Voulez vous supprimer le jeu {jeu_a_supp}"):
                    IntOS.supprimer("jeux", jeu_a_supp)
                    show_jeux()
            elif jeu_a_supp in IntOS.dic_bonus:
                if messagebox.askyesno("Launcher de Fastattack", f"Voulez vous supprimer le bonus {jeu_a_supp}"):
                    IntOS.supprimer("bonus", jeu_a_supp)
                    show_bonus()
            elif jeu_a_supp is not None:
                messagebox.showerror("Suppression", "Nom du jeu/bonus entré inconnu")


def modifier():
    jeux_a_modif = dic_selectionne["liste_jeux_selectionne"]
    bonus_a_modif = dic_selectionne["liste_bonus_selectionne"]
    if jeux_a_modif != []:
        for item in jeux_a_modif:
            nouv_nom = simpledialog.askstring("Modifier", f"Nouveau nom de {item}")
            if nouv_nom != "":
                if item in IntOS.dic_jeux:
                    IntOS.modifier_nom("jeux", item, nouv_nom)
                else:
                    messagebox.showerror("Modifier", f"Le jeu {item} n'est pas enregistré dans le launcher")
        reset()
    if bonus_a_modif != []:
        for item in bonus_a_modif:
            nouv_nom = simpledialog.askstring("Modifier", f"Nouveau nom de {item}")
            if nouv_nom != "":
                if item in IntOS.dic_bonus:
                    IntOS.modifier_nom("bonus", item, nouv_nom)
                else:
                    messagebox.showerror("Modifier", f"Le bonus {item} n'est pas enregistré dans le launcher")
        reset()
    if jeux_a_modif == [] and bonus_a_modif == []:
        messagebox.showinfo("Modifier", "Aucun jeu/bonus sélectionné")


# Autres fonctions
def get_nom_jeu(path: str) -> str:
    try:
        if path.endswith(".url") or path.endswith(".lnk") or path.endswith(".exe"):
            nom = path[:-4]
            if "/" in nom or "\\" in nom:
                nom_retourne = list(reversed(nom))
                slash = 0
                for lettre in nom_retourne:
                    if lettre == "/" or lettre == "\\":
                        break
                    slash += 1
                nom = nom[len(nom)-slash:]
        else:
            nom = ""
    except:
        nom = ""
    return nom


def play():
    if len(dic_selectionne["liste_jeux_selectionne"]) > 1:
        messagebox.showwarning("Launcher de Fastattack", "Plusieurs jeux sélectionnés")
    elif len(dic_selectionne["liste_jeux_selectionne"]) == 0:
        if dic_selectionne["liste_bonus_selectionne"] == []:
            messagebox.showinfo("Launcher de Fastattack", "Pas de jeux ni de bonus sélectionnés")
        else:
            IntOS.lancer("PaS_dE_Jeu_A_LANcER", dic_selectionne["liste_bonus_selectionne"])
            messagebox.showinfo("Launcher de Fastattack", "Pas de jeux séléctionné : les bonus séléctionnés ont été lancés")
    else:
        # quand 1 seul jeu est select
        IntOS.lancer(dic_selectionne["liste_jeux_selectionne"][0], dic_selectionne["liste_bonus_selectionne"])


def recherche():
    item = simpledialog.askstring("Recherche", "Jeu/bonus à rechercher")
    if item in IntOS.dic_jeux:
        if messagebox.askyesno("Recherche", f"Jeu {item} trouvé\rVoulez-vous le lancer ?"):
            IntOS.lancer(item, dic_selectionne["liste_bonus_selectionne"])
    elif item in IntOS.dic_bonus:
        if messagebox.askyesno("Recherche", f"Bonus {item} trouvé\rVoulez-vous le lancer ?"):
            IntOS.lancer("PaS_dE_Jeu_A_LANcER", [item])
    elif item is None:
        pass
    else:
        messagebox.showinfo("Recherche", f"{item} est introuvable")


def trier():
    messagebox.showinfo("Trier", "Fonction de tri à venir")


def jeu_random():
    if len(IntOS.dic_jeux["liste_jeux"]) > 1:
        numero = random.randint(0, len(IntOS.dic_jeux["liste_jeux"]))
        jeu = IntOS.dic_jeux["liste_jeux"][numero]
        if messagebox.askyesno("Random", f"Le jeu choisi par l'aléatoire est {jeu}\rVoulez-vous le lancer ?"):
            IntOS.lancer(jeu, dic_selectionne["liste_bonus_selectionne"])
    else:
        messagebox.showwarning("Random", "Pas assez de jeux enregistrés dans le launcher")


def avance():
    rep = simpledialog.askstring("Avancé", "Que voulez vous faire ?\rModifier l'application [M]\rAfficher la console [C]\rAfficher les informations à propos du launcher [I]")
    if rep == "M":
        rep = simpledialog.askstring("Modification", "Que voulez vous faire ?\rDésinstaller l'application [D]\rMettre à jour l'application [M]\rAccéder aux fichiers locaux [F]")
        if rep == "D":
            if messagebox.askokcancel("Désinstallation", "Êtes vous sûr de vouloir désinstaller l'application ? Toutes les données seront supprimées"):
                messagebox.showinfo("Désinstaller", "Fonction de désinstallation à venir")
        elif rep == "M":
            maj = init.check_maj()
            if maj == 0:
                messagebox.showinfo("Mise à jour", "Pas de mise à jour disponible")
            elif maj == 1:
                if messagebox.askyesno("Mise à jour", "Mise à jour disponible\rVoulez vous effectuer la mise à jour ?"):
                    try:
                        os.startfile("MAJ_launcher_de_Fastattack.exe")
                    except:
                        messagebox.showerror("Mise à jour", "Logiciel de mise à jour introuvable")
            else:
                messagebox.showerror("Mise à jour", "Une erreur a eu lieu durant la vérification de mise à jour\rVeuillez lire la console pour plus d'informations sur l'erreur")
        elif rep == "F":
            os.startfile(os.getcwd())
    elif rep == "I":
        with open("Infos.txt", "r") as b:
            infos = b.readlines()
        messagebox.showinfo("A propos du launcher", f"Développé par Fastattack\r{infos[0]}")
    elif rep == "C":
        if messagebox.askokcancel("Console", "Le terminal va s'ouvrir dans la console du launcher\rL'interface du launcher sera inutilisable tant que le le terminal est actif"):
            Terminal.launch()


# définition de la fenêtre et de ses paramètres
fen = tk.Tk()
fen.title("Launcher de Fastattack")
fen.geometry("1280x720")
fen.resizable(width=False, height=False)

# definitions lignes et colonnes
fen.grid_columnconfigure(0, weight=0)
fen.grid_columnconfigure(1, weight=1)
fen.grid_columnconfigure(2, weight=1)
fen.grid_columnconfigure(3, weight=1)
fen.grid_columnconfigure(4, weight=1)
fen.grid_columnconfigure(5, weight=0)
fen.grid_rowconfigure(0, weight=0)
fen.grid_rowconfigure(1, weight=0)
fen.grid_rowconfigure(2, weight=0)
fen.grid_rowconfigure(3, weight=0)
fen.grid_rowconfigure(4, weight=0)
fen.grid_rowconfigure(5, weight=0)
fen.grid_rowconfigure(6, weight=1)
fen.grid_rowconfigure(7, weight=1)
fen.grid_rowconfigure(8, weight=1)
fen.grid_rowconfigure(9, weight=0)

# variables et objets tkinter
bouton_jeux = tk.Button(fen, text="Jeux", command=show_jeux)
bouton_jeux.grid(column=0, row=0, sticky="nswe", padx=5, pady=5)
bouton_bonus = tk.Button(fen, text="Bonus", command=show_bonus)
bouton_bonus.grid(column=0, row=1, sticky="nswe", padx=5, pady=5)
bouton_reset = tk.Button(fen, text="Reset", command=reset)
bouton_reset.grid(column=0, row=2, sticky="nwe", padx=5, pady=5)
bouton_pageS = tk.Button(fen, text="pageS", command=page_suivante)
bouton_pageS.grid(column=0, row=3, sticky="nswe", padx=5, pady=5)
bouton_pageP = tk.Button(fen, text="pageP", command=page_precedente)
bouton_pageP.grid(column=0, row=4, sticky="nswe", padx=5, pady=5)
bouton_lancer = tk.Button(fen, text="Jouer", command=play)
bouton_lancer.grid(column=0, row=11, sticky="nswe", padx=5, pady=5)
bouton_recherche = tk.Button(fen, text="Rechercher", command=recherche)
bouton_recherche.grid(column=5, row=0, sticky="nswe", padx=5, pady=5)
bouton_tri = tk.Button(fen, text="Filtrer", command=trier)
bouton_tri.grid(column=5, row=1, sticky="nswe", padx=5, pady=5)
bouton_random = tk.Button(fen, text="Random", command=jeu_random)
bouton_random.grid(column=5, row=2, sticky="nswe", padx=5, pady=5)
bouton_add = tk.Button(fen, text="Ajouter", command=ajout)
bouton_add.grid(column=5, row=3, sticky="nswe", padx=5, pady=5)
bouton_supp = tk.Button(fen, text="Supprimer", command=supprimer)
bouton_supp.grid(column=5, row=4, sticky="nswe", padx=5, pady=5)
bouton_modifier = tk.Button(fen, text="Modifier", command=modifier)
bouton_modifier.grid(column=5, row=5, sticky="nswe", padx=5, pady=5)
bouton_avance = tk.Button(fen, text="Avancé", command=avance)
bouton_avance.grid(column=5, row=11, sticky="nswe", padx=5, pady=5)


# commandes de start
check = IntOS.check()
if check[0] != []:
    messagebox.showwarning("Launcher de Fastattack", f"Les jeux {check[0]} n'ont pas été trouvés: ils ne pourront pas être lancés")
if check[1] != []:
    messagebox.showwarning("Launcher de Fastattack", f"Les bonus {check[1]} n'ont pas été trouvés: ils ne pourront pas être lancés")

show_jeux()
up_select()
up_page()

fen.mainloop()
