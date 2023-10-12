from tkinter import *
from tkinter import messagebox
import random, pyperclip, json

#PASSWORD GENERATOR#

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    passw = []
    password = ""

    for char in range(nr_letters):
        passw += random.choice(letters)

    for char in range(nr_symbols):
        passw += random.choice(symbols)

    for char in range(nr_numbers):
        passw += random.choice(numbers)

    random.shuffle(passw)
    password = "".join(passw)

    password_input.focus()
    password_input.delete(0,END)
    password_input.insert(0,password)
    pyperclip.copy(password)
    #the generated password is automatically saved to clipboard
#SAVE INFO#
def show_alert():
    messagebox.showinfo("Alert", "One or more fields left empty!")

def add_to_file():
    new_data = {
        website_input.get():{
            "email": email_user_input.get(),
            "password": password_input.get()
        }
    }

    if website_input.get() != "" and email_user_input.get() != "" and password_input.get() != "":
        try:
            with open("accounts.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("accounts.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("accounts.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)
    else:
        show_alert()
#FIND PASSWORD
def find_password():
    try:
        with open("accounts.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        if website_input.get() in data:
            email = data[website_input.get()]["email"]
            password = data[website_input.get()]["password"]
            messagebox.showinfo(title=website_input.get(), message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title="Error", message=f'No details for {website_input.get()} exists.')

#UI SETUP#

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

bg = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=bg)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=34)
website_input.grid(row=1, column=1)
email_user_input = Entry(width=52)
email_user_input.focus()
email_user_input.insert(0, "dragos_juganariu@yahoo.com")
email_user_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=34)
password_input.grid(row=3, column=1)

searchbtn = Button(text="Search", width=14, command=find_password)
searchbtn.grid(row=1, column=2)
generate_password = Button(text="Generate Password", width=14, command=generate_pass)
generate_password.grid(row=3, column=2)
add = Button(text="Add", width=44, command=add_to_file)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()