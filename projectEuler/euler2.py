#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
x = 1
y = 2
t = 0
s = 2
while (y < 4000000):
	t = y
	y = y+x
	x = t
	if (y%2 == 0):
		s += y
print(s)
