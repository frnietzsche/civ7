#NaturalSelectionReproduce
#Max Moverley
#ICS4U
#10/2/19
import random
from NaturalSelectionCharCreate import Person

class Child(Person):
    def __init__(self, curiosity, aggression, smarts, height, gender, mom, dad):
        self.curiosity=curiosity
        self.aggression=aggression
        self.smarts=smarts
        self.height=height
        self.age=0
        self.weight=0
        self.strength=0
        self.speed=0
        stamina1=0
        stamina2=0
        self.stamina=0
        self.awareness=0
        consumption1=0
        consumption2=0
        self.indust=0
        self.consumption=0
        self.gender=gender
        self.mom=mom
        self.dad=dad

        #########WEIGHT & HEIGHT########
        
        #Male
        if self.gender==(0):
            
            if self.height>=170 and self.height<180:
                self.weight=random.randrange(122, 160)

            elif self.height>=180 and self.height<190:
                self.weight=random.randrange(160, 171)

            elif self.height>=190 and self.height<=200:
                self.weight=random.randrange(171, 245)        

        #Female
        if self.gender==(1):

            if self.height>=160 and self.height<170:
                self.weight=random.randrange(99, 122)

            elif self.height>=170 and self.height<180:
                self.weight=random.randrange(122, 131)

            elif self.height>=180 and self.height<=190:
                self.weight=random.randrange(131, 188)

        
    
        ########STREGTH##############

        #Female
        if self.gender==(1):
            
            if self.weight<=188 and self.weight>131:
                self.strength=random.randrange(7, 10)

            elif self.weight<=131 and self.weight>122:
                self.strength=random.randrange(4, 7)

            elif self.weight<=122 and self.weight>=99:
                self.strength=random.randrange(1, 4)

        #Male
        if self.gender==(0):
            
            if self.weight<=245 and self.weight>171:
                self.strength=random.randrange(7, 10)

            elif self.weight<=171 and self.weight>160:
                self.strength=random.randrange(4, 7)

            elif self.weight<=160 and self.weight>=122:
                self.strength=random.randrange(1, 4)

        ########SPEED AND AWARENESS##
        if self.height<=200 and self.height>185:
            self.speed=random.randrange(7, 10)
            self.awareness=random.randrange(7, 10)

        elif self.height<=185 and self.height>175:
            self.speed=random.randrange(4, 7)
            self.awareness=random.randrange(4, 7)

        elif self.height<=175 and self.height>=160:
            self.speed=random.randrange(1, 4)
            self.awareness=random.randrange(1, 4)

        ########STAMINA##############
        if self.speed<=9 and self.speed>6:
            stamina1=random.randrange(7, 10)

        elif self.speed<=6 and self.speed>3:
            stamina1=random.randrange(4, 7)

        elif self.speed<=3 and self.speed>0:
            stamina1=random.randrange(1, 4)

        if self.strength<=9 and self.strength>6:
            stamina2=random.randrange(7, 10)

        elif self.strength<=6 and self.strength>3:
            stamina2=random.randrange(4, 7)

        elif self.strength<=3 and self.strength>=0:
            stamina2=random.randrange(1, 4)

        staminaAve=stamina1+stamina2
        staminaTot=staminaAve/2
        self.stamina=int(round(staminaTot, 0))
        
        ########INDUST################
        if self.smarts<=9 and self.smarts>6 or self.curiosity<=9 and self.curiosity>6:
            self.indust=random.randrange(7, 10)

        elif self.smarts<=6 and self.smarts>3 or self.curiosity<=6 and self.curiosity>3:
            self.indust=random.randrange(4, 7)

        elif self.smarts<=3 and self.smarts>0 or self.curiosity<=3 and self.curiosity>0:
            self.indust=random.randrange(0, 4)

        ########CONSUMPTION###########

        #Female
        if self.gender==(1):
                    
            if self.weight<=188 and self.weight>131:
                consumption1=random.randrange(7, 10)

            elif self.weight<=131 and self.weight>122:
                consumption1=random.randrange(4, 7)

            elif self.weight<=122 and self.weight>=99:
                consumption1=random.randrange(1, 4)

            if self.stamina<=9 and self.stamina>6:
                consumption2=random.randrange(7, 10)

            elif self.stamina<=6 and self.stamina>3:
                consumption2=random.randrange(4, 7)

            elif self.stamina<=3 and self.stamina>=0:
                consumption2=random.randrange(1, 4)

            consumptionAve=consumption1+consumption2
            consumptionTot=consumptionAve/2
            self.consumption=int(round(consumptionTot, 0))

        #Male
        if self.gender==(0):

            if self.weight<=245 and self.weight>171:
                consumption1=random.randrange(7, 10)

            elif self.weight<=171 and self.weight>160:
                consumption1=random.randrange(4, 7)

            elif self.weight<=160 and self.weight>=122:
                consumption1=random.randrange(1, 4)

            if self.stamina<=9 and self.stamina>6:
                consumption2=random.randrange(7, 10)

            elif self.stamina<=6 and self.stamina>3:
                consumption2=random.randrange(4, 7)

            elif self.stamina<=3 and self.stamina>0:
                consumption2=random.randrange(1, 4)

            consumptionAve=consumption1+consumption2
            consumptionTot=consumptionAve/2
            self.consumption=int(round(consumptionTot, 0))

        print('Weight:',self.weight,'lbs')
        print('Height:',self.height,'cm')
        
        if self.gender==(1):
            print('Gender: Female')

        if self.gender==(0):
            print('Gender: Male')

        print('Speed:',self.speed)
        print('Strength:',self.strength)
        print('Intelligence:',self.smarts)
        print('Curiosity:',self.curiosity)

        print('Stamina:',self.stamina)
        print('Awareness:',self.awareness)
        print('Agression:',self.aggression)
        print('Ingenuity:',self.indust)
        print('Consumption Rate:',self.consumption,' units per cycle')
        
def reproduce(parent1, parent2):
    gender=random.randrange(0,2)
    
    if parent1.curiosity-parent2.curiosity>=0:
        curiosity=random.randrange(parent2.curiosity-1, parent1.curiosity+2)

    else:
        curiosity=random.randrange(parent1.curiosity-1, parent2.curiosity+2)

    if curiosity==10:
        curiosity-=1

    if curiosity==0:
        curiosity+=1

    if parent1.aggression-parent2.aggression>=0:
        aggression=random.randrange(parent2.aggression-1, parent1.aggression+2)

    else:
        aggression=random.randrange(parent1.aggression-1, parent2.aggression+2)

    if aggression==10:
        aggression-=1

    if aggression==0:
        aggression+=1

    if parent1.smarts-parent2.smarts>=0:
        smarts=random.randrange(parent2.smarts-1, parent1.smarts+2)

    else:
        smarts=random.randrange(parent1.smarts-1, parent2.smarts+2)

    if smarts==10:
        smarts-=1

    if smarts==0:
        smarts+=1

    if gender==0:
        if parent1.height-parent2.height>=0:
            height=random.randrange(parent2.height-2, parent1.height+10)

        else:
            height=random.randrange(parent1.height-2, parent2.height+10)

    else:
        if parent1.height-parent2.height>=0:
            height=random.randrange(parent2.height-8, parent1.height+5)

        else:
            height=random.randrange(parent1.height-8, parent2.height+5)

    

    return Child(curiosity, aggression, smarts, height, gender)

jeff=Person()
print()
mary=Person()
print()

if jeff.gender+mary.gender==1:
    jerry=reproduce(mary, jeff)
