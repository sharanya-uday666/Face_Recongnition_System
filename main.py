from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path
import subprocess
import sys
from datetime import datetime


class Face_Recognition_System:

    def __init__(self, root):

        self.root = root

        # =========================================================
        # WINDOW
        # =========================================================

        self.root.geometry("1200x600+50+20")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)

        # =========================================================
        # PROJECT FOLDER
        # =========================================================

        self.project_folder = Path(__file__).resolve().parent

        # =========================================================
        # IMAGE LOADING FUNCTION
        # =========================================================

        def load_image(filename, width, height):

            image_path = self.project_folder / "college_images" / filename

            try:

                if image_path.exists():

                    img = Image.open(image_path)

                    img = img.resize(
                        (width, height),
                        Image.Resampling.LANCZOS
                    )

                    return ImageTk.PhotoImage(img)

                else:

                    print("Image not found:")
                    print(image_path)

            except Exception as e:

                print("Error loading image:")
                print(image_path)
                print(e)

            # Blank image if image is missing
            img = Image.new(
                "RGB",
                (width, height),
                "lightgray"
            )

            return ImageTk.PhotoImage(img)

        # =========================================================
        # TOP IMAGE 1
        # =========================================================

        self.photoimg = load_image(
            "sunflowers-8980921_1280.jpg",
            400,
            90
        )

        label1 = Label(
            self.root,
            image=self.photoimg
        )

        label1.place(
            x=0,
            y=0,
            width=400,
            height=90
        )

        # =========================================================
        # TOP IMAGE 2
        # =========================================================

        self.photoimg1 = load_image(
            "ChatGPT Image Mar 1, 2026, 07_38_08 PM.png",
            400,
            90
        )

        label2 = Label(
            self.root,
            image=self.photoimg1
        )

        label2.place(
            x=400,
            y=0,
            width=400,
            height=90
        )

        # =========================================================
        # TOP IMAGE 3
        # =========================================================

        self.photoimg2 = load_image(
            "ChatGPT Image Mar 2, 2026, 12_26_46 AM.png",
            400,
            90
        )

        label3 = Label(
            self.root,
            image=self.photoimg2
        )

        label3.place(
            x=800,
            y=0,
            width=400,
            height=90
        )

        # =========================================================
        # BACKGROUND IMAGE
        # =========================================================

        self.photoimg3 = load_image(
            "WhatsApp Image 2026-06-20 at 7.49.52 PM.jpeg",
            1200,
            510
        )

        background = Label(
            self.root,
            image=self.photoimg3
        )

        background.place(
            x=0,
            y=90,
            width=1200,
            height=510
        )

        # =========================================================
        # TITLE
        # =========================================================

        title_lbl = Label(
            background,
            text="FACE RECOGNITION SYSTEM ATTENDANCE SYSTEM SOFTWARE",
            font=("times new roman", 19, "bold"),
            bg="white",
            fg="red"
        )

        title_lbl.place(
            x=0,
            y=0,
            width=1200,
            height=40
        )

        # =========================================================
        # LIVE DATE AND TIME
        # =========================================================

        self.time_lbl = Label(
            background,
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black"
        )

        self.time_lbl.place(
            x=0,
            y=40,
            width=1200,
            height=30
        )

        # Start clock
        self.update_time()

        # =========================================================
        # STUDENT DETAILS
        # =========================================================

        self.photoimg4 = load_image(
            "360_F_35308534_WGRVXlymcjQqoRXzeWEfVCOfBHBq9YdW.jpg",
            160,
            115
        )

        b1 = Button(
            background,
            image=self.photoimg4,
            cursor="hand2",
            command=self.student_details
        )

        b1.place(
            x=60,
            y=75,
            width=160,
            height=115
        )

        b1_1 = Button(
            background,
            text="Student Details",
            command=self.student_details,
            cursor="hand2",
            font=("times new roman", 11, "bold"),
            bg="darkblue",
            fg="white"
        )

        b1_1.place(
            x=60,
            y=190,
            width=160,
            height=30
        )

        # =========================================================
        # FACE RECOGNITION
        # =========================================================

        self.photoimg5 = load_image(
            "istockphoto-2162644435-612x612.jpg",
            160,
            115
        )

        b2 = Button(
            background,
            image=self.photoimg5,
            cursor="hand2",
            command=self.face_detector
        )

        b2.place(
            x=350,
            y=75,
            width=160,
            height=115
        )

        b2_1 = Button(
            background,
            text="Face Recognition",
            command=self.face_detector,
            cursor="hand2",
            font=("times new roman", 11, "bold"),
            bg="darkblue",
            fg="white"
        )

        b2_1.place(
            x=350,
            y=190,
            width=160,
            height=30
        )

        # =========================================================
        # ATTENDANCE
        # =========================================================

        self.photoimg6 = load_image(
            "images.jpg",
            160,
            115
        )

        b3 = Button(
            background,
            image=self.photoimg6,
            cursor="hand2",
            command=self.attendance
        )

        b3.place(
            x=640,
            y=75,
            width=160,
            height=115
        )

        b3_1 = Button(
            background,
            text="Attendance",
            command=self.attendance,
            cursor="hand2",
            font=("times new roman", 11, "bold"),
            bg="darkblue",
            fg="white"
        )

        b3_1.place(
            x=640,
            y=190,
            width=160,
            height=30
        )

        # =========================================================
        # HELP DESK
        # =========================================================

        self.photoimg7 = load_image(
            "4939493.png",
            160,
            115
        )

        b4 = Button(
            background,
            image=self.photoimg7,
            cursor="hand2",
            command=self.help_desk
        )

        b4.place(
            x=930,
            y=75,
            width=160,
            height=115
        )

        b4_1 = Button(
            background,
            text="Help Desk",
            command=self.help_desk,
            cursor="hand2",
            font=("times new roman", 11, "bold"),
            bg="darkblue",
            fg="white"
        )

        b4_1.place(
            x=930,
            y=190,
            width=160,
            height=30
        )

        # =========================================================
        # TRAIN DATA
        # =========================================================

        self.photoimg8 = load_image(
            "2022_12_MicrosoftTeams-image-7_480x360.jpg",
            160,
            115
        )

        b5 = Button(
            background,
            image=self.photoimg8,
            cursor="hand2",
            command=self.train_data
        )

        b5.place(
            x=60,
            y=270,
            width=160,
            height=115
        )

        b5_1 = Button(
            background,
            text="Train Data",
            command=self.train_data,
            cursor="hand2",
            font=("times new roman", 11, "bold"),
            bg="darkblue",
            fg="white"
        )

        b5_1.place(
            x=60,
            y=385,
            width=160,
            height=30
        )

        # =========================================================
        # PHOTOS FACE
        # =========================================================

        self.photoimg9 = load_image(
            "blue-smiley-face-button-15880828.webp",
            160,
            115
        )

        b6 = Button(
            background,
            image=self.photoimg9,
            cursor="hand2",
            command=self.photos_face
        )

        b6.place(
            x=350,
            y=270,
            width=160,
            height=115
        )

        b6_1 = Button(
            background,
            text="Photos Face",
            command=self.photos_face,
            cursor="hand2",
            font=("times new roman", 11, "bold"),
            bg="darkblue",
            fg="white"
        )

        b6_1.place(
            x=350,
            y=385,
            width=160,
            height=30
        )

        # =========================================================
        # DEVELOPER
        # =========================================================

        self.photoimg10 = load_image(
            "images.jpg",
            160,
            115
        )

        b7 = Button(
            background,
            image=self.photoimg10,
            cursor="hand2",
            command=self.developer
        )

        b7.place(
            x=640,
            y=270,
            width=160,
            height=115
        )

        b7_1 = Button(
            background,
            text="Developer",
            command=self.developer,
            cursor="hand2",
            font=("times new roman", 11, "bold"),
            bg="darkblue",
            fg="white"
        )

        b7_1.place(
            x=640,
            y=385,
            width=160,
            height=30
        )

        # =========================================================
        # EXIT
        # =========================================================

        self.photoimg11 = load_image(
            "zq129-plastic-exit-sign-face-panel-signs.jpg",
            160,
            115
        )

        b8 = Button(
            background,
            image=self.photoimg11,
            cursor="hand2",
            command=self.exit_system
        )

        b8.place(
            x=930,
            y=270,
            width=160,
            height=115
        )

        b8_1 = Button(
            background,
            text="Exit",
            command=self.exit_system,
            cursor="hand2",
            font=("times new roman", 11, "bold"),
            bg="darkblue",
            fg="white"
        )

        b8_1.place(
            x=930,
            y=385,
            width=160,
            height=30
        )

    # =========================================================
    # LIVE DATE AND TIME
    # =========================================================

    def update_time(self):

        current_time = datetime.now().strftime(
            "%d-%m-%Y    %I:%M:%S %p"
        )

        self.time_lbl.config(
            text="Date & Time : " + current_time
        )

        # Update every 1 second
        self.root.after(
            1000,
            self.update_time
        )

    # =========================================================
    # OPEN PYTHON FILE
    # =========================================================

    def open_module(self, filename, module_name):

        file_path = self.project_folder / filename

        # Check file exists
        if not file_path.exists():

            messagebox.showerror(
                "File Not Found",
                f"{filename} was not found.\n\n"
                f"Expected location:\n\n"
                f"{file_path}"
            )

            return

        try:

            subprocess.Popen(
                [sys.executable, str(file_path)],
                cwd=str(self.project_folder)
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to open {module_name}.\n\n"
                f"Error:\n{e}"
            )

    # =========================================================
    # STUDENT DETAILS
    # =========================================================

    def student_details(self):

        self.open_module(
            "student.py",
            "Student Details"
        )

    # =========================================================
    # FACE RECOGNITION
    # =========================================================

    def face_detector(self):

        self.open_module(
            "face_recongnition.py",
            "Face Recognition"
        )

    # =========================================================
    # ATTENDANCE
    # =========================================================

    def attendance(self):

        self.open_module(
            "attendance.py",
            "Attendance"
        )

    # =========================================================
    # HELP DESK
    # =========================================================

    def help_desk(self):

        self.open_module(
            "help.py",
            "Help Desk"
        )

    # =========================================================
    # TRAIN DATA
    # =========================================================

    def train_data(self):

        self.open_module(
            "train.py",
            "Train Data"
        )

    # =========================================================
    # PHOTOS FACE
    # =========================================================

    def photos_face(self):

        self.open_module(
            "photos.py",
            "Photos Face"
        )

    # =========================================================
    # DEVELOPER
    # =========================================================

    def developer(self):

        self.open_module(
            "developer.py",
            "Developer"
        )

    # =========================================================
    # EXIT
    # =========================================================

    def exit_system(self):

        answer = messagebox.askyesno(
            "Exit",
            "Do you want to exit?"
        )

        if answer:

            self.root.destroy()


# =============================================================
# MAIN PROGRAM
# =============================================================

if __name__ == "__main__":

    root = Tk()

    obj = Face_Recognition_System(root)

    root.mainloop()

