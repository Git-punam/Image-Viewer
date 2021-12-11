from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image viewer application using python")
root.resizable(0, 0)

# create frame
frame=Frame(root, width=600, height=500, bg='white', relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)

# create thumbanials of all images
img1 = Image.open('images\white_image1.png')
img1.thumbnail((550, 450))
img2 = Image.open('images\white_image2.png')
img2.thumbnail((550, 450))
img3 = Image.open('images\white_image3.png')
img3.thumbnail((550, 450))
img4 = Image.open('images\white_image4.png')
img4.thumbnail((550, 450))
img5 = Image.open('images\white_image5.jpg')
img5.thumbnail((550, 450))
img6 = Image.open('images\yellow_flower5.jpg')
img6.thumbnail((550, 450))
img7 = Image.open('images\yellow_flower4.jpg')
img7.thumbnail((550, 450))
img8 = Image.open('images\yellow_flower3.jpg')
img8.thumbnail((550, 450))
img9 = Image.open('images\yellow_flower2.jpg')
img9.thumbnail((550, 450))
img10 = Image.open('images\yellow_flower1.jpg')
img10.thumbnail((550, 450))
img11 = Image.open('images\Blue_flower1.jpg')
img11.thumbnail((550, 450))
img12 = Image.open('images\Blue_flower2.jpg')
img12.thumbnail((550, 450))
img13 = Image.open('images\Blue_flower3.jpg')
img13.thumbnail((550, 450))
img14 = Image.open('images\Blue_flower4.jpg')
img14.thumbnail((550, 450))
img15 = Image.open('images\Blue_flower5.jpg')
img15.thumbnail((550, 450))
img16 = Image.open('images\Red_flower1.jpg')
img16.thumbnail((550, 450))
img17 = Image.open('images\Red_flower2.jpg')
img17.thumbnail((550, 450))
img18 = Image.open('images\Red_flower3.jpg')
img18.thumbnail((550, 450))
img19 = Image.open('images\Red_flower4.jpg')
img19.thumbnail((550, 450))
img20 = Image.open('images\Red_flower5.jpg')
img20.thumbnail((550, 450))



# open images to use with labels
image1 = ImageTk.PhotoImage(img1)
image2 = ImageTk.PhotoImage(img2)
image3 = ImageTk.PhotoImage(img3)
image4 = ImageTk.PhotoImage(img4)
image5 = ImageTk.PhotoImage(img5)
image6 = ImageTk.PhotoImage(img6)
image7 = ImageTk.PhotoImage(img7)
image8 = ImageTk.PhotoImage(img8)
image9 = ImageTk.PhotoImage(img9)
image10 = ImageTk.PhotoImage(img10)
image11 = ImageTk.PhotoImage(img11)
image12 = ImageTk.PhotoImage(img12)
image13 = ImageTk.PhotoImage(img13)
image14 = ImageTk.PhotoImage(img14)
image15 = ImageTk.PhotoImage(img15)
image16 = ImageTk.PhotoImage(img16)
image17 = ImageTk.PhotoImage(img17)
image18 = ImageTk.PhotoImage(img18)
image19 = ImageTk.PhotoImage(img19)
image20 = ImageTk.PhotoImage(img20)

# create list of images
images = [image1, image2, image3, image4, image5,image6,image7,image8,image9,image10,image11,image12,image13,image14,image15,image16,image17,image18,image19,image20]

# configure the image to the Label in frame
i = 0
image_label = Label(frame, image=images[i])
image_label.pack()

# create functions to display
# previous an next images
def previous():
    global i
    i = i - 1
    try:
        image_label.config(image=images[i])
    except:
        i = 0
        previous()
def next():
    global i
    i = i + 1
    try:
        image_label.config(image=images[i])
    except:
        i = -1
        next()

# create buttons
btn1 = Button(root, text="Previous", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=previous)
btn1.pack(side=LEFT, padx=60, pady=5)
btn3 = Button(root, text="Exit", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn3.pack(side=LEFT, padx=60, pady=5)
btn2 = Button(root, text="Next", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=next)
btn2.pack(side=LEFT, padx=60, pady=5)

root.mainloop()