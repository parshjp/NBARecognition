import os
import face_recognition
import cv2
from tkinter import *
from tkinter import filedialog, messagebox

tol = 0.6  # tolerance, lower is stricter, higher is lenient
box_thickness, font_thickness = 4, 3
detection_model = "cnn"
kf = []
kn = []


def uploadFile():
    global filename
    filename = filedialog.askopenfilename(title="Select an Image or Video",
                                          filetypes=(("Image/Video Files", ("*.jpg*", "*.mp4*")),
                                                     ("All Files", "*.*"))
                                          )
    if filename.endswith(".jpg"):
        Label(frame, text='Image Uploaded Successfully! Running Recognition...', foreground='green',
              font='TkDefaultFont 10 bold').grid(row=1, pady=10)
    elif filename.endswith(".mp4"):
        Label(frame, text='Video Uploaded Successfully! Running Recognition...', foreground='green',
              font='TkDefaultFont 10 bold').grid(row=1, pady=10)
    else:
        messagebox.showerror("Unknown File.", "File must be .jpg or .mp4!")




root = Tk()
root.title('NBA Recognition')
frame = Frame(root, padx=100, pady=100)
frame.pack()

btnPlay = Button(frame, text='Click to Upload Image (.jpg) or Video (.mp4)', padx=100, font='TkDefaultFont 10 bold',
                 relief='solid', borderwidth=1, width=18, command=uploadFile)
btnPlay.grid(row=0, column=0, padx=5)

root.mainloop()



#image upload, compare for faces(with known files, sentdex) then logo (cascade, 3h yt)
#video upload, compare for faces (sentdex) then logo (aditya pai thon)








