from random import randint
arra2 =[]
y = 1
n = 5
d = 0
while y <= n:
    arra2.append(randint(-12, 50))
    y +=1
c = sum(arra2)
print (arra2, "Summa arra2 = ", c)
