# Code Explanation

This document provides a detailed breakdown of the hand-tracking implementation, split across `hand_detector.py` and `main.py`. The project leverages MediaPipe's pretrained hand-tracking model and OpenCV for real-time video processing.

## File Structure

- **`hand_detector.py`**: Contains the `HandDetector` class for hand detection and landmark extraction.
- **`main.py`**: Manages the video capture loop, FPS calculation, and display.

## Detailed Breakdown

### A. `hand_detector.py`

1. **Imports**:
   - `cv2`: OpenCV library for webcam capture, image processing, and display.
   - `mediapipe as mp`: MediaPipe for hand detection and landmark estimation.

2. **`HandDetector` Class**:
   - **Purpose**: Encapsulates the hand detection logic, making it reusable and modular.
   - **Initialization (`__init__`)**:
     - Creates an instance of `mp.solutions.hands.Hands` with configurable parameters:
       - `mode=False`: Processes video frames (dynamic input) rather than static images.
       - `maxHands=2`: Limits detection to two hands (default, adjustable).
       - `detectionCon=0.5`: Minimum confidence threshold for initial hand detection.
       - `trackCon=0.5`: Minimum confidence for tracking hand landmarks across frames.
     - `self.mpDraw`: Utility from MediaPipe to draw landmarks and connections.
   - **Why?**: These settings balance speed and accuracy for real-time performance.

3. **`findHands` Method**:
   - **Input**: A BGR image from the webcam (OpenCV format).
   - **Process**:
     1. Converts the image to RGB (`cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`), as MediaPipe expects RGB input.
     2. Processes the image with `self.hands.process()` to detect hands and landmarks.
     3. If landmarks are found (`results.multi_hand_landmarks`), optionally draws them on the image using `self.mpDraw.draw_landmarks`.
   - **Output**: Returns the modified image and detection `results` (containing landmark data).
   - **Details**: The drawing connects 21 landmarks per hand (e.g., fingertips, joints) with lines, using MediaPipe’s predefined `HAND_CONNECTIONS`.

4. **`findPosition` Method**:
   - **Input**: The image and `results` from `findHands`.
   - **Process**:
     1. Checks if landmarks exist (`results.multi_hand_landmarks`).
     2. Extracts the first hand’s landmarks (index 0) and converts normalized coordinates (0 to 1) to pixel values based on image dimensions (`h, w`).
     3. Builds a list (`lmList`) of `[x, y]` coordinates for all 21 landmarks.
     4. Optionally draws pink circles (`cv2.circle`) at each landmark position.
   - **Output**: Returns `lmList` with pixel coordinates (e.g., `[[x1, y1], [x2, y2], ...]`).
   - **Why First Hand?**: Simplifies the demo by focusing on one hand; multi-hand support could be added by iterating over all detected hands.
### B. `main.py`

1. **Imports**:
   - `cv2`: For webcam capture and display.
   - `time`: For FPS calculation.
   - `from hand_detector import HandDetector`: Imports the detector class.

2. **`main` Function**:
   - **Purpose**: Orchestrates the real-time video loop and integrates the `HandDetector`.
   - **Steps**:
     1. **Initialization**:
        - `pTime = 0`: Tracks the previous frame’s timestamp for FPS calculation.
        - `cap = cv2.VideoCapture(0)`: Opens the default webcam.
        - `detector = HandDetector()`: Creates a detector instance with default settings.
     2. **Video Loop**:
        - Reads frames (`cap.read()`), exiting if unsuccessful.
        - Calls `detector.findHands(img)` to detect and draw landmarks.
        - Calls `detector.findPosition(img, results)` to get landmark coordinates and prints the thumb tip position (`lmList[4]`) as an example.
        - Calculates FPS using the time difference between frames (`1 / (time.time() - pTime)`).
        - Displays FPS on the image with `cv2.putText`.
        - Shows the image in a window (`cv2.imshow`) and exits on pressing 'q'.
     3. **Cleanup**:
        - Releases the camera (`cap.release()`) and closes windows (`cv2.destroyAllWindows()`).
   - **FPS Logic**: Measures processing speed, critical for real-time applications. The initial `pTime = 0` may cause a divide-by-zero error on the first frame, which could be improved (see commented alternative in the code).

### Technical Details

- **MediaPipe Hands Model**: A lightweight, pretrained machine learning model that detects 21 3D landmarks per hand (x, y, z coordinates). This code uses only 2D (x, y) for simplicity.
- **Coordinate System**: MediaPipe returns normalized coordinates (0 to 1) relative to the image size, scaled to pixel values in `findPosition`.
- **Color Format**: OpenCV uses BGR, while MediaPipe uses RGB, requiring conversion before processing.
- **Landmark Indices**: The 21 landmarks follow MediaPipe’s convention (e.g., 0 = wrist, 4 = thumb tip, 8 = index fingertip). See [MediaPipe Hands documentation](https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/hands.md) for the full map.

### Implementation Choices

- **Single Hand Focus**: The code processes only the first detected hand (`results.multi_hand_landmarks[0]`) for simplicity, though MediaPipe supports multiple hands.
- **Drawing Options**: Both `findHands` and `findPosition` allow toggling drawing (`draw=True/False`) for flexibility (e.g., disable visuals for pure data extraction).
- **Thumb Tip Output**: Printing `lmList[4]` demonstrates accessing specific landmarks; users can modify this to track other points (e.g., `lmList[8]` for the index finger).

### Example Workflow
1. Webcam captures a frame.
2. `findHands` detects hands and draws landmarks.
3. `findPosition` extracts the thumb tip’s pixel coordinates (e.g., `[320, 240]`).
4. FPS is calculated and displayed.
5. The annotated frame is shown in a window.

This structure makes the code beginner-friendly while providing a foundation for advanced features like gesture recognition.