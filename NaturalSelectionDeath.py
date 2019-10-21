#NaturalSelectionDeath
#Max Moverley
#ICS4U
#10/17/19
import random
from NaturalSelectionCharCreate import Person

living=[]
cemetary=[]
archive=[]

def deathCheck(person):
    death=False
    deathChance=random.randrange(0,100)
    if person.age>10 and person.age<=20:
        if deathChance<=15:
            death=True
        else:
            death=False

    elif person.age>20 and person.age<=30:
        if deathChance<=30:
            death=True
        else:
            death=False

    elif person.age>30 and person.age<=35:
        if deathChance<=45:
            death=True
        else:
            death=False

    elif person.age>35 and person.age<=40:
        if deathChance<=60:
            death=True
        else:
            death=False

    elif person.age>40 and person.age<=45:
        if deathChance<=75:
            death=True
        else:
            death=False

    elif person.age>45:
        if deathChance<=90:
            death=True
        else:
            death=False
    
    if death==True:
        person.alive=False
        cemetary.append(person)

        if person in living:
            living.remove(person)

        return cemetary
        return living

    else:
        if person not in living:
            living.append(person)

        return living

for x in range(50):
    archive.append(Person())
    archive[x].age=random.randrange(1,50)
 
for i in range(50):
    for x in range(len(archive)):
        if archive[x].alive==True:
            deathCheck(archive[x])

    print()
    print("TRIAL #",i+1)
    print("TOTAL:",len(archive))
    print("DEAD:",len(cemetary))
    print("LIVING:",len(living))
