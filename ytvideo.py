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
                print(f"Downloaded: {ytObject.title}")
            except Exception as e:
                print(f"Error: {e}")
            print("Download Complete")
        else:
            print("Enter Valid link")

    def main(self):
        # System Settings
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        # Our app frame
        self.app = customtkinter.CTk()
        self.app.geometry("720x480")
        self.app.title("YouTube Video Downloader")

        # Adding UI Elements
        title = customtkinter.CTkLabel(self.app, text="Insert the YouTube link")
        title.pack(padx=10, pady=10)

        # Link input
        self.url_var = tkinter.StringVar()
        link = customtkinter.CTkEntry(self.app, width=350, height=20, textvariable=self.url_var)
        link.pack(padx=10, pady=10)

        # Download button
        download = customtkinter.CTkButton(self.app, text="Download", command=self.startDownload)
        download.pack(padx=10, pady=10)

        # Bind the Enter key to the startDownload function
        self.app.bind('<Return>', self.on_enter)

        # Run app
        self.app.mainloop()

if __name__ == "__main__":
    print("App starting...")
    main_app = Main()
