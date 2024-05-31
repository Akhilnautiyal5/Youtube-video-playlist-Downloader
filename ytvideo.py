import tkinter
import customtkinter
from pytube import YouTube
class Main:
    def __init__(self):
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
        url_var = tkinter.StringVar()
        link = customtkinter.CTkEntry(app, width=350, height=20, textvariable=url_var)
        link.pack()
        print (url_var)

        # Download button
        # download = customtkinter.CTkButton(app, text="Download", command=startDownload)

        # Run app
        app.mainloop()

if __name__ == "__main__":
    main_app = Main()

