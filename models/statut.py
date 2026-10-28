from enum import Enum


class Statut(Enum):
    NOUVEAU = "Nouveau"
    EN_COURS = "En cours"
    EN_ATTENTE = "En attente client"
    RESOLU = "Résolu"
    FERME = "Fermé"

    def peut_passer_a(self, autre: "Statut") -> bool:
        return autre in _TRANSITIONS[self]

    @property
    def est_termine(self) -> bool:
        return self in (Statut.RESOLU, Statut.FERME)


# Défini HORS de la classe : un dictionnaire déclaré dans le corps d'une Enum
# deviendrait lui-même un membre de l'énumération.
_TRANSITIONS: dict[Statut, set[Statut]] = {
    Statut.NOUVEAU: {Statut.EN_COURS, Statut.FERME},
    Statut.EN_COURS: {Statut.EN_ATTENTE, Statut.RESOLU},
    Statut.EN_ATTENTE: {Statut.EN_COURS},
    Statut.RESOLU: {Statut.FERME, Statut.EN_COURS},
    Statut.FERME: set(),
}
