import cv2
import time
from hand_detector import HandDetector


def main():
    pTime = 0  # Previous frame timestamp (initially 0, may cause FPS glitch on first frame)
    cap = cv2.VideoCapture(0)  # Open default webcam
    detector = HandDetector()  # Create hand detector instance
    while True:
        success, img = cap.read()  # Capture a frame
        if not success:
            print("Failed to read from camera.")
            break
        # Detect hands and optionally draw landmarks
        img, results = detector.findHands(img)
        # Get landmark positions and optionally draw circles
        lmList = detector.findPosition(img, results)
        if lmList:
            print(lmList[4])  # Print thumb tip coordinates (landmark 4)

        # Calculate FPS based on time between frames
        fps = 1 / (time.time() - pTime) if time.time() > pTime else 0
        pTime = time.time()  # Update previous time
        # Display FPS on the image in pink text
        cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)  # Show the processed frame
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
            break

    cap.release()  # Release webcam
    cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == "__main__":
    main()