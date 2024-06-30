import tkinter
import customtkinter
from pytube import YouTube
import os
import re

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
        print("Starting download for URL:", ytLink)

            # Regular expression to check if the URL is a valid YouTube link
        youtube_regex = re.compile(
            r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+',
            re.IGNORECASE
        )

        if ytLink and youtube_regex.match(ytLink):
            try:
                ytObject = YouTube(ytLink, on_progress_callback=self.on_progress)
                video = ytObject.streams.get_highest_resolution()
                video.download(output_path=output_folder)
                self.finishedLabel.configure(text=f"Downloading: {ytObject.title}", text_color="white")
            except Exception as e:
                self.finishedLabel.configure(text=f"Error: {e}", text_color="red")

            self.finishedLabel.configure(text=f"Downloaded video: {ytObject.title}", text_color="white")       
            print(f"Downloaded video: {ytObject.title}")       
        else:
            self.finishedLabel.configure(text="Enter Valid link", text_color="red")

        


    def on_progress(self, stream, byte_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - byte_remaining
        percentage_of_completion = int((bytes_downloaded / total_size) * 100)
        
        # percent = (str)(int(percentage_of_completion))
        self.pPercentage.configure(text=f"{percentage_of_completion}%")
        self.pPercentage.update()

        # Update Progress Bar
        self.progressbar.set(percentage_of_completion / 100)


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
        self.url_var = tkinter.StringVar(value="")
        link = customtkinter.CTkEntry(self.app, width=350, height=20, textvariable=self.url_var)
        link.pack(padx=10, pady=10)

        self.finishedLabel = customtkinter.CTkLabel(self.app, text="")
        self.finishedLabel.pack()

        # Progress Percentage
        self.pPercentage = customtkinter.CTkLabel(self.app, text="0%")
        self.pPercentage.pack()
        self.pPercentage.update()


        # Progress percentage bar
        self.progressbar = customtkinter.CTkProgressBar(self.app, orientation="horizontal",
            width=300,
            # corner_radius=20,
            # border_width=2,
            # border_color="red",
            # fg_color="green",
            # progress_color="pink",
            # mode="determinate",
            # determinate_speed=5,
            # indeterminate_speed=.5
            
            )
        self.progressbar.set(0)
        self.progressbar.update()
        self.progressbar.pack(padx=10, pady=10)

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
