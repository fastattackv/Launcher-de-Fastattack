import os
import shutil
from PIL import Image


# quand raccourcis steam = .url
def get_icone_steam(chemin_jeu: str, jeu: str) -> str:
    """
    Copie l'icone du fichier de raccourci steam (.url) au dossier d'icones
    :param chemin_jeu: chemin du raccourci steam
    :param jeu: nom du jeu (qui sera donné à l'icone)
    :return: ERROR si erreur, OK si pas d'erreurs
    """
    to_return = "ERROR"
    if os.path.isfile(chemin_jeu):
        if chemin_jeu.endswith(".url"):
            a = open(chemin_jeu, "r")
            content = a.readlines()
            a.close()
            try:
                path_icone = content[6]
            except:
                to_return = "ERROR"
            else:
                if path_icone.startswith("IconFile="):
                    try:
                        path_icone = path_icone.removeprefix("IconFile=")
                        shutil.copyfile(path_icone.strip(), rf"fichiers\icones\{jeu}.ico")
                    except:
                        to_return = "ERROR"
                    else:
                        ico_to_png(rf"fichiers\icones\{jeu}.ico")
                        to_return = "OK"
                else:
                    to_return = "ERROR"
        else:
            to_return = "ERROR"
    else:
        print("ERREUR: fichier introuvable (fonction get_icones_url_steam->get_icons)")
    return to_return


# quand raccourci epic = .url
def get_icone_epic(chemin_jeu: str, jeu: str) -> str:
    """
    Obtient le chemin du .exe par le raccourci .url puis extrait l'icone
    :param chemin_jeu: chemin du raccourci epic (.url)
    :param jeu: nom du jeu (qui sera donné à l'icone)
    :return: ERROR si erreur, OK si pas d'erreurs
    """
    to_return = "ERROR"
    if os.path.isfile(chemin_jeu):
        if chemin_jeu.endswith(".url"):
            a = open(chemin_jeu, "r")
            content = a.readlines()
            a.close()
            try:
                path_icone = content[7]
            except:
                to_return = "ERROR"
            else:
                if path_icone.startswith("IconFile="):
                    try:
                        path_icone = path_icone.removeprefix("IconFile=")
                        b = extract_icon_from_exe(path_icone.strip(), jeu, r"fichiers\icones")
                        if os.path.isfile(b):
                            to_return = "OK"
                    except:
                        to_return = "ERROR"
                else:
                    to_return = "ERROR3"
        else:
            to_return = "ERROR"
    else:
        print("ERREUR: fichier introuvable (fonction get_icone_epic->get_icons)")
    return to_return


def extract_icon_from_exe(icon_in_path, icon_name, icon_out_path, out_width = 100, out_height = 100):
    # https://techartorg.github.io/python3/python3-snippets/extract_icon_from_exe/   created by bob white (un peu modifié)
    """Given an icon path (exe file) extract it and output at the desired width/height as a png image.

    Args:
        icon_in_path (string): path to the exe to extract the icon from
        icon_name (string): name of the icon so we can save it out with the correct name
        icon_out_path (string): final destination (FOLDER) - Gets combined with icon_name for full icon_path
        out_width (int, optional): desired icon width
        out_height (int, optional): desired icon height

    Returns:
        string: path to the final icon
    """
    import win32ui
    import win32gui
    import win32con
    import win32api
    from PIL import Image

    ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
    ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

    large, small = win32gui.ExtractIconEx(icon_in_path,0)
    win32gui.DestroyIcon(small[0])

    hdc = win32ui.CreateDCFromHandle( win32gui.GetDC(0) )
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap( hdc, ico_x, ico_y )
    hdc = hdc.CreateCompatibleDC()

    hdc.SelectObject( hbmp )
    hdc.DrawIcon( (0,0), large[0] )

    bmpstr = hbmp.GetBitmapBits(True)
    icon = Image.frombuffer(
        'RGBA',
        (32,32),
        bmpstr, 'raw', 'BGRA', 0, 1
    )

    full_outpath = os.path.join(icon_out_path, "{}.png".format(icon_name))
    icon = icon.resize((out_width, out_height))
    icon.save(full_outpath)
    #return the final path to the image
    return full_outpath


def ico_to_png(chemin_ico: str):
    """
    Converti un fichier .ico en .png, ATTENTION le fichier .ico sera supprimé après la conversion
    :param chemin_ico: chemin du fichier .ico à convertir (le .png sera dans le même dossier que le .ico)
    :return: rien
    """
    img = Image.open(chemin_ico)
    chemin_png = chemin_ico.removesuffix(".ico")
    chemin_png += ".png"
    img = img.resize((100, 100))
    img.save(chemin_png)
    img.close()
    os.remove(chemin_ico)


def get_icone(chemin_item: str, item: str) -> str:
    r"""
    essaye les différentes fonctions pour récupérer l'icone du jeu/bonus et l'enregistre dans le dossier fichiers\icones
    :param chemin_item: chemin du jeu/bonus/raccourci duquel il faut enregistrer l'icone
    :param item: nom du jeu/bonus (qui sera donné à l'icone)
    :return: OK si l'icone a été récupérée, ERROR si la récupération de l'icone a échoué
    """
    rep_a = get_icone_steam(chemin_item, item)
    if rep_a == "ERROR":
        rep_b = get_icone_epic(chemin_item, item)
        if rep_b == "ERROR":
            try:
                rep_c = extract_icon_from_exe(chemin_item, item, r"fichiers\icones")
            except:
                rep_c = ""
            if not os.path.isfile(rep_c):
                return "ERROR"
    return "OK"
