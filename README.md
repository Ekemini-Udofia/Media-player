
# Simple Media Player

## Overview

This is a basic media player application for Windows built using `tkinter` for the user interface and `moviepy` for video playback. It allows you to open, play, and stop video files.

## Features

* **Open Video:** Select video files via a file dialog.
* **Play Video:** Plays the loaded video.
* **Stop Video:** Stops playback and clears the display.
* **Resizable Window:** Adjust the window size as needed.

## Dependencies

* `tkinter` (Standard Python library)
* `moviepy`
* `Pillow`

Install the required libraries:

```bash
pip install moviepy pillow
```

## Usage

1.  **Run the application:**

    ```bash
    python main.py
    ```

2.  **Open a video:**

    * Click the "Open" button and select a video file.

3.  **Play/Stop:**

    * Use the "Play" and "Stop" buttons to control playback.

## Notes

* Supported video formats: `.mp4`, `.avi`, `.mkv`, `.mov`.
* Audio playback is not currently supported.
* Large video files may affect performance.

## Future Enhancements

* Add audio playback.
* Implement a pause feature.
* Optimize performance for high-resolution videos.
* Include a progress bar.

## Code Structure

### Global Variables

* `video`: Holds the currently loaded video object.

### Functions

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
```
