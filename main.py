import random


# list_words = [
#     "giraffe", "elephant","cheetah","butterfly","penguin","kangaroo","crocodile","whale","squirrel","flamingo","tiger","zebra","panda","parrot","dolphin","octopus","koala","rhinoceros","hippopotamus","caterpillar","falcon","jellyfish","lobster","chameleon", "armadillo","lemur","quokka","hummingbird","beetle","porcupine","pelican","platypus","lemming","bison","seagull","gazelle","koala","eagle","firefly","hedgehog","albatross","dragonfly","anteater","fox","narwhal","peacock","platypus",
# ]
list_words = ["Dog"]
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(list_words)


len_chosen_word = len(chosen_word)




display_list=[]
for i in range(0, len_chosen_word):
    
    display_list.append("_")
    

    
print("Introduce letters and guess the follwig word")

display_string="".join(display_list)
print(display_string)


print('')

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("guess a letter:\n").lower()
print("")
counter=0

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in chosen_word:
    
    if guess==i:
        display_list[counter]=i
        print("correct")
    
        
    counter+=1
    
print(f"the word doesn't contain the letter {guess}")
print(display_list)