import cv2


def get_user_image(request, ip):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("User", frame)
        image = cv2.imwrite(f"user-{ip}.jpg", frame)
        if image:
            return image
        if request.method == "GET":
            break
    cap.release()
    cv2.destroyAllWindows()
