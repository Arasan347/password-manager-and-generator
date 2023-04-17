from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters = random.randint(0, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_letters = [random.choice(letters) for _ in range(nr_letters)]
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

password_list = password_letters+password_symbols+password_numbers
random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

def gen_password():
    pass_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_text = web_input.get()
    mail_text = mail_input.get()
    pass_text = pass_input.get()



    if web_text == "" or pass_text == "":
        messagebox.showinfo(title="warning", message="Hey you have left some fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="confirmation", message="Is it ok to save the details?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{web_text} | {mail_text} | {pass_text}\n")
            web_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password")
window.config(pady=20, padx=20)


canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)

# labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)


# inputs
web_input = Entry(width=50)
web_input.grid(column=1, row=1, columnspan=3)
web_input.focus()

mail_input = Entry(width=50)
mail_input.grid(column=1, row=2, columnspan=3)
mail_input.insert(0, "arasanb43@gmail.com")


pass_input = Entry(width=33)
pass_input.grid(column=1, row=3, columnspan=1)



# Buttons
gen_button = Button(text="Generate",width=13, command=gen_password)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=3)


window.mainloop()