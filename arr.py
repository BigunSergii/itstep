from random import randint
arra2 =[]
y = 1
n = 9
while y < n:
    arra2.append(randint(-10, 90))
    y +=1
c = sum(arra2)
print (arra2, "Summa arra2 = ", c)
