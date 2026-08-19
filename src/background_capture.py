import cv2
import time

def capture_background(cap, warmup_seconds=2, discard_frames=30):
    """
    Captures a static background frame.
    Assumes the person is NOT in frame yet.
    """
    print(f"Capturing background in {warmup_seconds} seconds... step out of frame!")
    time.sleep(warmup_seconds)  # let camera auto-exposure/white-balance settle

    background = None
    for i in range(discard_frames):
        ret, background = cap.read()
        if not ret:
            print("Error: failed to read frame during background capture")
            return None

    background = cv2.flip(background, 1)  # match the mirror-flip used in the live loop
    print("Background captured.")
    return background


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: could not open webcam")
        return

    background = capture_background(cap)
    if background is None:
        cap.release()
        return

    print("Press 'b' to recapture background, 'q' to quit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: failed to grab frame")
            break

        frame = cv2.flip(frame, 1)

        # For now just show live frame + background side by side to confirm capture worked
        combined = cv2.hconcat([frame, background])
        cv2.imshow('Live (left) vs Background (right)', combined)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('b'):
            background = capture_background(cap)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()