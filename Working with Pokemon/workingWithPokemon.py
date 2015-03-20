#Funcion recursiva que cicla para encontrar el primer nombre el cual 
#el ultimo caracter de pokemon es el mismo que su primer caracter.
def recursiva():

    found=False

    for pokeShackle in pokedex:

        #Si no hemos encontrado ninguno,  no esta en la lista aun y los caracteres coinciden ...
        if(found==False and tempList.count(pokeShackle)==0 and pokeShackle[0]==tempList[-1][-1] ):
                
                    tempList.append(pokeShackle)
                    found=True
                    recursiva()
    return

##BEGIN MAIN##

#abrimos el fichero y leemos de el
file = open('pokemon.txt','r')

#guardamos el contenido del fichero en una lista temporal.
fileRead = file.read()

#creamos una lista vacia para separar los nombres de los pokemon
pokedex = []

#y por ultimo la lista de la solucion.
solution = []

#El metodo split separa las palabras entre los espacios en blanco.
for i in fileRead.split():

    pokedex.append(i)

#Bucle que cicla sobre toda la lista de Pokemon. Para cada uno de ellos comprobara
#cual es la cadena de Pokemon mas larga.
for pokemon in pokedex:

    tempList=[]
    tempList.append(pokemon)

    recursiva()

    #Si la secuencia actual es mas larga que la que tenemos por solucion...
    if( len(solution) < len(tempList) ):

        #Copia la secuencia actual en solution
        solution=tempList[:]

print len(solution),solution
##END MAIN##