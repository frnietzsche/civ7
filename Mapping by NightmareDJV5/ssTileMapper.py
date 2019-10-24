#darrien varrette
#2019-10-01
#Generate Map


#A = root

import tkinter
import random










class World(object):
    def __init__(self,lengthx,widthy,seedval,numTiles):
        def replace_to_color(input_text,numTiles):
            input_text=str(input_text)
            """
            empty      = X = 0 = "#ffffff"
            
            forest     = ▓ = 1 = "#009600"
            plains     = ░ = 2 = "#00ff00"
            swamp      = S = 3 = "#005500"
            tundra     = ó = 4 = "#cccccc"
            mountions  = A = 5 = "#6699ff"
            grasslands = ▒ = 6 = "#ecfcf0"
            hills      = ∩ = 7 = "#998899"
            """
            #set to color
            input_text=input_text.replace("X","#ffffff")
            
            input_text=input_text.replace("▓","#009600")
            input_text=input_text.replace("░","#00ff00")
            input_text=input_text.replace("S","#005500")
            input_text=input_text.replace("ó","#cccccc")
            input_text=input_text.replace("A","#6699ff")
            input_text=input_text.replace("▒","#ecfcf0")
            input_text=input_text.replace("∩","#998899")
            return input_text
        
        def replacer(input_text,numTiles):
            input_text=str(input_text)
            input_text=input_text.replace("><",",")
            input_text=input_text.replace(">","]")
            input_text=input_text.replace("<","[")
            ###input_text=input_text.replace(" ","")
            """
            empty      = X = 0 = "#ffffff"
            
            forest     = ▓ = 1 = "#009600"
            plains     = ░ = 2 = "#00ff00"
            swamp      = S = 3 = "#005500"
            tundra     = ó = 4 = "#cccccc"
            mountions  = A = 5 = "#6699ff"
            grasslands = ▒ = 6 = "#ecfcf0"
            hills      = ∩ = 7 = "#998899"
            """
            #set to text_id stuff
            input_text=input_text.replace("0","X")
            
            input_text=input_text.replace("1","▓")
            input_text=input_text.replace("2","░")
            input_text=input_text.replace("3","S")
            input_text=input_text.replace("4","ó")
            input_text=input_text.replace("5","A")
            input_text=input_text.replace("6","▒")
            input_text=input_text.replace("7","∩")
            
            input_text = replace_to_color(input_text,numTiles)
            return input_text
        
        
        def generate_land(inx,iny,seed,numTiles):
            x=inx-int(0-self.lengthx/2)
            y=iny-int(0-self.widthy/2)
            import math


            
            sseed=str(seed)
            iseed=int(seed)
            temp1=1
            x0=math.cos(1+x+iseed)
            y0=math.sin(1+y+iseed)

            #make land more logicall
            
            output=((round(0+temp1*x0*y0*iseed))%numTiles)+1  #(x+temp1+1)*(y+temp1+1)%temp1+(y+x)*1
            del math
            return abs(output)
        
        self.lengthx = lengthx
        self.widthy = widthy
        self.seed = seedval
        self.numTiles = numTiles
        tilemaparray_txt=[["?"] * self.widthy] * self.lengthx
        for x in range(self.lengthx):
            temp100 = [0 for i in range(self.widthy)]
            for y in range(self.widthy):
                #finish tile map genorator
                temp100[y]=generate_land(x,y,self.seed,self.numTiles)
                ##print(x,y)
                
            tilemaparray_txt[x]=temp100
        
        
        self.tilemaparray_int = str(tilemaparray_txt)
        print("self.tilemaparray_int",self.tilemaparray_int)
        #replacer
        for y in range(self.widthy):
            for x in range(self.lengthx):
                tilemaparray_txt[x][y] = replacer(tilemaparray_txt[x][y],self.numTiles)
        self.tilemaparray_txt = tilemaparray_txt
        
    def get_list(self):
        return self.tilemaparray_txt



        
#█



"""
def myFun(*argv):  
    for arg in argv:  
        print (arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
"""


"""
seed = 69420
max_x = 64
max_y = 64
numTiles = 7 #8
world = World(max_x,max_y,69420,numTiles)





#windowData




#make it so you can see mouse move around map

windowData = tkinter.Tk()
###put updater here

####fix if Needed \/  \/
ssDrawTileMapping.Draw_map(windowData,seed,max_x,max_y,world.get_list())
#ssMoveMouse4UI.Draw_UI(windowData,screenSizeX,screenSizeY)#add this
#finish UI

#tk.mainloop()
print(world.get_list())

##make it so map isnt always a square

"""








"""
forest     = ▓
plains     = ░
swamp      = S
tundra     = ó
mountions  = A
grasslands = ▒
hills      = ∩
"""
"""
empty      = X = 0 = "#ffffff"

forest     = ▓ = 1 = "#009600"
plains     = ░ = 2 = "#00ff00"
swamp      = S = 3 = "#005500"
tundra     = ó = 4 = "#cccccc"
mountions  = A = 5 = "#6699ff"
grasslands = ▒ = 6 = "#ecfcf0"
hills      = ∩ = 7 = "#998899"
"""
























"""
land tiles

forest ▓
high danger high resources

plains ░
mid danger mid resources small awarness buff

swamp S
mild danger high resources mid speed debuff

tundra ó
high danger low resources

mountions A
mild danger low resources huge industrialisation buff

grasslands ▒
mid danger mild resources

hills ∩
mid danger low resources mild courage buff

"""

