import tkinter as tk
from tkinter import Button, Frame, Canvas, filedialog
from PIL import Image, ImageTk
import moviepy.editor as mp

# Global variable to hold the video object
video = None

# Function to open a new video file
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

# Function to play the video
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

# Function to stop the video
def stop_video():
    canvas.delete("all")  # Clear the canvas

# Create the main tkinter window
root = tk.Tk()
root.iconbitmap("res/icon.ico")
root.title("Media Player")
root.geometry("800x600")  # Set the initial size of the window
root.resizable(True, True)  # Allow resizing of the window

# Create a frame for the video display
video_frame = Frame(root, bg="black")
video_frame.pack(fill=tk.BOTH, expand=True)

# Create a canvas for rendering the video
canvas = Canvas(video_frame, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)

# Create a frame for the controls
control_frame = Frame(root, bg="gray")
control_frame.pack(fill=tk.X)

# Add buttons for controls
open_button = Button(control_frame, text="Open", command=open_video)
open_button.pack(side=tk.LEFT, padx=10, pady=10)

play_button = Button(control_frame, text="Play", command=play_video)
play_button.pack(side=tk.LEFT, padx=10, pady=10)

stop_button = Button(control_frame, text="Stop", command=stop_video)
stop_button.pack(side=tk.LEFT, padx=10, pady=10)

# Run the tkinter main loop
root.mainloop()