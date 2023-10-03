import customtkinter
import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk


DEFAULT_EMAIL = ""
FONT_large = ("Microsoft YaHei UI", 17)
FONT_normal = ("Microsoft YaHei UI", 13)


def save():
    pass


def search():
    pass


def generate_password():
    pass


# ---------------------------- UI S1 SETUP ------------------------------- #

app = customtkinter.CTk()
# app.geometry("720x480")
app.title("App Manager")
app.config(padx=50, pady=50)

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
password_copied = customtkinter.CTkLabel(app, text="Password copied to clipboard!", font=FONT_normal, fg_color="transparent")
password_copied.grid(row=5, column=0, columnspan=3, padx=1, pady=1, sticky="EW")


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
