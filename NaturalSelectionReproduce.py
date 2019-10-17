#NaturalSelectionReproduce
#Max Moverley
#ICS4U
#10/2/19
import random
from NaturalSelectionCharCreate import Person

class Child(Person):
    def __init__(self, strength, speed, intelligence, endurance, gender, mom, dad):
        self.strength=strength
        self.speed=speed
        self.intelligence=intelligence
        self.endurance=endurance
        self.gender=gender
        self.mom=mom
        self.dad=dad

        if gender==0:
            print("Gender: Male")
        else:
            print("Gender: Female")
        print('Strength:',self.strength)
        print('Speed:',self.speed)
        print('Intelligence:',self.intelligence)
        print('Endurance:',self.endurance)
        
def reproduce(parent1, parent2):
    ##GENDER##
    gender=random.randrange(0,2)

    ##PARENTS##
    if parent1.gender==1:
        mom=parent1
        dad=parent2

    else:
        mom=parent2
        dad=parent1

    ##STRENGTH##
    if parent1.strength>=parent2.strength:
        strength=random.randrange(parent2.strength-1, parent1.strength+2)

    else:
        strength=random.randrange(parent1.strength-1, parent2.strength+2)

    if strength==10:
        strength=9

    if strength==0:
        strength=1

    ##SPEED##
    if parent1.speed>=parent2.speed:
        speed=random.randrange(parent2.speed-1, parent1.speed+2)

    else:
        speed=random.randrange(parent1.speed-1, parent2.speed+2)

    if speed==10:
        speed=9

    if speed==0:
        speed=1

    ##INTELLIGENCE##
    if parent1.intelligence>=parent2.intelligence:
        intelligence=random.randrange(parent2.intelligence-1, parent1.intelligence+2)

    else:
        intelligence=random.randrange(parent1.intelligence-1, parent2.intelligence+2)

    if intelligence==10:
        intelligence=9

    if intelligence==0:
        intelligence=1

    ##ENDURANCE##
    if parent1.endurance>=parent2.endurance:
        endurance=random.randrange(parent2.endurance-1, parent1.endurance+2)

    else:
        endurance=random.randrange(parent1.endurance-1, parent2.endurance+2)

    if endurance==10:
        endurance=9

    if endurance==0:
        endurance=1

    strengthRoll=random.randrange(1,100)
    speedRoll=random.randrange(1,100)
    intRoll=random.randrange(1,100)
    endurRoll=random.randrange(1,100)

    ##STRENGTH MODIFY##
    if strengthRoll==69:
        strength+=5
        if strength>=10:
            strength=9

    if strengthRoll==70:
        strength-=5
        if strength<=0:
            strength=1

    ##SPEED MODIFY##
    if speedRoll==69:
        speed+=5
        if speed>=10:
            speed=9

    if speedRoll==70:
        speed-=5
        if speed<=0:
            speed=1

    ##INTELLIGENCE MODIFY##
    if intRoll==69:
        intelligence+=5
        if intelligence>=10:
            intelligence=9

    if intRoll==70:
        intelligence-=5
        if intelligence<=0:
            intelligence=1

    ##ENDURANCE MODIFY##
    if endurRoll==69:
        endurance+=5
        if endurance>=10:
            endurance=9

    if endurRoll==70:
        endurance-=5
        if endurance<=0:
            endurance=1

    return Child(strength, speed, intelligence, endurance, gender, mom, dad)

def mateCheck(m1, m2):
    if m1.gender+m2.gender!=1:
        return False

    elif (m1.mate!="" or m2.mate!=""):
        return False
    
    elif m1.child==m2 or m2.child==m1:
        return False

    elif (m1.mom==m2.mom) or (m1.dad==m2.dad):
        return False

    else:
        m3=reproduce(m1,m2)
        m1.mate=m2
        m2.mate=m1
        m1.child.append(m3)
        m2.child=m1.child

        return m3

john=Person()
print()
liz=Person()
print()

garfield=mateCheck(john,liz)
print(john.mate)
