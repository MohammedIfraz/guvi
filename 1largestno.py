a = float(input())
b = float(input())
c = float(input())

if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c

print(largest)
