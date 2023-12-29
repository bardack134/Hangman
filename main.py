
# Importar el módulo random para generar números aleatorios
import random
print('''

 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|

''')
print('''
  ___________.._______
 | .__________))______|
 | | / /      ||
 | |/ /       ||
 | | /        ||.-''.
 | |/         |/  _  \\
 | |          ||  `/,|
 | |          (\\\\`_.'
 | |         .-`--'.
 | |        /Y . . Y\\
 | |       // |   | \\
 | |      //  | . |  \\
 | |     ')   |   |   (`
 | |          ||'||
 | |          || ||
 | |          || ||
 | |          || ||
 | |         / | | \\
 """"""""""|_`-' `-' |"""|
 |"|"""""""\ \       '"|"|
 | |        \ \        | |
 : :         \ \       : :  
 . .          `'       . .
''')

print("""
*GUESS THE LETTERS IN THE HIDDEN WORD. 
    *EACH INCORRECT GUESS ADDS A PART TO THE HANGMAN. 
        *TRY TO GUESS THE WORD BEFORE THE HANGMAN IS COMPLETE.

""")

print("")
print("")
#  lista de palabras posibles para el juego
list_words = [
     "giraffe", "elephant","cheetah","butterfly","penguin","kangaroo","crocodile","whale","squirrel","flamingo","tiger","zebra","panda","parrot","dolphin","octopus","koala","rhinoceros","hippopotamus","caterpillar","falcon","jellyfish","lobster","chameleon", "armadillo","lemur","quokka","hummingbird","beetle","porcupine","pelican","platypus","lemming","bison","seagull","gazelle","koala","eagle","firefly","hedgehog","albatross","dragonfly","anteater","fox","narwhal","peacock","platypus",
 ]
# una sola palabra para probar el codigo
# list_words = ["dog"]

#Estados en los que se encuentra nuestro jugador
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# Elegir una palabra al azar de la lista y asignarla a una variable llamada chosen_word
chosen_word=random.choice(list_words)


# Obtener la longitud de la palabra elegida y asignarla a una variable llamada len_chosen_word
len_chosen_word = len(chosen_word)

# Crear una lista vacía para mostrar la palabra oculta con guiones bajos
display_list=[]

# Recorrer cada letra de la palabra elegida
for i in range(0, len_chosen_word):
    
    # Añadir un guión bajo a la lista de display
    display_list.append("_")



# Convertir la lista de display en una cadena y asignarla a una variable llamada display_string
display_string="".join(display_list)


# Imprimir la cadena de display
print(f'The word to be guessed is "{display_string}".')


# Imprimir una línea vacía para separar
print('')

# Pedir al usuario que adivine una letra y asignar su respuesta a una variable llamada guess. Convertir la respuesta a minúscula.
guess=input("guess a letter: ").lower()



# Crear una variable llamada counter para llevar la cuenta de la posición de cada letra en la palabra elegida
counter=0

#variable indicando false, para que entre en el ciclo while 
end_of_game=False


#variable que nos indicara el numero de vidas que tiene el usuario, y las veces que podra intentar, adivinar una palabra
lives=6
print(lives)

#ciclo while para permitir al usuario adivinar de nuevo una letra de la palabra hasta que gane o pierda
while end_of_game==False:
    
    #miramos si todavia hay espacios abiertos "_" dentro de nuestra palabra ha adivinar, que tenemos mientras tanto en forma de lista
    if "_"  in display_list:
    
        # Recorrer cada letra de la palabra elegida
        for i in chosen_word:
            
            # Comprobar si la letra que el usuario adivinó (guess) es una de las letras de la palabra elegida
            if i==guess:
                
                # Si es así, reemplazar el guión bajo correspondiente en la lista de display por la letra adivinada
                display_list[counter]=i
            
                                        
            # Incrementar el contador en uno
            counter+=1

        # Comprobar si la letra que el usuario adivinó no está en la lista de display
        if guess not in display_list:
            
            # Si es así, imprimir un mensaje que le dice al usuario que la palabra no contiene la letra adivinada
            print(f"the word doesn't contain the letter {guess}")
            
            print(stages[lives])
            
            #le restamos una vida al numero de vidas del usuario
            lives=lives-1
            
            
            #si el numero de vidas llega a cero, signifca que se acabo el juego, la variable end_of_game se vuelve True y termnina el bucle while
            if lives==0:
                print("you have lost, end of the game")
                
                end_of_game=True

        # la lista de display actualizada la convertimos en cadena para imprimirla
              
        display_string="".join(display_list)
        
        print(display_string)
        
        #espacio en pantalla 
        print("")
        
        
        #reseteamosa el contador de nuevo a cero, para que empieza a contar para la nueva letra
        counter=0
        
        #miramos si todavia hay espacios abiertos "_" dentro de nuestra palabra ha adivinar, que tenemos mientras tanto en forma de lista
        if end_of_game==False:
            
            # Pedir al usuario que adivine otra letra y asignar su respuesta a una variable llamada guess. Convertir la respuesta a minúscula.
            guess=input("guess another letter: ").lower()
            
    else:
        print("game over")
        
        #cambiamos el valor de la variable, para indicar que el juego termino y salir del ciclo while
        end_of_game=True