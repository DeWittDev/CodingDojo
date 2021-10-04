# #1 Countdown

def Counter(a):
    listing = []
    for i in range(a,-1,-1):
        listing.append(i)
    return listing

print(Counter(7))



# #2 Print and Return
x = [3,5]
def PrintReturn(a):
    for i in a:
        print(a[0])
        return a[1]

print(PrintReturn(x))


#3 First Plus Length
y = [2,9,6,23,7,2,4,14,74]
def FirstPlusLength(a):
    return (len(a) + a[0])

print(FirstPlusLength(y))


#4 Values Greater than Second
def GreaterValue(a):
    b = []
    for i in range(0,len(a)):
        if a[i] > a[1]:
            b.append(a[i])
    print(len(b))
    return b
print(GreaterValue(y))


#5 This Length,That Value
def valueList(length,value):
    b =[]
    for i in range(length):
        b.append(value)
    return b
print(valueList(7,3))