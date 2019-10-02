#Natural Selection
#Stone Provo

###EVERYONE CAN WALK

##########Stat Chart######################
'''
1= cannot do anything related to said stat, ie: cannot run
2= can do things related to stat, but very poorly ie: more like speedwalking
3= can do things related to stat, but not very well ie: a jogging pace
4= slightly below average ie: can run but is a slow runner
5= average ie: can run
6= slightly above average ie: faster than normal
7= athlete level ie: self explanitory
8= olympic level ie: self explanitory
9= the best you can be ie: Usain Bolt
'''
##########################################

import random
class Person:
    
    def __init__(self):
        
        self.gender=random.randrange(0, 2)
        self.curiosity=random.randrange(1, 10)
        self.aggression=random.randrange(1, 10)
        self.smarts=random.randrange(1, 10)
        self.age=0

        #Male
        if self.gender==(0):
            
            hStart=170
            hR=random.randrange(1, 31)
            self.height=hStart+hR

            if self.height>=170 and self.height>180:
                self.weight=random.randrange(122, 190)

            elif self.height>=180 and self.height>190:
                self.weight=random.randrange(160, 210)

            elif self.height>=190 and self.height>=200:
                self.weight=random.randrange(171, 245)

        #Female
        if self.gender==(1):

            hStart=160
            hR=random.randrange(1, 31)
            self.height=hStart+hR

            if self.height>=160 and self.height>170:
                self.weight=random.randrange(99, 150)

            elif self.height>=170 and self.height>180:
                self.weight=random.randrange(122, 161)

            elif self.height>=180 and self.height>=190:
                self.weight=random.randrange(131, 188)
    
        ########STREGTH##############

        #Female
        if self.gender=(1):
            
            if self.weight<=188 and self.weight>131:
                self.strength=random.randrange(7, 10)

            elif self.weight<=161 and self.weight>122:
                self.strength=random.randrange(4, 7)

            elif self.weight<=150 and self.weight>=99:
                self.strength=random.randrange(1, 4)

        #Male
        if self.gender(0):
            
            if self.weight<=245 and self.weight>171:
                self.strength=random.randrange(7, 10)

            elif self.weight<=210 and self.weight>160:
                self.strength=random.randrange(4, 7)

            elif self.weight<=190 and self.weight>=122:
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

        elif self.strength<=3 and self.strength>0:
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
        if self.gender=(1):
                    
            if self.weight<=160 and self.weight>140:
                consumption1=random.randrange(7, 10)

            elif self.weight<=140 and self.weight>120: #####FIX WEIGHT VALUES AND MAKE A SEPARATE MALE VERSON
                consumption1=random.randrange(4, 7)

            elif self.weight<=120 and self.weight>=100:
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
        print('Speed:',self.speed)
        print('Strength:',self.strength)
        print('Intelligence:',self.smarts)
        print('Curiosity:',self.curiosity)

        print('Stamina:',self.stamina)
        print('Awareness:',self.awareness)
        print('Agression:',self.aggression)
        print('Ingenuity:',self.indust)
        print('Consumption Rate:',self.consumption,' units per cycle')
        

y=1
for x in range(50):
    print('Person #',y)
    i=Person()
    print()
    y=y+1
