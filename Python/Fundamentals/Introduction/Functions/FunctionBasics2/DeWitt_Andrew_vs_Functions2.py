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


# #3 First Plus Length
y = [2,9,6,23,7,2,4,14,74]
def FirstPlusLength(a):
    return (len(a) + a[0])

print(FirstPlusLength(y))


#4 Values Greater than Second
def GreaterValue(a):
    x = []
    for i in a:
        if len(a) < 
        elif a[i] > a[1]:
            x.append(a[i])
