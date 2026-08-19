import cv2
import numpy as np
import time

# HSV bounds derived from color sampling (Step 4)
lower_bound = np.array([113, 35, 30])
upper_bound = np.array([141, 180, 200])

kernel = np.ones((5, 5), np.uint8)


def capture_background(cap, warmup_seconds=2, discard_frames=30):
    print(f"Capturing background in {warmup_seconds} seconds... step out of frame!")
    time.sleep(warmup_seconds)

    background = None
    for i in range(discard_frames):
        ret, background = cap.read()
        if not ret:
            print("Error: failed to read frame during background capture")
            return None

    background = cv2.flip(background, 1)
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
            break

        frame = cv2.flip(frame, 1)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Threshold
        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

        # Morphological cleanup
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

        inverse_mask = cv2.bitwise_not(mask)

        # Compositing
        cloak_area = cv2.bitwise_and(background, background, mask=mask)
        non_cloak_area = cv2.bitwise_and(frame, frame, mask=inverse_mask)
        final_output = cv2.bitwise_or(cloak_area, non_cloak_area)

        cv2.imshow('Marauders Cloak', final_output)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('b'):
            background = capture_background(cap)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()