#Person Generator
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
    
    def __init__(self, gender='None'):

        self.gender=gender
        gU=gender.upper()
        
        if self.gender==('None'):
            gender=random.randrange(0, 2)

        self.health=10
        self.curiosity=random.randrange(1, 10)
        self.aggression=random.randrange(1, 10)
        self.smarts=random.randrange(1, 10)
        self.age=0
        self.weight=0
        self.height=0
        self.strength=0
        self.speed=0
        stamina1=0
        stamina2=0
        self.stamina=0
        self.awareness=0
        consumption1=0
        comdumption2=0
        self.indust=0
        self.consumption=0


        #########WEIGHT & HEIGHT########
        
        #Male
        if gU==('MALE') or gender==(0):
            
            hStart=170
            hR=random.randrange(1, 31)
            self.height=hStart+hR

            if self.height>=170 and self.height<180:
                self.weight=random.randrange(122, 160)

            elif self.height>=180 and self.height<190:
                self.weight=random.randrange(160, 171)

            elif self.height>=190 and self.height<=200:
                self.weight=random.randrange(171, 245)        

        #Female
        if gU==('FEMALE') or gender==(1):

            hStart=160
            hR=random.randrange(1, 31)
            self.height=hStart+hR

            if self.height>=160 and self.height<170:
                self.weight=random.randrange(99, 122)

            elif self.height>=170 and self.height<180:
                self.weight=random.randrange(122, 131)

            elif self.height>=180 and self.height<=190:
                self.weight=random.randrange(131, 188)

        
    
        ########STREGTH##############

        #Female
        if gU==('FEMALE') or gender==(1):
            
            if self.weight<=188 and self.weight>131:
                self.strength=random.randrange(7, 10)

            elif self.weight<=131 and self.weight>122:
                self.strength=random.randrange(4, 7)

            elif self.weight<=122 and self.weight>=99:
                self.strength=random.randrange(1, 4)

        #Male
        if gU==('MALE') or gender==(0):
            
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
        if gU==('FEMALE') or gender==(1):
                    
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
        if gU==('MALE') or gender==(0):

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
        print('Health:',self.health)
        if gU==('FEMALE') or gender==(1):
            print('Gender: Female')

        if gU==('MALE') or gender==(0):
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


    ######TRAVEL#######
    def travel(self):

        if self.curiosity<=9 and self.curiosity>6:

            if self.stamina<=9 and self.stamina>6:
                        travelDis1=3

            if self.stamina<=6 and self.stamina>3:
                        travelDis1=2

            if self.stamina<=3 and self.stamina>=0:
                        travelDis1=1

            if self.awareness<=9 and self.awareness>6:
                        travelDis2=3

            if self.awareness<=6 and self.awareness>3:
                        travelDis2=2

            if self.awareness<=3 and self.awareness>=0:
                        travelDis2=1

        if self.curiosity<=6 and self.curiosity>3:

            if self.stamina<=9 and self.stamina>6:
                        travelDis1=2

            if self.stamina<=6 and self.stamina>3:
                        travelDis1=1

            if self.stamina<=3 and self.stamina>=0:
                        travelDis1=0

            if self.awareness<=9 and self.awareness>6:
                        travelDis2=2

            if self.awareness<=6 and self.awareness>3:
                        travelDis2=1

            if self.awareness<=3 and self.awareness>=0:
                        travelDis2=0

        if self. curiosity<=3 and self.curiosity>=0:

            if self.stamina<=9 and self.stamina>6:
                        travelDis1=1

            if self.stamina<=6 and self.stamina>3:
                        travelDis1=0

            if self.stamina<=3 and self.stamina>=0:
                        travelDis1=0

            if self.awareness<=9 and self.awareness>6:
                        travelDis2=1

            if self.awareness<=6 and self.awareness>3:
                        travelDis2=0

            if self.awareness<=3 and self.awareness>=0:
                        travelDis2=0
                        
        travelDisAve=travelDis1+travelDis2
        travelDisTot=travelDisAve/2
        self.travelDis=int(round(travelDisTot, 0))

        print("Person moved",self.travelDis,'Tiles')
        #########DONE TRAVEL#############

    ######CRAFTING#####
    def craft(self):
        

        if self.indust==9:
            craftR=random.randrange(1, 100)

            if craftR<=90:
                self.craft=True

            else:
                self.craft=False

        if self.indust==8:
            craftR=random.randrange(1, 100)

            if craftR<=80:
                self.craft=True

            else:
                self.craft=False

        if self.indust==7:
            craftR=random.randrange(1, 100)

            if craftR<=70:
                self.craft=True

            else:
                self.craft=False

        if self.indust==6:
            craftR=random.randrange(1, 100)

            if craftR<=60:
                self.craft=True

            else:
                self.craft=False

        if self.indust==5:
            craftR=random.randrange(1, 100)

            if craftR<=50:
                self.craft=True

            else:
                self.craft=False

        if self.indust==4:
            craftR=random.randrange(1, 100)

            if craftR<=40:
                self.craft=True

            else:
                self.craft=False

        if self.indust==3:
            craftR=random.randrange(1, 100)

            if craftR<=30:
                self.craft=True

            else:
                self.craft=False

        if self.indust==2:
            craftR=random.randrange(1, 100)

            if craftR<=20:
                self.craft=True

            else:
                self.craft=False

        if self.indust==1:
            craftR=random.randrange(1, 100)

            if craftR<=10:
                self.craft=True

            else:
                self.craft=False

        if self.indust==0:
            craftR=random.randrange(1, 100)

            if craftR<=5:
                self.craft=True

            else:
                self.craft=False
                
        if self.craft==True:
            print("Person was able to craft something!")
            c=1
            
        if self.craft==False:
            print("Person was not able to craft something")
            c=0
            
        #####END OF CRAFTING#######
    
    ###BEAST ATTACK#####
    def beastAtk(self):
        sg=1

        
        if self.strength<=9 and self.strength>6 or self.speed<=9 and self.speed>6:
            if sg==1: 
                beastR=random.randrange(1, 100)
                sg=sg+1

                #Surviving unscathed
                if beastR>33 or self.craft==True:
                    damage=0
                      
                #Taking little damage but probably survives
                elif beastR<=33 and self.craft==False:
                    damage=random.randrange(1, 3)
                    self.health=self.health-damage
            
        if self.strength<=6 and self.strength>3 or self.speed<=6 and self.speed>3:
            if sg==1:
                beastR=random.randrange(1, 100)
                sg=sg+1
                
                #Survivng unscathed
                if beastR<=100 and beastR>75 or self.craft==True:
                    damage=0
                
                #Taking some damage but probably survives
                elif beastR<=75 and beastR>25 and self.craft==False:
                    damage=random.randrange(1, 5)
                    self.health=self.health-damage

                #Taking critical damage, could be killed
                elif beastR<=25 and self.craft==False:
                    damage=random.randrange(5, 11)
                    self.health=self.health-damage
                
        if self.strength<=3 and self.strength>0 or self.speed<=3 and self.speed>0:
            if sg==1:
                sg=sg+1
                beastR=random.randrange(1, 100)

                #Whatever was crafted saved them and they escaped unharmed
                if self.craft==True:
                    damage=0
                
                #Taking big damage, will most likely survive
                elif beastR>50 and self.craft==False:
                    damage=random.randrange(1, 7)
                    self.health=self.health-damage
                    
                #Taking critical damage, will likely die
                elif beastR<=50 and self.craft==False:
                    damage=random.randrange(7, 11)
                    self.health=self.health-damage
                
        print('Person took',damage,'points of damage')
                
        if self.health<=0:
            print('Person has died')

        else:
            print('Person now has',self.health,'points of health')
        


#Envoirmental danger other than animals?
#finding a mate?
'''
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
'''
i=Person()
print()
i.beastAtk()
