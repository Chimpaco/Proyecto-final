"""-------Imports------"""


import tkinter as tk 
from tkinter import filedialog
from PIL import Image, ImageTk


"""-------Funciones de editor de imagenes-------"""


def open():
    global root_img
    global image_editable
    global image_edited
    global image_label
    root_img = filedialog.askopenfilename(initialdir="Ejercicios/image" ,title="Select a file",filetypes=(("files jpeg","*.jpeg"),("files jpg","*.jpg"),("files png","*.png")))
    image_editable =Image.open(root_img)
    image_edited = ImageTk.PhotoImage(image_editable)
    image_label =tk.Label(frame_img,image=image_edited,width=900, height=700,bg="#BDC3C7")
    image_label.grid(column=2,row=2)
    image_label.grid_propagate(False)

def rotate_img_rigth():
    global image_editable
    global image_edited
    image_edit_rot_r = image_editable
    image_edit_rot_r = image_edit_rot_r.rotate(90,expand=True)
    image_edited = ImageTk.PhotoImage(image_edit_rot_r)
    image_label.configure(image=image_edited)

def rotate_img_left():
    global image_editable
    global image_edited
    image_edit_rot_l = image_editable
    image_edit_rot_l = image_edit_rot_l.rotate(-90,expand=True)
    image_edited = ImageTk.PhotoImage(image_edit_rot_l)
    image_label.configure(image=image_edited)

def save():
    global image_editable
    global image_edited
    image_editable = image_edited
    image_edit_save = filedialog.asksaveasfilename(initialdir="Ejercicios/image" ,title="Select a folder",filetypes=(("files jpeg","*.jpeg"),))
    image_editable =image_edited.save(image_edit_save)


"""-------Ventana Principal-------"""


win_edit = tk.Tk()
win_edit.geometry("900x800")
win_edit.title("Image Editor 1.0")

"""-------Frames-------"""

frame_top = tk.Frame(win_edit,width=900, height=30,bg="#D6DBDF",)
frame_top.grid(column=1,row=1,columnspan=4,)

frame_img = tk.Frame(win_edit,width=900, height=700,bg="#BDC3C7")
frame_img.grid(column=1,row=2,columnspan=4)
frame_img.grid_propagate(False)


"""-------Textos-------"""


text_h1 = tk.Label(frame_top, text="Image Editor",font=20)
text_h1.grid(column=2,row=1)
text_h1.grid_propagate(False)


"""-------Botones-------"""


btn_up = tk.Button (win_edit,text="Upload",font="Arial, 20" ,bg="#21618C", command=open)
btn_up.grid(column=1,row=5)

btn_rr = tk.Button (win_edit,text="rotate right",font="Arial, 20" , bg="#21618C", command=rotate_img_rigth)
btn_rr.grid(column=2,row=5)

btn_rl = tk.Button (win_edit,text="rotate left",font="Arial, 20" , bg="#21618C", command=rotate_img_left)
btn_rl.grid(column=3,row=5)

btn_sv = tk.Button (win_edit,text="Save",font="Arial, 20" , bg="#21618C", command=save)
btn_sv.grid(column=4,row=5)

btn_up.bind('<Enter>', lambda e: e.widget.config(bg="#198CD8"))
btn_up.bind('<Leave>', lambda e: e.widget.config(bg="#21618C"))

btn_rr.bind('<Enter>', lambda e: e.widget.config(bg="#198CD8"))
btn_rr.bind('<Leave>', lambda e: e.widget.config(bg="#21618C"))

btn_rl.bind('<Enter>', lambda e: e.widget.config(bg="#198CD8"))
btn_rl.bind('<Leave>', lambda e: e.widget.config(bg="#21618C"))

btn_sv.bind('<Enter>', lambda e: e.widget.config(bg="#198CD8"))
btn_sv.bind('<Leave>', lambda e: e.widget.config(bg="#21618C"))


win_edit.mainloop()