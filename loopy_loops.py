
pokemon = ('picachu', 'charmander', 'bulbasaur')
print(pokemon[1])

starter1, starter2, starter3 = pokemon
print(starter1, starter2, starter3)

MyName= ('K','J''J')
'i' in MyName
print('i' in MyName)

for x in range(2, 11):
    print(x)

x = 2
while x < 11:
    print(x)
    x += 1

MyString='This is a simple string'
for x in MyString:
    print(x)

MyString = ('this', 'is', 'a', 'simple', 'set')
x = 0
for x in MyString:
    for y in range(3):
        print(x)

# The nested loop below was my first try, then i worked on simplifying it.
    
MyString = ('this', 'is', 'a', 'simple', 'set')
x = 0
while x < 5:
    y = 0
    while y < 3:
        print(MyString[x])
        y += 1
    x += 1

