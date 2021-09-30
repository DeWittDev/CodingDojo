
for i in range(150): #basics
    print(i)

for i in range(0,1000,5): #Multiples of 5
    print(i)

for i in range(1,100): #Counting, the Dojo Way
    if i % 10 == 0:
        print('Coding')
    elif i % 5 == 0:
        print('Coding Dojo')
    else:
        print(i)

x = 0
for i in range(0,500000):
    if i % 2 == 1:
        x += i

print(x)

for i in range(2018,0,-4):
    print(i)


lowNum = 3945
highNum =4034
mult = 8
for i in range(lowNum,highNum):
    if i % mult == 0:
        print(i)