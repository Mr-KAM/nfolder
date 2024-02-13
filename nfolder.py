# Importations =====================================
import os
import datetime
import rich

# Initialisation et importation de données ===============================================


institutions = [
    "INP-HB",
    "ESA",
    "M SUP AGRO",
    "FONCTION PUBLIQUE",
    "MESRS",
    "ENTRE PRIVE",
    "MOI",
    "FAMILLE",
    "AINE-PROF",
    "BOSS",
]
description_inst = """
Institutions :
    1: "INP-HB",
    2: "ESA",
    3: "M SUP AGRO",
    4: "FONCTION PUBLIQUE",
    4: "MESRS",
    5: "ENTRE PRIVE",
    6: "MOI",
    7: "FAMILLE",
    8: "AINE-PROF",
    9: "BOSS"
==================
"""

types = [
    "PROJET",
    "THESE",
    "PFE",
    "COURS",
    "AUTO FORMATIONS",
    "DATABASE",
    "BUSINESS",
    "INFOS",
    "MISSIONS",
    "CODE",
]
description_typ = """
Object or Types:
    1: "PROJET",
    2: "THESE",
    3: "PFE",
    4: "COURS",
    5: "AUTO FORMATIONS"
    6: "DATABASE",
    7: "BUSINESS",
    8: "INFOS",
    9: "MISSIONS",
    10: "CODE"
=================
"""
priorites = {1: "1", 2: "2", 3: "3", 4: "4", 0: "0"}
description_priority = """
Priorité de la tâche :
    1: urgente-importante           ⏰*💎 (A traiter - priorité n°1)
    2: urgente-peu importante       ⏰*👕 (A déléguer - priorité n°2)
    3: peu urgente-importante       🎶*💎 (A planifier - priorité n°3)
    4: peu urgente-peu importante   🎶*👕 (A abandonner)
    0: validé
"""
# ================== Fonctions


def abreviation_mois_annee_actuelle():
    # Obtenir la date et l'heure actuelle
    date_actuelle = datetime.datetime.now()

    # Récupérer l'abréviation du mois et l'année actuelle
    abreviation_mois = date_actuelle.strftime("%b")
    annee = date_actuelle.year

    return f"{abreviation_mois}-{annee}"


def creer_dossiers(nom_dossier):
    chemin = os.path.join(os.getcwd(), nom_dossier)

    # Créer le dossier spécifié s'il n'existe pas déjà
    if not os.path.exists(chemin):
        os.makedirs(chemin)
        print(f"📂 Dossier '{nom_dossier}' créé avec succès !")
    else:
        print(f"Le dossier '{nom_dossier}' existe déjà.")


def create_folder(priorite, typ, inst, name):
    date = abreviation_mois_annee_actuelle()
    folder_name = f"{priorite}.{typ}_{inst}_{name}_{date}".upper()
    creer_dossiers(folder_name)


if __name__ == "__main__":
    priorite = priorites[int(input(f"{description_priority} \n: >"))]
    typ = int(input(f"{description_typ}\n : >"))
    inst = int(input(f"{description_inst} \n: >"))
    name = input(f"Title : >")

    create_folder(priorite, types[typ - 1], institutions[inst], name)
