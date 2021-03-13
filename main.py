from tkinter import *
from tkinter import messagebox
import password

# ---------- fonksiyon bölümü ----------

def generate_password():
    password_text.set("")
    password_text.set(password.sifre_uret())


def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning!", message="Empty fields are not allowed!")
    else:

        sonuc = messagebox.askokcancel(title=website, message=f"These info are entered:\n"
                                                              f"Email: {email}\n"
                                                              f"Password: {password}\n"
                                                              f"Are you sure to save?")

        if (sonuc):
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

            messagebox.showinfo(title=website, message="Your info is saved successfully!")

            clear()
        else:
            website_text.set("")
            password_text.set("")

def clear():
    website_text.set("")
    #email_text.set("")
    password_text.set("")

def center_window(w=300, h=200):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


# ---------- UI Bölümü ------------------
window = Tk()
window.title("Password Manager - v1.0")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=E)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky=E)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky=E)

# Entrys
website_text = StringVar();
website_entry = Entry(width=52, textvariable=website_text)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_text = StringVar();
email_entry = Entry(width=52, textvariable=email_text)
email_entry.grid(row=2, column=1, columnspan=2)
email_text.set("borayuret@gmail.com")
password_text = StringVar();
password_entry = Entry(width=33, textvariable=password_text, show='*')
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)


center_window(550,400)
window.mainloop()
