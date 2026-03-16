from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Student Form")
root.iconbitmap("star.png.png")

root.geometry('500x500+0+0')
root.configure(background="#700000")

# image
img = Image.open('giet2.jpg')
resize_img = img.resize((100,70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root,image = img)
img_label.pack(pady=10,padx=20)

# text label
text_label = Label(root,text="Gietu,Gunupur",font=('Bold', 14,'bold'),bg="#005F70",fg='black')
text_label.pack(pady=10,padx=20)

email_label = Label(root,text="Email",font=('simple', 12,'bold'),bg="#007070",fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root,font=('simple', 12,'bold'),fg='white',bg='grey')
email_entry.pack(pady=(5,10))

password_label = Label(root,text="Password",font=('Arial', 18,'bold'),bg="#00706E",fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root,font=('simple', 11,'bold'),fg='white',bg='grey')
password_entry.pack(pady=(5,10))

login_btn = Button(root,text="Login",font=('simple', 12,'bold'),bg="#007070",fg='white')
login_btn.pack(pady=(5,10))

root.mainloop()
