import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        # Initialize MediaPipe Hands model with customizable settings
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=mode,         # False for video, True for static images
            max_num_hands=maxHands,         # Max number of hands to detect
            min_detection_confidence=detectionCon,  # Confidence threshold for detection
            min_tracking_confidence=trackCon        # Confidence for tracking across frames
        )
        self.mpDraw = mp.solutions.drawing_utils  # Utility to draw landmarks

    def findHands(self, img, draw=True):
        # Convert BGR (OpenCV) to RGB (MediaPipe requirement)
        results = self.hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # Draw landmarks and connections if enabled and hands are detected
        if draw and results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)
        return img, results  # Return modified image and detection results

    def findPosition(self, img, results, draw=True):
        lmList = []  # List to store [x, y] coordinates of landmarks
        if results.multi_hand_landmarks:
            h, w, _ = img.shape  # Get image dimensions
            # Process the first detected hand (extendable to multiple hands)
            for lm in results.multi_hand_landmarks[0].landmark:
                # Convert normalized coordinates (0-1) to pixel values
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([cx, cy])
                if draw:
                    # Draw a pink circle at each landmark
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        return lmList  # Return list of landmark coordinates
