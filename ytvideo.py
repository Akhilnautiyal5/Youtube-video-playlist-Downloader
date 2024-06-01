import tkinter
import customtkinter
from pytube import YouTube
class Main:
    def startDownload(self):
        ytLink = self.link.url_var.get()
        if ytLink:
            try:
                ytObject = YouTube(ytLink)
                video = ytObject.streams.get_highest_resolution()
                video.download()
                print(f"Downloaded: {yt.title}")
            except Exception as e:
                print(f"Error: {e}")
            print("Download Complete")
        else:
            print ("Enter Valid link")

    def main(self):
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
        download = customtkinter.CTkButton(app, text="Download", command=self.startDownload)
        download.pack(padx=10, pady=10)

        # Run app
        app.mainloop()

if __name__ == "__main__":
    main_app = Main()

