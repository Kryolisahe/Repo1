from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

window=Tk()
window.geometry("900x800")
window.title("Image Editor")

img=Image.open("wildlife.png")
img=img.resize((600,600))

def displayImage(img):
    dispImage=ImageTk.PhotoImage(img)
    panel.configure(image=dispImage)
    panel.image=dispImage

def rotate():
    global img
    img=img.rotate(90)
    dispIayImage(img)

def Flip():
    global img
    img=img.transpose(Image.FLIP_LEFT_RIGHT)
    displayImage(img)

def Opening():
    imgName=filedialog.askopenfilename(title="open")
    if imgName:
        img=Image.open(imgName)
        img=img.resize((600,600))
        displayImage(img)

def Save():
    global img
    imgName=filedialog.asksaveasfilename(title="save",defaultextension=".jpg")
    if imgName:
        img.save(imgName)

panel=Label(window,bg="BLACK")
panel.grid(row=0,column=0,columnspan=12,padx=50,pady=50)
displayImage(img)

btnopen=Button(window,text="Open",width=25,command=Opening)
btnopen.grid(row=0,column=1)

btnrotate=Button(window,text="Rotate",width=25,command=rotate)
btnrotate.grid(row=1,column=1)

btnflip=Button(window,text="Flip",width=25,command=Flip)
btnflip.grid(row=2,column=1)

btnsave=Button(window,text="Save",width=25,command=Save)
btnsave.grid(row=3,column=1)

window.mainloop()
