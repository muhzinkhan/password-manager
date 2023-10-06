import customtkinter
from tkinter import messagebox, END
import random
import pyperclip
import json
from PIL import Image


DEFAULT_EMAIL = ""
FONT_large = ("Microsoft YaHei UI", 17)
FONT_normal = ("Microsoft YaHei UI", 13)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_length = 16
    random_3_set = [random.randint(2, 7) for _ in range(2)]
    random_3_set.append(password_length - sum(random_3_set))

    nr_letters = random_3_set[0]
    nr_symbols = random_3_set[1]
    nr_numbers = random_3_set[2]

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)

    # password_copied_label
    password_copied = customtkinter.CTkLabel(app, text="Password copied to clipboard!", font=FONT_normal,
                                             fg_color="transparent")
    password_copied.grid(row=5, column=0, columnspan=3, padx=1, pady=1, sticky="EW")
    password_copied.after(5000, password_copied.destroy)


# ---------------------------- SEARCH SAVED PASSWORD ------------------------------- #

def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website to search.")
    else:
        try:
            with open("data/data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                pyperclip.copy(password)
                messagebox.showinfo(title=website, message=f"Email:          {email}\nPassword:  {password}\n\nPassword has been copied to the clipboard!")
            else:
                messagebox.showinfo(title="Error", message=f"No details for '{website}' exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Email:          {email}\nPassword:  {password} \n\nIs it okay to save?")
        if is_ok:
            try:
                with open("data/data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data/data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data/data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

app = customtkinter.CTk()
app.title("App Manager")
app.geometry("575x485 ")
app.resizable(False, False)
app.config(padx=50, pady=50)
app.iconbitmap('assets/password_manager_icon.ico')

# -------Center Logo-------

img = customtkinter.CTkImage(dark_image=Image.open("assets/password_manager_icon.png"), size=(220, 220))
logo_label = customtkinter.CTkLabel(app, image=img, text="")  # display image with a CTkLabel
logo_label.grid(row=0, column=1, pady=10)


# -------Labels-------

# website_label
website_label = customtkinter.CTkLabel(app, text="Website:", font=FONT_normal, fg_color="transparent")
website_label.grid(row=1, column=0, padx=3, pady=3)

# email_label
email_label = customtkinter.CTkLabel(app, text="Email/Username:", font=FONT_normal, fg_color="transparent")
email_label.grid(row=2, column=0, padx=3, pady=3)

# password_label
password_label = customtkinter.CTkLabel(app, text="Password", font=FONT_normal, fg_color="transparent")
password_label.grid(row=3, column=0, padx=3, pady=3)

# password_copied_label
# Inside the generate_password() definition


# -------Entries -------

# website_entry
website_entry = customtkinter.CTkEntry(app, placeholder_text="Website.com", font=FONT_normal, width=35)
website_entry.grid(row=1, column=1, sticky="EW", padx=3, pady=3)
website_entry.focus()

# email_entry
email_entry = customtkinter.CTkEntry(app, placeholder_text="Email", font=FONT_normal, width=35)
email_entry.insert(0, DEFAULT_EMAIL)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW", padx=3, pady=3)

# password_entry
password_entry = customtkinter.CTkEntry(app, placeholder_text="Password", font=FONT_normal, width=35)
password_entry.grid(row=3, column=1, sticky="EW", padx=3, pady=3)


# -------Buttons-------

# search_button
search_button = customtkinter.CTkButton(app, text="Search", font=FONT_normal, command=search)
search_button.grid(row=1, column=2, sticky="EW", padx=3, pady=3)

# add_button
add_button = customtkinter.CTkButton(app, text="Add", font=FONT_large, height=36, width=36, command=save)
add_button.grid(row=4, column=0, columnspan=3, sticky="EW", padx=3, pady=3)

# generate_button
generate_button = customtkinter.CTkButton(app, text="Generate Password", font=FONT_normal, command=generate_password)
generate_button.grid(row=3, column=2, padx=3, pady=3)

app.mainloop()
