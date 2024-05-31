import tkinter
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Video Dowloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert the youtube link")
title.pack(padx=10, pady=10)

# Liink input
link = customtkinter.CTkEntry(app, width=350, height=40, )

# Run app
app.mainloop()