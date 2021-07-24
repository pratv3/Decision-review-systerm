# www.pratv3python.blogspot.com/ can get the code
from tkinter import *
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import time
import imutils
# given video
stream=cv2.VideoCapture("Nm.mp4")
# width and height of screen
SET_WIDTH=650
SET_HEIGHT=368
# functions to run code
def play(speed):
    print(speed)
     
    #play reverse
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    grabbed,frame =stream.read()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=  PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0 ,image=frame ,anchor=NW)
      
def out ():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("player is out")
def notout():
    thread=threading.Thread(target=pending,args=("notout",))
    thread.daemon=1
    thread.start()
    print("player is not out")
def pending(decision):
    # decision pending
    frame=cv2.cvtColor(cv2.imread("hacker3.jpg"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=NW)
    time.sleep(1)
    # sponsor image
    frame=cv2.cvtColor(cv2.imread("sponsor.jpg"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=NW)
    time.sleep(1.5)
    # out or notout
    if decision=="out":
        dimg="notout.jpg"
    elif decision=="notout":
        dimg="out.jpg"
    frame=cv2.cvtColor(cv2.imread(dimg),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=NW)
# tkinter gui starts here
r=Tk()
r.title("DRS review systerm")
cv_img=cv2.cvtColor(cv2.imread("gameover.png"),cv2.COLOR_BGR2RGB)
canvas=Canvas(r,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=NW,image=photo)
canvas.pack()
#buttons to control play back
btn=Button(r,text="<<previous (fast)",width=50, command=partial(play,-25))
btn.pack()
btn=Button(r,text="<<previous (slow)",width=50,command=partial(play,-2))
btn.pack()
btn=Button(r,text=">>forward (fast)",width=50,command=partial(play,25))
btn.pack()
btn=Button(r,text=">>forward (slow)",width=50,command=partial(play,2))
btn.pack()
btn=Button(r,text="OUT",width=50,command=out)
btn.pack()
btn=Button(r,text="NOT OUT",width=50,command=notout)
btn.pack()

r.mainloop()
