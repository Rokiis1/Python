from pytube import YouTube

# We pass arguments to the script
link = input("Enter link here: ")
yt = YouTube(link)

print("Title", yt.title)

print("View",yt.views)

print("downloading....")

# Download video by higest resolution
yd = yt.streams.get_highest_resolution()
yd.download('./video')

print("Downloaded!")
