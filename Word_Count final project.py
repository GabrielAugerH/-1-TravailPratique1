#Fait le 26 septembre 2023
#Créé par Gabriel Auger-Herrera
#Programme qui permet de compter des mots dans une phrase ou un texte

#word_count function
def count_word(word):
     return word.count(' ') +1
#fuction applying by users text as fuction below
mettre_votre_texte = input()
print(count_word(mettre_votre_texte))