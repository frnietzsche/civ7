#NaturalSelectionReproduce
#Max Moverley
#ICS4U
#10/2/19
import random
from NaturalSelectionCharCreate import Person

class Child:
    def __init__(self, speed, strength, intelligence, curiosity):
        self.speed=speed
        self.strength=strength
        self.intelligence=intelligence
        self.curiosity=curiosity

def reproduce(parent1, parent2):
    if parent1.speed-parent2.speed>=0:
        speed=random.randrange(parent2.speed-1, parent1.speed+2)

    else:
        speed=random.randrange(parent1.speed-1, parent2.speed+2)
        
    if speed==10:
        speed-=1

    if speed==0:
        speed+=1

    if parent1.strength-parent2.strength>=0:
        strength=random.randrange(parent2.strength-1, parent1.strength+2)

    else:
        strength=random.randrange(parent1.strength-1, parent2.strength+2)

    if strength==10:
        strength-=1

    if strength==0:
        strength+=1
        
    if parent1.intelligence-parent2.intelligence>=0:
        intelligence=random.randrange(parent2.intelligence-1, parent1.intelligence+2)

    else:
        intelligence=random.randrange(parent1.intelligence-1, parent2.intelligence+2)

    if intelligence==10:
        intelligence-=1

    if intelligence==0:
        intelligence+=1
        
    if parent1.curiosity-parent2.curiosity>=0:
        curiosity=random.randrange(parent2.curiosity-1, parent1.curiosity+2)

    else:
        curiosity=random.randrange(parent1.curiosity-1, parent2.curiosity+2)

    if curiosity==10:
        curiosity-=1

    if curiosity==0:
        curiosity+=1
            
    return Child(speed,strength,intelligence,curiosity)

#NEED TO INCORPERATE THE REST OF THE STATS#
