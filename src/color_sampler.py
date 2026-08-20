import cv2


def show_hsv_on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_frame = param["hsv"]
        pixel = hsv_frame[y, x]
        print(f"Clicked at ({x}, {y}) -> HSV: {pixel}")


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: could not open webcam")
        return

    window_name = 'Color Sampler'
    cv2.namedWindow(window_name)

    # Use a mutable dict so the callback always reads the latest HSV frame
    hsv_ref = {"hsv": None}
    cv2.setMouseCallback(window_name, show_hsv_on_click, hsv_ref)

    print("Click on the cloak in the window to sample its HSV value. Press 'q' to quit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        hsv_ref["hsv"] = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        cv2.imshow(window_name, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
