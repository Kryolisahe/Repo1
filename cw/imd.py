
from tkinter import *
from PIL import ImageTk, Image,ImageOps,ImageEnhance
from tkinter import filedialog

mainWin = Tk()
mainWin.geometry("900x700")
mainWin.title("The wild world")

img = Image.open("wildlife.png")
img = img.resize((600, 600))

def displayImage(img):
    dispImage = ImageTk.PhotoImage(img)
    panel.configure(image=dispImage)
    panel.image=dispImage





def rotate():
    global img
    img = img.rotate(90)
    displayImage(img)

def Flip():
    global img
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    displayImage(img)

def OpenImg():
    global img
    imgName=filedialog.askopenfilename(title='open')
    if imgName:
        img = Image.open(imgName)
        img = img.resize((600, 600))
        displayImage(img)

def Save():
    global img    
    imgName=filedialog.asksaveasfilename(title='save',defaultextension='.jpg')
    if imgName:        
        img.save(imgName)


panel = Label(mainWin,bg="BLACK")
panel.grid(row=0,column=0,rowspan=12,padx=50,pady=50)
displayImage(img)

btnOpen = Button(mainWin, text='Open',width=25,command=OpenImg)
btnOpen.grid(row=0,column=1)

btnRotate = Button(mainWin, text='Rotate',width=25,command=rotate)
btnRotate.grid(row=1,column=1)

btnFlip = Button(mainWin, text='Flip',width=25,command=Flip)
btnFlip.grid(row=2,column=1)

btnSave = Button(mainWin, text='Save',width=25,command=Save)
btnSave.grid(row=3,column=1)

def GrayScale():
    global img
    img=img.convert('L')
    displayImage(img)

def Invert():
    global img
    img=ImageOps.invert(img)
    displayImage(img)

def Contrast():
    global img
    enhancer=ImageEnhance.Contrast(img)
    img=enhancer.enhance(2)
    displayImage(img)

def Brightness():
    global img
    enhancer=ImageEnhance.Brightness(img)
    img=enhancer.enhance(2)
    displayImage(img)

def Sharpness():
    global img
    enhancer=ImageEnhance.Sharpness(img)
    img=enhancer.enhance(2)
    displayImage(img)

graybtn=Button(mainWin,text="GrayScale",width=25,command=GrayScale)
graybtn.grid(row=4,column=1)

invertbtn=Button(mainWin,text="Invert",width=25,command=Invert)
invertbtn.grid(row=5,column=1)

brightbtn=Button(mainWin,text="Brightness",width=25,command=Brightness)
brightbtn.grid(row=6,column=1)

sharpbtn=Button(mainWin,text="Sharpness",width=25,command=Sharpness)
sharpbtn.grid(row=7,column=1)

contrastbtn=Button(mainWin,text="Contrast",width=25,command=Contrast)
contrastbtn.grid(row=8,column=1)

mainWin.mainloop()
