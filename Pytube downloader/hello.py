from pytube import YouTube

link = input("Enter the URL of the video: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
#pip install pytube in the terminal for your code to run
#Paste the link in the terminal and hit enter(THE VIDEO WILL BE SAVED TO YOU CODE FOLDER)
#Run in VS Code
