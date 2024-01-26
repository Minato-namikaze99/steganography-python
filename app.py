from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk 
from PIL import Image, ImageTk 
import os 
from stegano import lsb 


root=Tk()
root.title("Steganography")
root.geometry("700x500+250+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

#the function to show the image
def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image FIle", filetypes=(("PNG File","*.png"), ("JPG File", "*.jpg"),("JPEG File", "*.jpeg"), ("All File", "*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image=img

#the function to save the image
def save():
    secret.save("Hidden.png")

#the function to hide data in the image
def Hide():
    global secret
    message=text1.get(1.0, END)
    secret=lsb.hide(str(filename), message, auto_convert_rgb=True)

#the function to show data in the image
def Show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)



#logo
logo=PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

#headinfg of the app
Label(root, text="CYBERSECURITY", bg="#2d4155", fg="white", font="times 25 bold").place(x=100, y=20)

#first frame, at the left
f=Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl=Label(f, bg="black")
lbl.place(x=40, y=10)

#second frame, at the right
frame2=Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
frame2.place(x=350, y=80)

text1=Text(frame2, font="arial 20", bg="white", fg="black", relief=GROOVE, wrap=WORD) #the input box
text1.place(x=0, y=0, width=320, height=295)

scrollbar1=Scrollbar(frame2) #adding a scrollbar to the typing space and configure it to scroll the view of the input text
scrollbar1.place(x=320, y=0, height=300)
scrollbar1.configure(command=text1.yview)

text1.configure(yscrollcommand=scrollbar1.set) #configuring the text to be scrolled by the scrollbar

#third frame, at the left bottom
frame3=Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

#the open file button
Button(frame3, text="Access Image", width=10, height=2, font="times 14 bold", command=showimage).place(x=20,y=30)

#the save image button
Button(frame3, text="Save Image", width=10, height=2, font="times 14 bold", command=save).place(x=180,y=30)
#the legendary label, LOL
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

#fourthframe, at the right bottom
frame4=Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

#the hide data button
Button(frame4, text="Hide Data", width=10, height=2, font="times 14 bold", command=Hide).place(x=20,y=30)

#the show data button
Button(frame4, text="Show Data", width=10, height=2, font="times 14 bold", command=Show).place(x=180,y=30)
#the legendary label, LOL
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()