#Slide show
from tkinter import *
from PIL import Image, ImageTk
from time import sleep
print('starting slide show')
w=0
h=0
  
 
class Window(Frame):
    def __init__(self ,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title('Slide show')
        self.pack(fill =BOTH, expand =1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        slideshow =Menu(menu)
        slideshow.add_command(label ='slide1', command =self.showimg1)
        #slideshow.add_command(label ='slideshowing_GIF', command =self.showGIF)
        slideshow.add_command(label ='slide2', command =self.showimg2)
        slideshow.add_command(label ='slide3', command =self.showimg3)
        menu.add_cascade(label ='Slideshow', menu=slideshow)
    
    def showimg1(self):    
        load = Image.open('Itsimagefile.png')
        print(load.filename)
        render = ImageTk.PhotoImage(load)
        img = Label(self,image=render)
        img.image= render
        img.place(x=0,y=0)
        w = render.width()
        h = render.height()
        #print(w) #print(h)
        
        #print(w,h)
        #print(load.format)
        #print(load.filename)
        
    def showimg2(self):
        load = Image.open('New-Technology-Innovation-600x400 - Copy.png')
        print(load.filename)
        render = ImageTk.PhotoImage(load)
        img = Label(self,image=render)
        img.image= render
        img.place(x=0,y=0)
        w = render.width()
        h = render.height()
        #print(w) #print(h)
        #root.geometry("%dx%d" % (w,h))
        #print(w,h)
        #print(load.format)
        #print(load.filename)
        
    def showimg3(self):
        load = Image.open('Capture.PNG')
        print(load.filename)
        render = ImageTk.PhotoImage(load)
        img = Label(self,image=render)
        img.image= render
        img.place(x=0,y=0)
        w = render.width()
        h = render.height()
        #print(w) #print(h)
        #root.geometry("%dx%d" % (w,h))
        #print(w,h)
        #print(load.format)
        #print(load.filename)
##    def showGIF(self):
##        self.showimg2()
##        sleep(2)
##        self.showimg3()
##        sleep(2)
##        self.showimg1()
##        sleep(2)       
  
        
root =Tk()
app = Window(root)
#root.geometry("%dx%d" % (w,h))
root.geometry('400x300')
root.mainloop()
# slide show
print('slide show done')
