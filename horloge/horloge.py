from time import *

def afficher_heure(heure):
    print(heure, end='\r')

def regler_heure_manuellement():
    heure_saisie = input("Entrez l'heure au format HH:MM:SS : ")
    try:
        heures, minutes, secondes = map(int, heure_saisie.split(':'))
        return f"{heures:02d}:{minutes:02d}:{secondes:02d}"
    except ValueError:
        print("Format incorrect. Assurez-vous d'entrer l'heure au format correct.")
        return regler_heure_manuellement()

while True:
    heure_actuelle = strftime('%H:%M:%S %p')
    afficher_heure(heure_actuelle)

    modifier_manuellement = input("Voulez-vous régler l'heure manuellement ? (Oui/Non): ").lower()
    if modifier_manuellement == "oui":
        nouvelle_heure = regler_heure_manuellement()
        heures, minutes, secondes = map(int, nouvelle_heure.split(':'))
    else:
        heures, minutes, secondes = map(int, strftime('%H:%M:%S').split(':'))

    while True:
        afficher_heure(f"{heures:02d}:{minutes:02d}:{secondes:02d}")
        secondes = (secondes + 1) % 60  # Incrémente les secondes et boucle à 0 à 59
        sleep(1)