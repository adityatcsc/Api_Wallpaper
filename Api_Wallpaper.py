import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from tkinter import *
import urllib.request
import urllib.parse
from io import BytesIO
from PIL import Image, ImageTk

root = Tk()
root.geometry("600x400")
root.minsize(500, 300)
root.title("Image.ai")
root.config(bg="#2F4F4F")

header = Frame(root, pady=20, bg="#2F4F4F")
header_label = Label(header, text="Ai Image Generator", font="SansSerif 35 bold", bg="#2F4F4F", fg="white")
header_label.pack()
header.pack(fill=X)

searchvalu = StringVar()
search_fr = Frame(root, pady=20, bg="#2F4F4F")

value = Entry(search_fr, textvariable=searchvalu, font="SansSerif 20", bg="#E0FFFF")
value.pack(ipadx=100, expand=5)

search_button = Button(search_fr, text="Search", padx=20, cursor="hand2", bg="#00FFFF", activebackground="#40E0D0")
search_button.pack(pady=10)

img_label = Label(root, relief="sunken", bd=2)
img_label.pack()

def show_image(url):
    try:
        with urllib.request.urlopen(url) as url_response:
            s = url_response.read()
        image = Image.open(BytesIO(s))
        img = ImageTk.PhotoImage(image)
        img_label.config(image=img)
        img_label.image = img
    except Exception as e:
        print(f"Error: {e}")

search_button.bind("<Button-1>", lambda e: show_image(f"https://source.unsplash.com/600x350/?{urllib.parse.quote(searchvalu.get())}"))
search_fr.pack(padx=25, fill=X)

root.mainloop()
