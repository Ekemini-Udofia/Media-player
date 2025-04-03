"""
A Simple Multimedia Player App (Python)

Contributors: @ekemini-udofia (github)
              @charles-d01 (github)

Depndencies/Requirements:

Python Libraries:
              Pillow - pip install pillow
              moviepy - pip install moviepy==1.0.3
              pygame - pip install pygame
              tkinter - inbuilt

Copmpilation: 
              To compile the python script to an executable, install auto-py-to-exe
              - pip install auto-py-to-exe
              Select the main.py script in the auto-py-to-exe menu.
              select icon.ico found @ res/icon.ico

Code Functions:
              The open function gets the path of the video you want to play
              //write the rest of theis later

              

For further ideas/contributions feel free to reach out via email - ekeminiabasiudofia@gmail.com



"""


import tkinter as tk
from tkinter import Button, Frame, Canvas, filedialog
from PIL import Image, ImageTk
import moviepy.editor as mp

# Global variable for the video object
video = None

# command for the open button; it gets the path of the video file to play through the askopenfilename =dialog
def open_video():
    global video
    file_path = filedialog.askopenfilename(
        title="Open Video File",
        filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.mov")]
    )
    if file_path:
        # Load the selected video
        video = mp.VideoFileClip(file_path)
        play_video()
# command for the play nuttons; it starts the video
def play_video():
    if not video:
        return  # Do nothing if no video is loaded

    def update_frame(frame):
        # Convert the frame to an image and display it on the canvas
        frame_image = ImageTk.PhotoImage(image=Image.fromarray(frame))
        canvas.create_image(0, 0, anchor=tk.NW, image=frame_image)
        canvas.image = frame_image  # Keep a reference to avoid garbage collection

    def render_video():
        for frame in video.iter_frames(fps=24, dtype="uint8"):
            update_frame(frame)
            root.update_idletasks()
            root.update()

    render_video()

def stop_video():
    canvas.delete("all")  # Stop the video by clearing the canvas

# Main tkinter window
root = tk.Tk()
root.iconbitmap("res/icon.ico")
root.title("Media Player")
root.geometry("800x600")  # Window size
root.resizable(True, True)  # Allo window to be resizable

# frame for the video display
video_frame = Frame(root, bg="black")
video_frame.pack(fill=tk.BOTH, expand=True)

# the canvas for rendering the video
canvas = Canvas(video_frame, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)

# Frame for the controls
control_frame = Frame(root, bg="gray")
control_frame.pack(fill=tk.X)

# Controls for the buttons
open_button = Button(control_frame, text="Open", command=open_video)
open_button.pack(side=tk.LEFT, padx=10, pady=10)

play_button = Button(control_frame, text="Play", command=play_video)
play_button.pack(side=tk.LEFT, padx=10, pady=10)

stop_button = Button(control_frame, text="Stop", command=stop_video)
stop_button.pack(side=tk.LEFT, padx=10, pady=10)


root.mainloop()