# import json
# miDiccionari = {
#   "nom": "Joan",
#   "cognom": "Figueres",
#   "edat": 30,
#   "ciutat": "Barcelona",
#   "email": "joan@example.com",
#   "telefon": "+34 600 123 456"
# }

# numero = input("Introdueix un numero")
# match numero:
#     case 1:
#     print(miDiccionari.items())
#     case 2:
#     diccionari[clau] = valor
# return miDiccionari

def fes_maca(func):
    def interna():
        print("M'han decorat")  # Afegeix comportament extra
        func()  # Crida la funció original
    return interna  # Torna la funció interna

def funcio_normal():
    print("Sóc normal")

funcio_normal()  # Crida la funció normal

# Creem una versió decorada de la funció normal
funcio_decorada = fes_maca(funcio_normal)

# Cridem la funció decorada
funcio_decorada()