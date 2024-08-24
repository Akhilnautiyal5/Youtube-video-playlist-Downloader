from pytube import Playlist, YouTube
import os

def download_video(video_url, output_folder, resolution):
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(res=resolution, file_extension='mp4', progressive=True).first()
        
        if video:
            print(f"Downloading video {yt.title}...")
            video.download(output_path=output_folder)
            print(f"Done downloading {yt.title}")
        else:
            print(f"No {resolution} stream available for video {yt.title}")
    except Exception as e:
        print(f"Error downloading video {yt.title}: {str(e)}")

playlist_url = input("Playlist Url: ")
pl = Playlist(playlist_url)

resolution = input("Enter desired resolution (e.g., 720p): ")
output_folder = r"C:\Users\AKHIL\Videos\yt_playlist"               #input("Enter the path where you want to save the videos: ")
# output_folder = r"F:\videos\python"

os.makedirs(output_folder, exist_ok=True)

i = 0
for video_url in pl.video_urls:
    i = i + 1
    download_video(video_url, output_folder, resolution)

print("All Done")
