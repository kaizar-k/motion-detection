import cv2
from motion_detection import MotionDetector
from visual_engine import VisualEngine

def main():
    # Initialise systems
    detector = MotionDetector()
    visuals = VisualEngine(width=800, height=600, particle_count=250)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access webcam.")
        return

    running = True

    while running:
        ret, frame = cap.read()
        if not ret:
            break

        # Compute motion score
        motion_score = detector.process_frame(frame)

        # Update visuals
        visuals.update_and_draw(motion_score)

        #show webcam feed
        cv2.imshow('Webcam Feed', frame)

        # Handle quit events
        for event in visuals.pygame.event.get():
            if event.type == visuals.pygame.QUIT:
                running = False

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
