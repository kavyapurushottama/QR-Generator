import qrcode
from pyzbar.pyzbar import  decode
from PIL import Image
# import tkinter as tk
# from tkinter import *
# from tkinter import ttk, filedialog, messagebox 



q1=qrcode.make("Hello my name is Kavya")
q3=qrcode.make("https://i.pinimg.com/originals/6d/cd/94/6dcd94c7c4bf4800648ef7cbe0113c33.gif")
q2=qrcode.make("https://www.youtube.com/watch?v=PrYfOzRYwFc")
q1.save("kavya.png",scale=8)
q2.save("yt.jpg",scale=7)
q3.save("gf.jpg",scale=5)
a=decode(Image.open("kavya.png"))
print(a[0].data.decode("ascii"))