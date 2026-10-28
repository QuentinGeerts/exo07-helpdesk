from models.statut import Statut
from models.ticket import Ticket


class Helpdesk:
    def __init__(self) -> None:
        self.__tickets: list[Ticket] = []

    def ajouter(self, ticket: Ticket) -> None:
        self.__tickets.append(ticket)

    def par_priorite(self) -> list[Ticket]:
        # IntEnum se compare comme un int : CRITIQUE (4) > BASSE (1)
        return sorted(self.__tickets, key=lambda t: t.priorite, reverse=True)

    def repartition(self) -> dict[Statut, int]:
        compteur = {statut: 0 for statut in Statut}   # tous les statuts, même à 0
        for ticket in self.__tickets:
            compteur[ticket.statut] += 1
        return compteur
