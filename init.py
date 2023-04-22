def check_modules() -> str:
    liste_pas_installe = []
    try:
        import pickle
    except:
        liste_pas_installe.append("pickle")
    try:
        import tkinter
    except:
        liste_pas_installe.append("tkinter")
    try:
        import os
    except:
        liste_pas_installe.append("os")
    try:
        import sys
    except:
        liste_pas_installe.append("sys")
    try:
        import shutil
    except:
        liste_pas_installe.append("shutil")
    try:
        import PIL
    except:
        liste_pas_installe.append("PIL")
    if liste_pas_installe != []:
        print("CRITICAL ERROR: modules " + str(liste_pas_installe) + " introuvables : l'application ne peux pas être lancée")
        return "ERROR"
    else:
        return "OK"


def check_files():
    import os
    import pickle
    if not os.path.isdir(r"fichiers"):
        os.mkdir(r"fichiers")
    if not os.path.isdir(r"fichiers\jeux url"):
        os.mkdir(r"fichiers\jeux url")
    if not os.path.isdir(r"fichiers\icones"):
        os.mkdir(r"fichiers\icones")
    if not os.path.isfile(r"bonus"):
        var = {'liste_bonus': []}
        with open('bonus', 'wb') as b:
            pickle.dump(var, b)
    if not os.path.isfile(r"jeux"):
        var = {'liste_jeux': []}
        with open('jeux', 'wb') as b:
            pickle.dump(var, b)


def check_integrity() -> str:
    import os.path
    liste_manquants = []
    if not os.path.isfile("interactions_os.py"):
        liste_manquants.append("interactions_os.py")
    if not os.path.isfile("get_icons.py"):
        liste_manquants.append("get_icons.py")
    if liste_manquants != []:
        print("CRITICAL ERROR: fichiers " + str(liste_manquants) + " introuvables : l'application ne peux pas être lancée")
        return "ERROR"
    else:
        return "OK"


def check_tout():
    rep = check_modules()
    if rep == "OK":
        rep = check_integrity()
        if rep == "OK":
            check_files()
        elif rep == "ERROR":
            while True:
                input()
    elif rep == "ERROR":
        while True:
            input()
