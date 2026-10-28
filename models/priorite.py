from enum import IntEnum


class Priorite(IntEnum):
    BASSE = 1
    NORMALE = 2
    HAUTE = 3
    CRITIQUE = 4

    @property
    def delai_heures(self) -> int:
        match self:
            case Priorite.BASSE:
                return 72
            case Priorite.NORMALE:
                return 24
            case Priorite.HAUTE:
                return 8
            case Priorite.CRITIQUE:
                return 2
