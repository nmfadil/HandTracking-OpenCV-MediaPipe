# HandTracking-OpenCV-MediaPipe

Real-time hand tracking using MediaPipe and OpenCV, with landmark detection and FPS display for webcam input.

## Overview

This project implements real-time hand tracking using MediaPipe's Hands solution and OpenCV for webcam video capture. It detects hand landmarks (e.g., fingertips, joints) and visualizes them with dots and connections, while displaying the frame rate (FPS) on the screen. The position of the thumb tip (landmark 4) is printed to the console as an example output.

This is a simple demonstration of computer vision techniques for hand detection and tracking, suitable for beginners or as a foundation for gesture-based applications.

## Features

- Real-time hand detection and landmark tracking using a webcam.
- Visualizes 21 hand landmarks per hand with lines connecting them.
- Displays FPS in the video feed.
- Prints the thumb tip coordinates (x, y) to the console.

## Technologies Used

- **Python**: 3.12 (compatible with MediaPipe and OpenCV)
- **Libraries**:
    - `opencv-python`: For webcam capture and image processing.
    - `mediapipe`: For hand detection and landmark estimation.
- **IDE**: VS Code

## Prerequisites

- Python 3.12 (or compatible version).
- A working webcam.
- Virtual environment (recommended).

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/HandTracking-OpenCV-MediaPipe.git
    cd HandTracking-OpenCV-MediaPipe
    ```
2. **Create a Virtual Environment**:
    ```bash
    py -3.12 -m venv venv
    ```
3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python hand_tracking.py
    ```
2. A window will open showing the webcam feed with detected hands, landmarks, and FPS.
3. Press `q` to exit the application.

## Code Explanation

- **HandDetector Class**: Initializes MediaPipe’s Hands model and provides methods for detecting hands and extracting landmark positions.
- **findHands**: Processes the image and draws hand landmarks if detected.
- **findPosition**: Extracts (x, y) coordinates of landmarks and optionally draws circles on them.
- **Main Loop**: Captures webcam frames, applies hand detection, calculates FPS, and displays the output.

For a detailed breakdown, see [CODE_EXPLANATION.md](CODE_EXPLANATION.md).

## Sample Output

- Hands are outlined with lines connecting 21 landmarks (e.g., fingertips, knuckles).
- Pink circles mark each landmark (optional, controlled by `draw=True`).
- FPS is displayed in pink text at the top-left corner.
- Console logs the thumb tip position (e.g., `[320, 240]`).

## Troubleshooting

- **Webcam Issues**: Ensure your webcam is connected and not in use by another app.
- **Module Not Found**: Verify `opencv-python` and `mediapipe` are installed (`pip list`).
- **Low FPS**: Reduce the webcam resolution (edit `cv2.VideoCapture(0)` settings) or run on a more powerful machine.

## Future Improvements

- Add gesture recognition (e.g., thumbs up, peace sign).
- Support multiple hands with distinct IDs.
- Export landmark data to a file for analysis.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.