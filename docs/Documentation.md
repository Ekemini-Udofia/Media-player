# Documentation for the Media Player Windows App

## Overview
This is a simple media player application built using `tkinter` for the GUI and `moviepy` for video playback. The application allows users to open and play video files within the application window. It also provides basic playback controls such as "Play" and "Stop."

---

## Features
- **Open Video**: Allows the user to select a video file using a file dialog.
- **Play Video**: Plays the currently loaded video inside the application window.
- **Stop Video**: Stops the video playback and clears the display.
- **Resizable Window**: The application window can be resized dynamically.

---

## Dependencies
The following Python libraries are required:
- `tkinter`: For the graphical user interface.
- `moviepy`: For video playback and frame extraction.
- `Pillow`: For rendering video frames on the `tkinter` canvas.

Install the dependencies using:
```bash
pip install moviepy pillow
```

# Code Structure and Usage

## Global Variables

* `video`: Holds the currently loaded video object.

## Functions

1.  **`open_video()`:**
    * Opens a file dialog to select a video file.
    * Loads the selected video into the `video` variable.
    * Automatically starts playback after loading.

2.  **`play_video()`:**
    * Plays the currently loaded video.
    * Renders video frames on the tkinter canvas.
    * Contains nested functions:
        * **`update_frame(frame)`:** Converts a video frame to an image and displays it on the canvas.
        * **`render_video()`:** Iterates through video frames and updates the canvas in real-time.

3.  **`stop_video()`:**
    * Stops the video playback by clearing the canvas.

## How to Use

1.  **Run the application:**
    * `python main.py`
2.  **Open a video:**
    * Click the "Open" button to select a video file.
    * The video will start playing automatically after selection.
3.  **Replay the video:**
    * Use the "Play" button to replay the video.
4.  **Stop the video:**
    * Use the "Stop" button to stop the video playback.

## Notes

* Supported video formats include `.mp4`, `.avi`, `.mkv`, and `.mov`.
* The application does not currently support audio playback.
* For smoother playback, ensure the video file is not too large or resource-intensive.

## Future Improvements

* Add support for audio playback using `pygame.mixer`.
* Implement a "Pause" button for better control.
* Improve performance for high-resolution videos.
* Add a progress bar to show video playback progress.