"""
159 	9F 	10011111 	- 	ƒ 	 
160 	A0 	10100000 	- 	á 	 
161 	A1 	10100001 	- 	í 	 
162 	A2 	10100010 	- 	ó 	 
163 	A3 	10100011 	- 	ú 	 
164 	A4 	10100100 	- 	ñ 	 
165 	A5 	10100101 	- 	Ñ 	 
166 	A6 	10100110 	- 	ª 	 
167 	A7 	10100111 	- 	º 	 
168 	A8 	10101000 	- 	¿ 	 
169 	A9 	10101001 	- 	⌐ 	 
170 	AA 	10101010 	- 	¬ 	 
171 	AB 	10101011 	- 	½ 	 
172 	AC 	10101100 	- 	¼ 	 
173 	AD 	10101101 	- 	¡ 	 
174 	AE 	10101110 	- 	« 	 
175 	AF 	10101111 	- 	» 	 
176 	B0 	10110000 	- 	░ 	 
177 	B1 	10110001 	- 	▒ 	 
178 	B2 	10110010 	- 	▓ 	 
179 	B3 	10110011 	- 	│ 	 
180 	B4 	10110100 	- 	┤ 	 
181 	B5 	10110101 	- 	╡ 	 
182 	B6 	10110110 	- 	╢ 	 
183 	B7 	10110111 	- 	╖ 	 
184 	B8 	10111000 	- 	╕ 	 
185 	B9 	10111001 	- 	╣ 	 
186 	BA 	10111010 	- 	║ 	 
187 	BB 	10111011 	- 	╗ 	 
188 	BC 	10111100 	- 	╝ 	 
189 	BD 	10111101 	- 	╜ 	 
190 	BE 	10111110 	- 	╛ 	 
191 	BF 	10111111 	- 	┐ 	 
192 	C0 	11000000 	- 	└ 	 
193 	C1 	11000001 	- 	┴ 	 
194 	C2 	11000010 	- 	┬ 	 
195 	C3 	11000011 	- 	├ 	 
196 	C4 	11000100 	- 	─ 	 
197 	C5 	11000101 	- 	┼ 	 
198 	C6 	11000110 	- 	╞ 	 
199 	C7 	11000111 	- 	╟ 	 
200 	C8 	11001000 	- 	╚ 	 
201 	C9 	11001001 	- 	╔ 	 
202 	CA 	11001010 	- 	╩ 	 
203 	CB 	11001011 	- 	╦ 	 
204 	CC 	11001100 	- 	╠ 	 
205 	CD 	11001101 	- 	═ 	 
206 	CE 	11001110 	- 	╬ 	 
207 	CF 	11001111 	- 	╧ 	 
208 	D0 	11010000 	- 	╨ 	 
209 	D1 	11010001 	- 	╤ 	 
210 	D2 	11010010 	- 	╥ 	 
211 	D3 	11010011 	- 	╙ 	 
212 	D4 	11010100 	- 	╘ 	 
213 	D5 	11010101 	- 	╒ 	 
214 	D6 	11010110 	- 	╓ 	 
215 	D7 	11010111 	- 	╫ 	 
216 	D8 	11011000 	- 	╪ 	 
217 	D9 	11011001 	- 	┘ 	 
218 	DA 	11011010 	- 	┌ 	 
219 	DB 	11011011 	- 	█ 	 
220 	DC 	11011100 	- 	▄ 	 
221 	DD 	11011101 	- 	▌ 	 
222 	DE 	11011110 	- 	▐ 	 
223 	DF 	11011111 	- 	▀ 	 
224 	E0 	11100000 	- 	α 	 
225 	E1 	11100001 	- 	ß 	 
226 	E2 	11100010 	- 	Γ 	 
227 	E3 	11100011 	- 	π 	 
228 	E4 	11100100 	- 	Σ 	 
229 	E5 	11100101 	- 	σ 	 
230 	E6 	11100110 	- 	µ 	 
231 	E7 	11100111 	- 	τ 	 
232 	E8 	11101000 	- 	Φ 	 
233 	E9 	11101001 	- 	Θ 	 
234 	EA 	11101010 	- 	Ω 	 
235 	EB 	11101011 	- 	δ 	 
236 	EC 	11101100 	- 	∞ 	 
237 	ED 	11101101 	- 	φ 	 
238 	EE 	11101110 	- 	ε 	 
239 	EF 	11101111 	- 	∩ 	 
240 	F0 	11110000 	- 	≡ 	 
241 	F1 	11110001 	- 	± 	 
242 	F2 	11110010 	- 	≥ 	 
243 	F3 	11110011 	- 	≤ 	 
244 	F4 	11110100 	- 	⌠ 	 
245 	F5 	11110101 	- 	⌡ 	 
246 	F6 	11110110 	- 	÷ 	 
247 	F7 	11110111 	- 	≈ 	 
248 	F8 	11111000 	- 	° 	 
249 	F9 	11111001 	- 	∙ 	 
250 	FA 	11111010 	- 	· 	 
251 	FB 	11111011 	- 	√ 	 
252 	FC 	11111100 	- 	ⁿ 	 
253 	FD 	11111101 	- 	² 	 
254 	FE 	11111110 	- 	■ 	 
255 	FF 	11111111 	-
"""

