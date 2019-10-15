#Small Person Maker
import random
class Person:
    def __init__(self):
        self.strength=0
        self.speed=0
        self.intelligence=0
        
        ###STRENGTH###
        strengthR=random.randrange(1, 16)

        if strengthR<5 and strengthR>0:
            self.strength=random.randrange(1, 4)

        if strengthR<11 and strengthR>=5:
            self.strength=random.randrange(4, 7)

        if strengthR<=15 and strengthR>=11:
            self.strength=random.randrange(7, 10)

        ###SPEED###
        speedR=random.randrange(1, 16)

        if speedR<5 and speedR>0:
            self.speed=random.randrange(1, 4)

        if speedR<11 and speedR>=5:
            self.speed=random.randrange(4, 7)

        if speedR<=15 and speedR>=11:
            self.speed=random.randrange(7, 10)

        ###INTELLIGENCE###
        intelligenceR=random.randrange(1, 16)

        if intelligenceR<5 and intelligenceR>0:
            self.intelligence=random.randrange(1, 4)

        if intelligenceR<11 and intelligenceR>=5:
            self.intelligence=random.randrange(4, 7)

        if intelligenceR<=15 and intelligenceR>=11:
            self.intelligence=random.randrange(7, 10)

        ###ENDURANCE###
        enduranceR=random.randrange(1, 16)

        if enduranceR<5 and enduranceR>0:
            self.endurance=random.randrange(1, 4)

        if enduranceR<11 and enduranceR>=5:
            self.endurance=random.randrange(4, 7)

        if enduranceR<=15 and enduranceR>=11:
            self.endurance=random.randrange(7, 10)


        
        print('Strength:',self.strength)
        print('Speed:',self.speed)
        print('Intelligence:',self.intelligence)
        print('Endurance:',self.endurance)
        
y=1
for x in range(50):
    print('Person #',y)
    i=Person()
    y=y+1
    print()
