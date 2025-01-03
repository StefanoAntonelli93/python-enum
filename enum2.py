from enum import Enum

class PuntoCardinale(Enum):
    NORD = 'N'
    SUD = 'S'
    EST = 'E'
    OVEST = 'W'
# iterazione   f-string   binding   interpolazione
for direzione in PuntoCardinale:
    print(f"Nome: {direzione.name}, Valore: {direzione.value}")


# SCEGLI DI ANDARE A NORD

direzione_giusta = PuntoCardinale.NORD

if direzione_giusta == PuntoCardinale.NORD:
    print("Stai andando a Nord")
else:
    print("Stai andando nella direzione sbagliata")