from enum import Enum

class Stagione(Enum):
    PRIMAVERA = 1
    ESTATE = 2
    AUTUNNO = 3
    INVERNO = 4
    # DECORATORE
    @property
    def fa_caldo(self):
        return self in {Stagione.PRIMAVERA, Stagione.ESTATE}
    
    def descrizione(self):
        return {
            Stagione.PRIMAVERA: "Il tempo si riscalda",
            Stagione.ESTATE: "Andiamo al mare",
            Stagione.AUTUNNO: "Cadono le foglie",
            Stagione.INVERNO: "L'inverno sta arrivando!",
        } [self] 
    
stagione_corrente = Stagione.INVERNO   
print(stagione_corrente.descrizione())

print(stagione_corrente.fa_caldo)