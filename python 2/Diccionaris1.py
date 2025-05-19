import json
miDiccionari = {
  "nom": "Joan",
  "cognom": "Figueres",
  "edat": 30,
  "ciutat": "Barcelona",
  "email": "joan@example.com",
  "telefon": "+34 600 123 456"
}

#Diccionario > String (con formato JSON)
JSON = json.dumps(miDiccionari)
print(JSON)
print()
print(type(JSON)) #Imprimeixo el tipo que es el "JSON"

#String lo escribes a fichero

    #abres fichero (para escritura y texto)
fitxer = open ("fitxerDic.txt", "wt")
    #escribes el string
fitxer.write(JSON)
    #cierras el fichero
fitxer.close()


####################################
print()
#abres un fichero (en formato texto y para leer)
fitxer2 = open ("fitxerDic.txt", "rt")

#lees el fichero a string
llegir = fitxer2.read()

#pasas el string a diccionario
dic = json.loads(llegir)

#muestras el diccionario por pantalla
print(dic)

#cierras el fichero
fitxer2.close()

####################################
print()
def externa(x):
 def interna(y):
    return x + y
 return interna
afegeix_cinc = externa(5)
result = afegeix_cinc(6)
print(result)
#Resultat = 11.

####################################
print()
def afegir(a, b):
 return a + b
def multiplicar(a, b):
 return a * b
def calcular(funcio, x, y):
 return funcio(x, y)
result = calcular(afegir, 4, 6)
print(result) # Mostra 10
result = calcular(multiplicar, 4, 6)
print(result) # Mostra 24

#####################################
print()
def salutacions(nom):
    def hola():
        return "Hola, " + nom + "!"
    return hola
missatge = salutacions("Valèria")
print(missatge()) # mostra "Hola, Valèria!"

