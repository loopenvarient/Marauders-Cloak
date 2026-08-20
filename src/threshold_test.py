import cv2

from config import LOWER_BOUND, UPPER_BOUND, KERNEL


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: could not open webcam")
        return

    print("Showing live feed, raw mask, cleaned mask, and cloak isolated. Press 'q' to quit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        # Blur before masking to match main.py behaviour
        blurred = cv2.GaussianBlur(frame, (7, 7), 0)
        hsv_frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        raw_mask = cv2.inRange(hsv_frame, LOWER_BOUND, UPPER_BOUND)

        # Morphological cleanup
        cleaned_mask = cv2.morphologyEx(raw_mask, cv2.MORPH_OPEN, KERNEL, iterations=2)
        cleaned_mask = cv2.morphologyEx(cleaned_mask, cv2.MORPH_CLOSE, KERNEL, iterations=2)

        cloak_only = cv2.bitwise_and(frame, frame, mask=cleaned_mask)

        cv2.imshow('Live Feed', frame)
        cv2.imshow('Raw Mask', raw_mask)
        cv2.imshow('Cleaned Mask', cleaned_mask)
        cv2.imshow('Cloak Isolated', cloak_only)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
