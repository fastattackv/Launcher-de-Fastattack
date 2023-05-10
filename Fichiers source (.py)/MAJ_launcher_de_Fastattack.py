import os
import requests
import zipfile
import psutil
import shutil

# recherche les versions actuelle et à installer
# Si une erreur apparait dans cette partie le logiciel crash car il n'est pas censé avoir d'erreurs (cette fonction a été passée avant d'executer ce code)
print("Installateur de mise à jour du launcher de Fastattack")
print("Version de l'installateur: 1.0")
with open("Infos.txt", "r") as b:
    lignes = b.readlines()
version = float(lignes[0].replace("Version:", ""))
r = requests.get("https://raw.githubusercontent.com/fastattackv/Launcher-de-Fastattack/main/T%C3%A9l%C3%A9chargements/Infos_git.txt")
version_git = r.content.replace(b"Version:", b"")
version_git = float(version_git.replace(b"\n", b""))
print(f"Version actuelle: {version}, Version à installer: {version_git}")
print("MAJ: Début de la mise à jour")

# kill l'application si elle est lancée
PROCNAME = "Launcher de Fastattack.exe"
for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        print("MAJ: Fermeture du launcher")
        proc.kill()

# Création du dossier MAJ et téléchargement .zip
print("MAJ: Téléchargement de la nouvelle version")
os.mkdir("MAJ")
url = f"https://github.com/fastattackv/Launcher-de-Fastattack/blob/main/Launcher%20de%20Fastattack%20v{version_git}.zip?raw=true"
filename = rf"MAJ\Launcher de Fastattack v{version_git}.zip"
try:
    r = requests.get(url)
except:
    print("ERROR: Le téléchargement du fichier de mise à jour a échoué")
    os.remove("MAJ")
    input("Entrée pour quitter")
else:
    f = open(filename, 'wb')
    f.write(r.content)
    f.close()

# Dézip le fichier
    print("MAJ: Extraction des fichiers de mise à jour")
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall("MAJ")

# Supprime le fichier de mise à jour .exe (inutile)
    os.remove(r"MAJ\Launcher de Fastattack\MAJ_launcher_de_Fastattack.exe")

# Supprime les anciens fichiers et les remplace par les nouveaux
    print("MAJ: Suppression de l'ancienne application")
    if not os.path.isfile("Launcher de Fastattack.exe"):
        print("ERROR: Ancienne application introuvable: arrêt de la mise à jour")
        os.path.remove("MAJ")
        input("Entrée pour quitter")
    else:
        os.remove("Launcher de Fastattack.exe")
        os.remove("Infos.txt")
        print("MAJ: Installation de la nouvelle version")
        shutil.copy(r"MAJ\Launcher de Fastattack\Launcher de Fastattack.exe", os.getcwd())
        shutil.copy(r"MAJ\Launcher de Fastattack\Infos.txt", os.getcwd())
        os.remove(r"MAJ\Launcher de Fastattack\Launcher de Fastattack.exe")
        os.remove(r"MAJ\Launcher de Fastattack\Infos.txt")
        print("MAJ: Mise à jour terminée avec succès")
        print(f"Version installée: {version_git}")
        input("Entrée pour quitter")
