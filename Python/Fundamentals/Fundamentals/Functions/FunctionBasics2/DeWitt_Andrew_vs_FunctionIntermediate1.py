print('----------- 1 -------------------')
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


def updateList(a):
    print(a)
    for i in range(0,len(a)):
        for b in range(0,len(a[i])):
            if a[i][b] == 10:
                a[i][b] = 15
                return a
        else:
            pass
updateList(x)
print(x)
print()

def updateDict1(a,b):
    print(a)
    for i in range(0,len(a)):
        if a[i][b] == 'Jordan':
            a[i][b] = 'Bryant'
            return a
updateDict1(students,'last_name')
print(students)
print()

def updateSports(a):
    print(a)
    for val in a:
        for i in range(0,len(a[val])):
            if a[val][i] == 'Messi':
                a[val][i] = 'Andres'
                return a
        else:
            pass
updateSports(sports_directory)
print(sports_directory)
print()

def updateZ(a):
    for val in a:
        for i in val:
            if val[i] == 20:
                val[i] = 30
                return a
updateZ(z)
print(z)



print('----------- 2 --------------')
users = [
        {'User' : 'Nix', 'Character' : 'Phoenix'},
        {'User' : 'Ninja', 'Character' : '3230'},
        {'User' : 'Proto', 'Character' : 'Legacy'},
        {'User' : 'Phoenix', 'Character' : 'KB'},
        {'User' : 'Nisha', 'Character' : 'Eysh'}
    ]

def iterateionDictionary(a):
    for i in range(0,len(a)):
        for key, val in a[i].items():
            print(key + " - " + val)
iterateionDictionary(users)



print('----------- 3 -------------------')
def iterateionDictionary2(keyName, a):
    for val in range(0,len(a)):
        for i in a[val]:
            if i == keyName:
                print(a[val][i])
iterateionDictionary2('User', users)
iterateionDictionary2('Character', users)



print('----------- 4 -------------------')
dojo = {
    'locations': ['San Jose', 'Seattle', ' Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(a):
    def count(b):
        num = 0
        for i in range(0, len(b)):
            num += 1
        return num
    for i in a:
        print(count(a[i]), i.upper())
        for c in a[i]:
            print(c)
        print()
printInfo(dojo)
