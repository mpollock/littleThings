#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
working = True
int = 2520
while (int%11 != 0) or (int%12 != 0) or (int%13 != 0) or (int%14 !=0) or (int%15 != 0) or (int%16 != 0) or (int%17 != 0) or (int%18 != 0) or (int%19 != 0) or (int%20 != 0):
 int += 2520 
print(int)
