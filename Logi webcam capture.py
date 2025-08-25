import cv2

# Open the webcam (0 is the default camera)
cap = cv2.VideoCapture(2)

# Wait for the camera to initialize
ret, frame = cap.read()

if ret:
    # Save the captured image
    cv2.imwrite("captured_image.jpg", frame)
    print("Image captured and saved as 'captured_image.jpg'")

# Release the camera
cap.release()
cv2.destroyAllWindows()
