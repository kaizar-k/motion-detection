import cv2
import numpy as np

class MotionDetector:
    def __init__(self, threshold=25, blur_size=(21, 21)):
        self.threshold = threshold
        self.blur_size = blur_size
        self.previous_frame = None

    def process_frame(self, frame):
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Blur to reduce noise
        gray = cv2.GaussianBlur(gray, self.blur_size, 0)

        # Initialise previous frame
        if self.previous_frame is None:
            self.previous_frame = gray
            return 0  # no motion on first frame

        # Frame differencing
        frame_delta = cv2.absdiff(self.previous_frame, gray)

        # Threshold to isolate motion
        _, thresh = cv2.threshold(frame_delta, self.threshold, 255, cv2.THRESH_BINARY)

        # Update previous frame
        self.previous_frame = gray

        # Motion score = number of white pixels
        motion_score = np.sum(thresh) / 255

        return motion_score
