#Small Person Maker
import random
class Person:
    def __init__(self):
        self.strength=0
        self.speed=0
        self.intelligence=0
        self.endurance=0
        self.gender=random.randrange(0, 2)
        
        ###STRENGTH###
        strengthR=random.randrange(1, 20)

        if strengthR<56 and strengthR>0:
            self.strength=random.randrange(1, 4)

        if strengthR<=20 and strengthR>10:
            self.strength=random.randrange(4, 7)

        if strengthR<11 and strengthR>=6:
            self.strength=random.randrange(7, 10)

        ###SPEED###
        speedR=random.randrange(1, 20)

        if speedR<6 and speedR>0:
            self.speed=random.randrange(1, 4)

        if speedR<=20 and speedR>10:
            self.speed=random.randrange(4, 7)

        if speedR<11 and speedR>=6:
            self.speed=random.randrange(7, 10)

        ###INTELLIGENCE###
        intelligenceR=random.randrange(1, 20)

        if intelligenceR<6 and intelligenceR>0:
            self.intelligence=random.randrange(1, 4)

        if intelligenceR<=20 and intelligenceR>10:
            self.intelligence=random.randrange(4, 7)

        if intelligenceR<11 and intelligenceR>=6:
            self.intelligence=random.randrange(7, 10)

        ###ENDURANCE###
        enduranceR=random.randrange(1, 16)

        if enduranceR<6 and enduranceR>0:
            self.endurance=random.randrange(1, 4)

        if enduranceR<=20 and enduranceR>10:
            self.endurance=random.randrange(4, 7)

        if enduranceR<11 and enduranceR>=6:
            self.endurance=random.randrange(7, 10)


        if self.gender==(0):
            print('Gender: Male')

        if self.gender==(1):
            print('Gender: Female')

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
