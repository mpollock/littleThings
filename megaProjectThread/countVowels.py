#This program asks for string input and turns it into pig latin
#happy -> appyhay, egg -> eggway
string = raw_input('Enter a word: ')
vowels = 0
vowel = ["a","e","i","o","u"]
for x in range(len(string)):
  if string[x].lower() in vowel:
    vowels += 1
print vowels
