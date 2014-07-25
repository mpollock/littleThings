#This program asks for string input and reverses that string
string = raw_input('Enter a string: ')
backwards = ""
for x in range(len(string), 0, -1):
  backwards += string[x-1]
print backwards
