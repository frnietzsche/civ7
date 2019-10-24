#darrien varrette
#2019-10-16
#ssMainProgram














import tkinter
import random


#start menu
class App():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('My Title')
        button = tkinter.Button(self.root, text = 'root quit', command=self.quit)
        button.pack()
        self.root.mainloop()
    def quit(self):
        self.root.destroy() 

app = App()










###put updater here
class MainProgram(object):
    def __init__(self,windowData,screenSizeX,screenSizeY,max_x,max_y,pyList):
        
        self.lastMouselist = [1,1]
        
        self.windowData = windowData
        self.windowData.title('MainProgram')
        self.showData = False
        self.screenSizeX = screenSizeX
        self.screenSizeY = screenSizeY
        self.max_x = max_x
        self.max_y = max_y
        self.pyList = pyList
        self.upDateDeleay = 1

        self.maxScreenX = screenSizeX
        self.maxScreenY = screenSizeY

        self.pixelSize = 5


        self.windowDataB = tkinter.Canvas(self.windowData,height=self.screenSizeX,width=self.screenSizeY)
        self.windowDataB.pack()

        
        self.windowData.geometry(str(self.maxScreenX)+"x"+str(self.maxScreenY))
        
        
        


        
        

        

        self.windowData.lift()
        self.windowData.attributes("-topmost", True)
        
        self.windowData.after(self.upDateDeleay, self.update)
        self.windowData.update()
        
        
    
    def update(self):#updates the entire program
        if self.showData==True:print(self.showData)
        def motion(event): #saves mouse x & y to text file
            #adds mouse information to text file to be read later
            file=open("mouse.txt","w+")
            
            x, y = event.x, event.y
            ##############################get mouse clicks
            mouse = [x,y]
            if self.showData==True:print(mouse)
            file.write(str(mouse))
            if self.showData==True:print("file written!")
            file.close()
            self.windowDataB.focus_set()


        
        self.windowData.bind('<Motion>', motion)
        self.windowData.bind('<Enter>', motion)
        def keyboard(event):
            currentKey = event.char
            if currentKey != '??':
                print("pressed", repr(event.char))
            self.windowDataB.focus_set()

        
        
        
        
        
        
        self.windowDataB.bind("<Key>", keyboard)
        self.windowDataB.bind("<Button-1>", keyboard)


        
        
        
        self.mouselist = self.getMouse_XY()
        self.mouse_X = self.mouselist[0]
        self.mouse_Y = self.mouselist[1]
        #this was going to be where it draws the UI Layout
        #ssMoveMouse4UI.
        self.Draw_UI(self.windowData,self.windowDataB,self.screenSizeX,self.screenSizeY,self.mouselist,self.lastMouselist)

        
        
        #map offset x&y
        offsetx=10
        offsety=10
        #ssDrawTileMapping.
        self.draw_Map(offsetx,offsety,self.windowData,self.windowDataB,self.max_x,self.max_y,self.pyList,self.maxScreenX,self.maxScreenY,self.pixelSize,self.mouselist,self.lastMouselist)


        
        self.lastMouselist = self.getMouse_XY()

        

        
        self.windowData.after(self.upDateDeleay, self.update)


        
        
        
    def readMouseFile(self):
        #####print("at: readMouseFile")
        ##get mouse data
        file=open("mouse.txt","r")
        if self.showData==True:print("file read")
        mouse = file.read()
        if self.showData==True:print(len(mouse))
        file.close()
        if self.showData==True:print("out mouse",mouse)
        return mouse
    
    def getMouse_XY(self):
        #reads mouse input file to get mouse input
        mouse = 0
        mouse = self.readMouseFile()
        if self.showData==True:print(mouse)
        mouse = mouse.replace("[","")
        mouse = mouse.replace("]","")
        mouse = mouse.replace(", ","|")
        for i in range(len(mouse)):
            if mouse[i]=="|":
                middle = i
        mousex = mouse[:middle]
        mousey = mouse[middle+1:]
        if self.showData==True:print(middle,mousex,mousey)
        return [int(mousex),int(mousey)]

        
        #LATER MAKE MOUSE AN ARRAY

    def draw_Map(self,xpos,ypos,windowData,windowDataB,max_x,max_y,pyList,maxScreenX,maxScreenY,pixelSize,mouseData,lastMouseArray=[0,0]):
        def create_pixel(B,x,y,pixelSize,setColor):
            #[a0,a0,a1,a1]
            x0 = x*pixelSize+xpos
            y0 = y*pixelSize+ypos
            x1 = x0+pixelSize
            y1 = y0+pixelSize
            B.create_rectangle(x0, y0, x1, y1,outline="#000000", fill=setColor)
            del x0,x1,y0,y1
        showData = False
        windowData = windowData
        if 'lastpyList' not in globals():
            global lastpyList
            lastpyList = 0
            global lastMouse
            lastMouse = []
        B = windowDataB
        if showData==True:print("at: update_Map_Screen")
        mouseColor = "#FF0000"
        #mouse pos relative to map pixels \/
        mouseX = int((mouseData[0])/pixelSize)-int(xpos/pixelSize)
        mouseY = int((mouseData[1])/pixelSize)-int(ypos/pixelSize)
        lastmouseX = int((lastMouseArray[0])/pixelSize)-int(xpos/pixelSize)
        lastmouseY = int((lastMouseArray[1])/pixelSize)-int(ypos/pixelSize)
        if lastpyList != pyList:
            for x in range(max_x):
                for y in range(max_y):
                    fillColor = pyList[x][y]
                    posarray = [x,y]
                    setColor = fillColor
                    create_pixel(B,x,y,pixelSize,setColor)
                    if [mouseX,mouseY]==[x,y]:
                        setColor = mouseColor
                        create_pixel(B,x,y,pixelSize,setColor)
                
                    ##add if clicked and if clicked then zoom in on terrain detail
            lastpyList = pyList
        #restes red pixels
        if [mouseX,mouseY]!=[lastmouseX,lastmouseY]:
            setColor = mouseColor
            create_pixel(B,mouseX,mouseY,pixelSize,setColor)
            lastx,lasty = lastmouseX,lastmouseY
            x0,y0 = lastx,lasty
            if lastx>=max_x:x0=max_x
            if lasty>=max_y:y0=max_y
            if lastx<=0:x0=0
            if lasty<=0:y0=0
            if x0<max_x and y0<max_y:create_pixel(B,x0,y0,pixelSize,pyList[x0][y0])
        #keep current pixel red
        if [mouseX,mouseY]==[lastmouseX,lastmouseY]:
            setColor = mouseColor
            create_pixel(B,mouseX,mouseY,pixelSize,setColor)
    
    #finish UI
    class Draw_UI(object):
        def __init__(self,windowData,windowDataB,max_x,max_y,mouseArray,lastMouseArray):
            self.showData = False
            self.upDateDeleay = 1
            #add self.lastMouseArray
            self.windowData = windowData
            self.mouselist = mouseArray
            self.max_x = max_x
            self.max_y = max_y
            self.maxScreenX = self.max_x
            self.maxScreenY = self.max_y
            self.B = windowDataB
            
            self.mouse_X = self.mouselist[0]
            self.mouse_Y = self.mouselist[1]
            self.update_UI_Screen(self.mouse_X,self.mouse_Y)
        def update_UI_Screen(self,mouse_x,mouse_y):
            #####print("at: update_UI_Screen")
            a0 = self.mouse_X;b0 = self.mouse_Y
            self.B.create_line(a0,b0,a0+1,b0+1,fill="#FF0000")
            for a in range(self.max_x):
                for b in range(self.max_y):
                    mouseColor = "#000000";posarray = [a,b]
    
    








#this make a sudo random map
import ssTileMapper
seed = 69420
max_x = 64
max_y = 64
numTiles = 7 #8
import ssTileMapper
world = ssTileMapper.World(max_x,max_y,69420,numTiles)
del ssTileMapper






#windowData
screenSizeX = 400
screenSizeY = 400
windowData = tkinter.Tk()
pyList = world.get_list()
MainProgram(windowData,screenSizeX,screenSizeY,max_x,max_y,pyList)
print(world.get_list())

##make it so map isnt always a square













