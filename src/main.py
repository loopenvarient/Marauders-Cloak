import cv2

from background_capture import capture_background
from config import LOWER_BOUND, UPPER_BOUND, KERNEL


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

        # Blur before masking for smoother cloak edges
        blurred = cv2.GaussianBlur(frame, (7, 7), 0)
        hsv_frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # Threshold
        mask = cv2.inRange(hsv_frame, LOWER_BOUND, UPPER_BOUND)

        # Morphological cleanup
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, KERNEL, iterations=2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, KERNEL, iterations=2)

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
            new_bg = capture_background(cap)
            if new_bg is not None:
                background = new_bg

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
