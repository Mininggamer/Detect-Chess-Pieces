from tkinter import *
import cv2 as cv
import numpy as np
import PIL
from PIL import ImageTk, Image
from os import listdir, remove
from sub import  load_image

try:
    for filenmae in listdir('save'):
        remove('save/' + filenmae)
except:
    None

window = Tk()
canvas1 = Canvas(window, width = 1024, height = 684)
canvas1.pack()



def Convert_img(img):
    #img = cv.imread("Save/" + List_name[img_no])

    frame = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = PIL.ImageTk.PhotoImage(image=Image.fromarray(frame))
    return img

List_predict = []
List_img = []
List_filename = []
for filename in listdir('image'):
    List_filename.append(filename)
    img = cv.imread('image/' + filename)
    img = np.array(img)
    frame = img[1:1369, :, :]
    frame = cv.resize(frame, (1024, 684))

    List_predict.append(Convert_img(load_image(frame)))

    img = Convert_img(frame)
    List_img.append(img)

image_container = canvas1.create_image(0,0 ,anchor = NW, image = List_img[0], tag = 'image')
#raw_img = PhotoImage(file = 'image/0b47311f426ff926578c9d738d683e76_jpg.rf.0b55f43ac16aa65c889558d8ea757072.jpg')

btn1 = Button(
    window,
    text='Back',
    font="Times 12",
    command=lambda: Back_Button(),
    state = DISABLED
)
btn2 = Button(
    window,
    text = 'Detect',
    font = "Times 12",
    command = lambda : Detect_Button()
)
btn3 = Button(
    window,
    text = 'Forward',
    font = "Times 12",
    command = lambda : Forward_Button()
)


img_no = 0

def Forward_Button():
    global img_no
    global canvas1
    global btn1
    global btn3
    btn2
    #canvas1.delete("image")
    img_no += 1

    #image_container = canvas1.create_image(0, 0, anchor=NW, image=img, tag='image')

    canvas1.itemconfig(image_container, image = List_img[img_no])
    if img_no == len(List_img)-1:
        btn3.configure(state = DISABLED)
    btn1.configure(state = NORMAL)
    btn2.configure(state=NORMAL)
    #canvas1.configure(image = None)
def Back_Button():
    global img_no
    global canvas1
    global btn1
    global btn3
    global btn2
    #canvas1.delete("image")
    img_no-=1

    canvas1.itemconfig(image_container, image = List_img[img_no])
    if img_no == 0:
        btn1.configure(state = DISABLED)
    btn3.configure(state=NORMAL)
    btn2.configure(state=NORMAL)

def Detect_Button():
    global img_no
    global canvas1
    global btn1
    global btn3
    global btn2
    canvas1.itemconfig(image_container, image = List_predict[img_no])

    if img_no == 0:
        btn1.configure(state = DISABLED)
        btn3.configure(state=NORMAL)
    if img_no == len(List_img)-1:
        btn3.configure(state = DISABLED)
        btn1.configure(state = NORMAL)
    btn2.configure(state = DISABLED)
    return



btn1.pack(side=LEFT, fill=X, expand=True)
btn2.pack(side=LEFT, fill=X, expand=True)
btn3.pack(side=LEFT, fill=X, expand=True)

window.mainloop()
