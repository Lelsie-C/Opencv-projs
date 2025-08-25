import cv2
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import os

class WebcamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Webcam App")

        # Open webcam
        self.cap = cv2.VideoCapture(0)

        # Create video label
        self.video_label = Label(root)
        self.video_label.pack()

        # Capture button
        self.capture_button = Button(root, text="Capture", command=self.capture_image)
        self.capture_button.pack()

        # Exit button
        self.exit_button = Button(root, text="Exit", command=self.close_app)
        self.exit_button.pack()

        # Start video stream
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        self.root.after(10, self.update_frame)

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            save_path = os.path.expanduser("~/Desktop/captured_image.jpg")  # Save to desktop
            cv2.imwrite(save_path, frame)
            print(f"Image saved as {save_path}")

    def close_app(self):
        self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebcamApp(root)
    root.mainloop()
