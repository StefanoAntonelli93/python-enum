from enum import Enum

class Stagione(Enum):
    PRIMAVERA = 1
    ESTATE = 2
    AUTUNNO = 3
    INVERNO = 4

    def descrizione(self):
        return {
            Stagione.PRIMAVERA: "Il tempo si riscalda",
            Stagione.ESTATE: "Andiamo al mare",
            Stagione.AUTUNNO: "Cadono le foglie",
            Stagione.INVERNO: "L'inverno sta arrivando!",
        } [self]