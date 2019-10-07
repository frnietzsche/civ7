from Person_Generator import Person


### MAIN PROGRAM ###

### Generate Sample Data
y=1
for x in range(20):
    print('Person #',y)
    i=Person('Male')
    print()
    y=y+1

for x in range(20):
    print('Person #',y)
    i=Person('Female')
    print()
    y=y+1

for x in range(10):
    print('Person #',y)
    i=Person()
    print()
    y=y+1
