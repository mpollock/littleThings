#This program asks for string input and turns it into pig latin
#happy -> appyhay, egg -> eggway
string = raw_input('Enter a word: ')
lain = ""
vowel = ["a","e","i","o","u"]
if string[0].lower() in vowel:
  latin = string + "way"
else:
  for x in range(len(string)):
    if string[x].lower() in vowel:
      latin = string[x:] + string[:x] + "ay"
      break
print latin
