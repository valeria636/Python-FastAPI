### Imports ################################################## 
import os   #per neteja la pantalla
import json
#Variables ###################################################

#Nom del fitxer on desar/carregar dades
FITXER_JSON = "alumnes.json"


### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla. 
#   
#   Retorna (str): l'opció escollida per l'usuari
##############################################################
def menu():
    #Netejem la pantalla
    os.system('cls')            
    
    #Mostrem les diferents opcions
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")
    
    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    #i retornem l'opció escollida per l'usuari
    return input()

### Funcions per a la gestió d'alumnes ######################

# Carregar alumnes del fitxer JSON
def carregar_alumnes():
    with open("alumnes.json", "r", encoding="utf-8") as fitxer:
        return json.load(fitxer)

# Assignem la llista d'alumnes carregada
alumnes = carregar_alumnes()

def desar_alumnes(alumnes):
    with open(FITXER_JSON, "w", encoding="utf-8") as file:
        json.dump(alumnes, file, indent=4, ensure_ascii=False)

def obtenir_seguent_id(alumnes):
    return max((alumne["id"] for alumne in alumnes), default=0) + 1

### Programa ################################################

#Fins a l'infinit (i més enllà)
while True:
    
    #Executem una opció funció del que hagi escollit l'usuari
    match menu():

        # Mostrar alumnes ##################################
        case "1":
            os.system('cls')
            print("Mostrar alumnes")
            print("-------------------------------")
            

            #Introduiu el vostre codi per mostrar alumnes aquí
            for alumne in alumnes:
                print(f"ID: {alumne['id']}, Nom: {alumne['nom']} {alumne['cognom']}")
            input()
            
    
        # Afegir alumne ##################################
        case "2":
            os.system('cls')
            print("Afegir alumne")
            print("-------------------------------")
            
            #Introduiu el vostre codi per afegir un alumne aquí
            nom = input("Nom: ")
            cognom = input("Cognom: ")
            dia = int(input("Dia de naixement: "))
            mes = int(input("Mes de naixement: "))
            any = int(input("Any de naixement: "))
            email = input("Email: ")
            feina = input("Treballa? (True/False): ").lower() == "true"
            curs = input("Curs: ")
                
            nou_id = obtenir_seguent_id(alumnes)
            nou_alumne = {
                "id": nou_id,
                "nom": nom,
                "cognom": cognom,
                "data": {"dia": dia, "mes": mes, "any": any},
                "email": email,
                "feina": feina,
                "curs": curs
            }
            alumnes.append(nou_alumne)
            print("Alumne afegit amb èxit!")
            input()
    
        # Veure alumne ##################################
        case "3":
            os.system('cls')
            print("Veure alumne")
            print("-------------------------------")
            
            #Introduiu el vostre codi per veure un alumne aquí
            id_alumne = int(input("ID de l'alumne: "))
            alumne = next((a for a in alumnes if a["id"] == id_alumne), None)
            print(json.dumps(alumne, indent=4, ensure_ascii=False) if alumne else "Alumne no trobat!")
            input()

        # Esborrar alumne ##################################
        case "4":
            os.system('cls')
            print("Esborrar alumne")
            print("-------------------------------")
          
            #Introduiu el vostre codi per esborrar un alumne aquí
            id_alumne = int(input("ID de l'alumne a esborrar: "))
            alumnes = [a for a in alumnes if a["id"] != id_alumne]
            print("Alumne esborrat!")
            input()

        # Desar a fitxer ##################################
        case "5":
            os.system('cls')
            print("Desar a fitxer")
            print("-------------------------------")

            #Introduiu el vostre codi per desar a fitxer aquí
            desar_alumnes(alumnes)
            print("Dades desades.")
            input()

        # Llegir fitxer ##################################
        case "6":    
            os.system('cls')
            print("Llegir fitxer")
            print("-------------------------------")

            #Introduiu el vostre codi per llegir de fitxer aquí
            alumnes = carregar_alumnes()
            print("Dades carregades.")
            input()

      

        # Sortir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")

            #Trenquem el bucle infinit
            break

        #Qualsevol altra cosa #####################   
        case _:
            print("\nOpció incorrecta\a")            
            input() 
