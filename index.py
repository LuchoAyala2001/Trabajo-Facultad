#Ya instale ahora estoy importando pandas
import pandas as pd
import os

#Aca vamos a definir las funciones que va a tener nuestro programa principal

#Vamos A crear una lista con los datos del pokemon
def listaPokemones(cantidad):
    pokemones = []
    for _ in range(cantidad):
        nombre = input("Ingrese el nombre del Pokémon: ")
        tipo = input("Ingrese el tipo del Pokémon: ")
        nivel = int(input("Ingrese el nivel del Pokémon: "))
        habilidad = input("Ingrese la habilidad del Pokémon: ")
        ataque = input("Ingrese el ataque principal del Pokémon: ")

        pokemon = [nombre, tipo, nivel, habilidad, ataque]
        pokemones.append(pokemon)

    return pokemones

#Funciones en las que se pasan de lista a data frames y que los data frames se crean y se pasan a un archivo excel

def añadirYCrearExcel (data_frame_pokemones):
    data_frame_pokemones.to_excel('Pokedex.xlsx', index = False)

def añadirAlExcel(data_frame_pokemones):
    pokedex = pd.read_excel('Pokedex.xlsx')
    pokedex = pd.concat([pokedex, data_frame_pokemones], ignore_index=True)
    pokedex.to_excel('Pokedex.xlsx', index=False)



def agregarPokemones():
    print("Bienvenido vas a agregar pokemones para tu pokedex")
    cantidad_a_capturar = int(input("Ingrese la cantidad de pokemones a capturar "))
    pokemones = listaPokemones(cantidad_a_capturar )
    data_frame_pokemones = pd.DataFrame(pokemones,columns=['Nombre','Tipo','Nivel','Habilidad','Ataque'])

    if os.path.exists('Pokedex.xlsx'):
        añadirAlExcel(data_frame_pokemones)
    else:
        añadirYCrearExcel(data_frame_pokemones)

# Funcion que revisa los pokemones en el archivo excel
def imprimirPokemones():
    print("Vamos a revisar su pokedex")
    if os.path.exists('Pokedex.xlsx'):
        pokedex = pd.read_excel('Pokedex.xlsx')
        print(pokedex)
    else:
        print("Usted no tiene pokemones en su pokedex")

# Funcion que permite la busqueda de su pokemon
def buscarPokemons(nombre,nivel):
    if os.path.exists('Pokedex.xlsx'):
        pokedex = pd.read_excel('Pokedex.xlsx')
        buscador = pokedex[(pokedex['Nombre']== nombre) & (pokedex['Nivel'] == nivel)]

        if not buscador.empty:
            print(buscador)
        else:
            print("No hay pokemones con esas caracteristicas")
    else:
        print("No existen Pokemons en su pokedex")


#Funcion que permite eliminar los pokemon
def eliminarPokemon(numero):
       
     if os.path.exists('Pokedex.xlsx'):
        pokedex = pd.read_excel('Pokedex.xlsx')

        if numero < len(pokedex):
            pokedex.drop([numero], axis=0, inplace=True)
            print(pokedex)
            pokedex.to_excel('Pokedex.xlsx', index=False)
        else:
            print("No hay pokemones en esa fila")
     else:
         print("No existen pokemones en su pokedex")



#Funcion de menu que recopila las demas funciones para hacerlo interactivo y que el usuario decida que hacer con su pokedex
def menu():
    print("Bienvenido a su pokedex, aqui tiene una serie de codigos que seran necesarios para manejarse en el")
    print("Presiona 1 si quiere ver los pokemones que obtuvo")
    print("Presione 2 si quiere agregar pokemones a su pokedex")
    print("Presione 3 si quiere buscar algun pokemon con esas caracteristicas")
    print("Presione 4 si quiere eliminar un pokemon")
    print("Presione 5 si quiere cerrar su pokedex")

    terminar = False
   
    while not terminar:
        codigo = int(input("ingrese su codigo"))

        if codigo == 1:
            imprimirPokemones()
        elif codigo == 2:
            agregarPokemones()
        elif codigo == 3:
            print("Vamos a buscar a su pokemon con sus caracteristicas preferidas")
            nombre = input("Ingrese el nombre de su pokemon")
            nivel = int(input("Ingrese el nivel de su pokemon"))
            buscarPokemons(nombre,nivel)
        elif codigo == 4:
            print("Vamos a eliminar de acuerdo a su fila ")
            imprimirPokemones()
            fila = int(input("Inserte el numero de fila para eliminar su pokemon"))
            eliminarPokemon(fila)
        elif codigo == 5:
            print("Gracias por visitar a la pokedex")
            terminar = True
        else:
            print("Inserte un codigo valido")

menu()

