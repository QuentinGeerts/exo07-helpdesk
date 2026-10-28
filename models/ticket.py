from models.categorie import Categorie
from models.priorite import Priorite
from models.statut import Statut


class Ticket:
    def __init__(self, numero: int, titre: str, priorite: Priorite, categorie: Categorie) -> None:
        self.numero = numero
        self.titre = titre
        self.priorite = priorite
        self.categorie = categorie
        self.__statut = Statut.NOUVEAU
        self.__historique: list[Statut] = [Statut.NOUVEAU]

    @property
    def statut(self) -> Statut:
        return self.__statut

    @property
    def historique(self) -> tuple[Statut, ...]:
        return tuple(self.__historique)

    def changer_statut(self, nouveau: Statut) -> None:
        if not self.__statut.peut_passer_a(nouveau):
            raise ValueError(f"{self.__statut.value} → {nouveau.value}")
        self.__statut = nouveau
        self.__historique.append(nouveau)

    def __str__(self) -> str:
        priorite = f"{self.priorite.name} ({self.priorite.delai_heures} h)"
        return f"#{self.numero} {priorite:<17} — {self.titre} — {self.__statut.value}"
