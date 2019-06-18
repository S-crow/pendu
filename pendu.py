# Jeu Pendu en python 3
import random

print("----- JEU DU PENDU -------")

# array of the possible words 
words = ["dictionnaire", "chien", "arbre", "portable", "maison", "armoire", "journal", "montagne", "buisson"]

word = random.choice(words)
hidden_word = ""
array_letters = []
nb_coups = 0

while True:
    hidden_word = ""

    letter = input("lettre choisie : ")

    for char in word:
    	if letter == char:
    	    array_letters.append(letter)
    	    hidden_word += letter
    	# for letters already found
    	elif char in array_letters:
    		hidden_word += array_letters[array_letters.index(char)]
    	else:
    	    hidden_word += "*"

    print(hidden_word)	 
    nb_coups += 1	    
    if(hidden_word == word):
        print("Bravo, Vous gagnez en", nb_coups, "coups !")
        break	    
           
