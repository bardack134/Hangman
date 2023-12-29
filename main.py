
# Importar el módulo random para generar números aleatorios
import random

#logos del juego
from hangman_art import *

#lista de palabras del juego
from hangman_words import *

from hangman_instructions import *


from hangman_stages import *


import os
#titulo del juego
print(title)

#logo del juego, del archivo hangman_art.py
print(logo)

#instrucciones del juego, del archivo hangman_instructions.py
print(instruccions)

print("")
print("")
#  lista de palabras posibles para el juego

# una sola palabra para probar el codigo
# list_words = ["dog"]



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
print('')

# Pedir al usuario que adivine una letra y asignar su respuesta a una variable llamada guess. Convertir la respuesta a minúscula.
guess=input("guess a letter: ").lower()


    
while guess.isdigit(): 
    print("you did not enter a letter, please try again")
    print("")
    guess=input("guess a letter: ").lower()
    

# Crear una variable llamada counter para llevar la cuenta de la posición de cada letra en la palabra elegida
counter=0

#variable indicando false, para que entre en el ciclo while 
end_of_game=False


#variable que nos indicara el numero de vidas que tiene el usuario, y las veces que podra intentar, adivinar una palabra
lives=6
# print(lives) para pruebas en el codigo

#ciclo while para permitir al usuario adivinar de nuevo una letra de la palabra hasta que gane o pierda
while end_of_game==False:
    os.system('cls')#limpiamos la consola
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
            print(f"the word doesn't contain the letter {guess}, you lose a life")
            
            print(stages[lives])
            
            #le restamos una vida al numero de vidas del usuario
            lives=lives-1
            
            
            #si el numero de vidas llega a cero, signifca que se acabo el juego, la variable end_of_game se vuelve True y termnina el bucle while
            if lives==-1:
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
            
            
            while guess.isdigit(): 
                print("you did not enter a letter, please try again")
                print("")
                guess=input("guess a letter: ").lower()
    else:
        print("game over")
        
        #cambiamos el valor de la variable, para indicar que el juego termino y salir del ciclo while
        end_of_game=True