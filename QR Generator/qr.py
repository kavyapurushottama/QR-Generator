import qrcode
from pyzbar.pyzbar import  decode
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox 

def createQR(*args):
    data=text_entry.get()
    if data:
        img=qrcode.make(data)
        res_img=img.resize((280,250))
        tkimage= ImageTk.PhotoImage(res_img)
        qrc1.delete("all")
        qrc1.create_image(0,0,anchor=tk.NW,image=tkimage)
        qrc1.image=tkimage
    else:
        messagebox.showwarning("Warning","Enter Data to Generate QR Code")
    

def SaveQR(*args):
    data=text_entry.get()
    if data:
        img=qrcode.make(data)
        res_img=img.resize((280,250))
        path=filedialog.asksaveasfilename(defaultextension=" .png",)
        if path:
            res_img= save(path) 
            messagebox.showinfo("Sucess","QR Code is Saved")
    else:
        messagebox.showwarning("Warning","No Data Entered!!")

root=tk.Tk()
root.title("QR Generator")
root.geometry("300x380")
root.config(bg="white")
root.resizable(0,0)

frame1=tk.Frame(root,bd=2,relief=tk.RAISED)
frame1.place(x=10,y=0,width=280,height=250)
frame2=tk.Frame(root,bd=2,relief=tk.SUNKEN)
frame2.place(x=10,y=260,width=280,height=100)

cover=tk.PhotoImage(file="qrCodeCover.png")
qrc1=tk.Canvas(frame1)
qrc1.bind("<Double-1>",SaveQR)
qrc1.create_image(0,0,anchor=tk.NW,image=cover)
qrc1.image=cover
qrc1.pack(fill=tk.BOTH)

text_entry=ttk.Entry(frame2,width=43,justify=tk.CENTER)
text_entry.bind("<Return>",createQR)
text_entry.place(x=5,y=5)

btn1=ttk.Button(frame2,text="Create",width=10,command=createQR)
btn1.place(x=25,y=50)
btn1=ttk.Button(frame2,text="Save",width=10,command=SaveQR)
btn1.place(x=100,y=50)
btn1=ttk.Button(frame2,text="Exit",width=10,command=root.quit)
btn1.place(x=175,y=50)

root.mainloop()


