import cv2
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: could not open webcam")
        return

    print("Webcam opened successfully. Press 'q' to quit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: failed to grab frame")
            break

        # Mirror-flip for natural selfie-view
        frame = cv2.flip(frame, 1)
       
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   # add this line

        cv2.imshow('Marauders Cloak', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()