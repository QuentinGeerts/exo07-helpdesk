from models import Categorie, Helpdesk, Priorite, Statut, Ticket


def lire_priorite(saisie: str | int) -> Priorite | None:
    """Convertit une saisie utilisateur en Priorite, ou None si inconnue."""
    try:
        if isinstance(saisie, int):
            return Priorite(saisie)                 # par valeur : Priorite(4)
        return Priorite[saisie.strip().upper()]     # par nom : Priorite["HAUTE"]
    except (KeyError, ValueError):
        return None


# 1. Parcourir l'énumération
print(f"Statuts : {', '.join(statut.value for statut in Statut)}")

# 2. Tickets
t1 = Ticket(1, "Serveur mail en panne", Priorite.CRITIQUE, Categorie.RESEAU)
t2 = Ticket(2, "Imprimante bloquée", Priorite.NORMALE, Categorie.MATERIEL)
t3 = Ticket(3, "VPN instable", Priorite.HAUTE, Categorie.RESEAU)
t4 = Ticket(4, "Nouveau fond d'écran", Priorite.BASSE, Categorie.LOGICIEL)

helpdesk = Helpdesk()
for ticket in (t1, t2, t3, t4):
    helpdesk.ajouter(ticket)

# 3. Transitions autorisées
for statut in (Statut.EN_COURS, Statut.RESOLU, Statut.FERME):
    t1.changer_statut(statut)
for statut in (Statut.EN_COURS, Statut.EN_ATTENTE):
    t2.changer_statut(statut)

# 4. Transition interdite
try:
    t3.changer_statut(Statut.RESOLU)
except ValueError as e:
    print(f"Transition refusée pour #{t3.numero} : {e}")

# 5. Tri et répartition
print("Tickets par priorité :")
for ticket in helpdesk.par_priorite():
    print(f"  {ticket}")

repartition = helpdesk.repartition()
print("Répartition : " + " | ".join(f"{s.value}: {n}" for s, n in repartition.items()))

# 6. Saisies utilisateur
resultats = []
for saisie in ("haute", 4, "urgente"):
    priorite = lire_priorite(saisie)
    affichage = f'"{saisie}"' if isinstance(saisie, str) else str(saisie)
    resultats.append(f"{affichage} → {priorite.name if priorite else 'priorité inconnue'}")
print(" | ".join(resultats))

# 7. Historique
print(f"Historique #{t1.numero} : " + " → ".join(s.value for s in t1.historique))

# ---------------------------------------------------------------------------
# Réponses aux questions
#
# 1. Depuis Python 3.11, IntEnum utilise le __str__ de int : print() affiche
#    la valeur (3). Une Enum classique affiche Classe.MEMBRE. Pour un
#    affichage lisible, on utilise explicitement .name ou .value.
#
# 2. Statut.FERME == "Fermé"        → False : un membre d'Enum n'est pas égal
#                                      à sa valeur.
#    Statut.FERME.value == "Fermé"  → True.
#    C'est voulu : on ne peut pas comparer par accident avec une chaîne.
#
# 3. Une priorité a un ordre naturel (CRITIQUE > HAUTE > ...) : IntEnum
#    permet de trier et de comparer (priorite >= Priorite.HAUTE) sans code
#    supplémentaire. Un statut n'a pas d'ordre : "Résolu > En attente" ne
#    veut rien dire, et le suivi des statuts passe par les transitions, pas
#    par une comparaison. Un IntEnum rendrait possibles des comparaisons
#    absurdes.
# ---------------------------------------------------------------------------
