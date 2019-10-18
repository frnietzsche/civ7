#NaturalSelectionDeath
#Max Moverley
#ICS4U
#10/17/19
import random
from NaturalSelectionCharCreate import Person

alive=[]
cemetary=[]
archive=[]

def deathCheck(person):
    death=False
    deathChance=random.randrange(0,100)
    if person.age>20 and person.age<=25:
        if deathChance<=15:
            death=True
        else:
            death=False

    elif person.age>25 and person.age<=30:
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
        cemetary.append(person)
        return cemetary

    else:
        alive.append(person)
        return alive

for x in range(50):
    archive.append(Person())

for x in range(len(archive)):
    archive[x].age=random.randrange(1,50)
    if archive[x].death==False:
        deathCheck(archive[x]) 
        
print(len(archive))
print(len(cemetary))
print(len(alive))
