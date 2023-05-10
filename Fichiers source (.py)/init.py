import os
import requests


def check_files():
    if not os.path.isdir(r"fichiers"):
        os.mkdir(r"fichiers")
    if not os.path.isdir(r"fichiers\jeux url"):
        os.mkdir(r"fichiers\jeux url")
    if not os.path.isdir(r"fichiers\icones"):
        os.mkdir(r"fichiers\icones")
    if not os.path.isfile(r"jeux.txt"):
        f = open("jeux.txt", "x")
        f.close()
    if not os.path.isfile(r"bonus.txt"):
        f = open("bonus.txt", "x")
        f.close()
    if not os.path.isfile(r"Infos.txt"):
        f = open("Infos.txt", "x")
        f.close()


def check_maj() -> int:
    """
    CHeck si une mise à jour est disponible
    :return: 0 pour pas de MAJ/1 pour MAJ à effectuer/2 si une erreur a eu lieu
    """
    if os.path.isfile("Infos.txt"):
        with open("Infos.txt", "r") as b:
            lignes = b.readlines()
        if len(lignes) > 0:
            if lignes[0].startswith("Version:"):
                try:
                    version = float(lignes[0].replace("Version:", ""))
                except:
                    print("ERROR: La version n'est pas lisible (fichier Infos.txt)")
                    return 2
                r = requests.get("https://raw.githubusercontent.com/fastattackv/Launcher-de-Fastattack/main/T%C3%A9l%C3%A9chargements/Infos_git.txt")
                if r.content[0:8] == b"Version:":
                    version_git = r.content.replace(b"Version:", b"")
                    version_git = float(version_git.replace(b"\n", b""))
                    if version_git == version:
                        return 0
                    elif version_git > version:
                        return 1
                    else:
                        print("ERROR: La version indiquée est plus récente que la version github. Veuillez vérifier la version manuellement (fichier Infos.txt)")
                        return 2
                else:
                    print("ERROR: Lecture de la version sur github impossible")
                    return 2
            else:
                print("ERROR: Mise à jour impossible, version introuvable (fichier Infos.txt)")
                return 2
        else:
            print("ERROR: Fichier Infos.txt vide")
            return 2
    else:
        print("ERROR: fichier Infos.txt introuvable")
        return 2


# exécution des fonctions
check_files()


# Si, durant le modding, voulez ajouter des instructions qui s'exécuteront au lancement du launcher, ajoutez les ici:
