import tkinter
import customtkinter
from pytube import YouTube
import os

class Main:
    def __init__(self):
        self.main()

    
    def on_enter(self, event):
        print("Enter key pressed")
        self.startDownload()

    
    def startDownload(self):
        ytLink = self.url_var.get()  # Correctly get the value from url_var
        output_folder = os.path.join(os.path.expanduser("~"), "Videos", "yt_playlist")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)  # Create the directory if it doesn't exist
        print("Start download for URL:", ytLink)
        if ytLink:
            try:
                ytObject = YouTube(ytLink)
                video = ytObject.streams.get_highest_resolution()
                video.download(output_path=output_folder)
                self.finishedLabel.configure(text=f"Downloading: {ytObject.title}")
            except Exception as e:
                self.finishedLabel.configure(text=f"Error: {e}")
                
                self.finishedLabel.configure(text=f"")
                
            self.finishedLabel.configure(text=f"Downloading: {ytObject.title}")
        else:
            self.finishedLabel.configure(text="Enter Valid link", text_color="red")

    def main(self):

        # System Settings
        customtkinter.set_appearance_mode("System")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # Our app frame
        self.app = customtkinter.CTk()
        self.app.geometry("720x480")
        self.app.title("YouTube Video Downloader")

        #font family, size, weight=bold/normal, slant=italic/roman
        title_font = customtkinter.CTkFont(family="Helvetica", size=30, weight="bold", slant="roman", underline=True, overstrike=False)


        # Adding UI Elements
        title = customtkinter.CTkLabel(self.app, text="Youtube video Downloader", font=title_font)
        title.pack(padx=10, pady=50)

        # Link input
        self.url_var = tkinter.StringVar()
        link = customtkinter.CTkEntry(self.app, width=350, height=20, textvariable=self.url_var)
        link.pack(padx=10, pady=10)

        self.finishedLabel = customtkinter.CTkLabel(self.app, text="")
        self.finishedLabel.pack()

        # Download button
        download = customtkinter.CTkButton(self.app, text="Download", command=self.startDownload)
        download.pack(padx=10, pady=10)

        appreance_button =customtkinter.CTkOptionMenu(self.app, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        appreance_button.pack(pady=20)


        # Bind the Enter key to the startDownload function
        self.app.bind('<Return>', self.on_enter)

        # Run app
        self.app.mainloop()
    
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    print("App starting...")
    main_app = Main()
