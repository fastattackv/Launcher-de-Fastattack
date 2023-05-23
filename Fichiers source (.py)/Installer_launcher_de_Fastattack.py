import requests
import os
import zipfile

# demande où installer l'application
print("Installateur du launcher de Fastattack")
print("Verion de l'installateur: v1.2, version du launcher à installer: v1.2")
varb = True
dossier = ""
while varb:
    dossier = input("Dans quel dossier voulez vous installer le launcher [chemin valide]: ")
    if dossier.startswith('"') and dossier.endswith('"'):
        dossier = dossier.removeprefix('"')
        dossier = dossier.removesuffix('"')
    if os.path.isdir(dossier):
        varb = False
    else:
        print("Chemin/nom de dossier invalide")

# demande s'il faut créer un raccourci sur le bureau
raccourci = input("Voulez vous créer un raccourci sur le bureau [Y/n]: ")
if raccourci == "Y":
    racourci = True
else:
    raccourci = False

# télécharge le fichier .zip qui contient l'application et les fichiers
url = "https://github.com/fastattackv/Launcher-de-Fastattack/blob/main/T%C3%A9l%C3%A9chargements/Launcher%20de%20Fastattack%20v1.2.zip?raw=true"
filename = dossier + r"\Launcher de Fastattack v1.0.zip"
try:
    r = requests.get(url)
except:
    print("ERROR: Le fichier à télécharger n'existe pas: essayez d'éxecuter la dernière version de l'application d'installation")
    input("Entrée pour quitter")
else:
    f = open(filename, 'wb')
    f.write(r.content)
    f.close()

# dézip le fichier
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(dossier)

# supprime le .zip
    os.remove(filename)

# créé le raccourci
    if raccourci:
        import win32com.client

        chemin = os.path.join(os.path.join(os.environ['USERPROFILE']), r'Desktop\Launcher de Fastattack.lnk')
        target = dossier + r"\Launcher de Fastattack\Launcher de Fastattack.exe"

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(chemin)
        shortcut.Targetpath = target
        shortcut.WindowStyle = 7
        shortcut.save()

    print("Installation terminée")
    input("Entrée pour quitter")
