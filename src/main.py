from tkinter import *
from video import *
from audio import *

root = Tk()

root.title("Media Player")

root.resizable(True, True)

# Create a frame for the video player
video_frame = Frame(root, bg='black')
video_frame.pack(fill=BOTH, expand=YES)

# Create a frame for the controls
control_frame = Frame(root)
control_frame.pack(fill=X)

# Play video function
def play_video():
    video.play(video_frame)

# Pause video function
def pause_video():
    video.pause()

# Stop video function
def stop_video():
    video.stop()

# Play music function
def play_music():
    audio.play()

# Pause music function
def pause_music():
    audio.pause()

# Stop music function
def stop_music():
    audio.stop()

# Add buttons to control frame
play_video_button = Button(control_frame, text="Play Video", command=play_video)
play_video_button.pack(side=LEFT, padx=10, pady=10)

pause_video_button = Button(control_frame, text="Pause Video", command=pause_video)
pause_video_button.pack(side=LEFT, padx=10, pady=10)

stop_video_button = Button(control_frame, text="Stop Video", command=stop_video)
stop_video_button.pack(side=LEFT, padx=10, pady=10)

play_music_button = Button(control_frame, text="Play Music", command=play_music)
play_music_button.pack(side=LEFT, padx=10, pady=10)

pause_music_button = Button(control_frame, text="Pause Music", command=pause_music)
pause_music_button.pack(side=LEFT, padx=10, pady=10)

stop_music_button = Button(control_frame, text="Stop Music", command=stop_music)
stop_music_button.pack(side=LEFT, padx=10, pady=10)

root.mainloop()