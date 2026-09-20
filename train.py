from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path
import cv2
import re
import numpy as np


class Train:

    def __init__(self, root):

        self.root = root

        # =====================================================
        # PROJECT FOLDER
        # =====================================================

        self.project_folder = Path(__file__).resolve().parent

        # =====================================================
        # FOLDERS
        # =====================================================

        self.image_folder = self.project_folder / "college_images"

        self.training_folder = (
            self.project_folder / "TrainingImage"
        )

        # =====================================================
        # CLASSIFIER FILE
        # =====================================================

        self.classifier_path = (
            self.project_folder / "classifier.xml"
        )

        # Create TrainingImage folder if it does not exist

        self.training_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        # =====================================================
        # WINDOW
        # =====================================================

        self.root.geometry(
            "1100x650+50+20"
        )

        self.root.title(
            "Face Recognition System"
        )

        self.root.resizable(
            False,
            False
        )

        self.root.configure(
            bg="white"
        )

        # =====================================================
        # TITLE
        # =====================================================

        title_lbl = Label(
            self.root,
            text="TRAIN DATA SET",
            font=(
                "Times New Roman",
                23,
                "bold"
            ),
            bg="white",
            fg="red"
        )

        title_lbl.place(
            x=0,
            y=0,
            width=1100,
            height=50
        )

        # =====================================================
        # TOP IMAGE
        # =====================================================

        top_image_path = (
            self.image_folder /
            "download.webp"
        )

        try:

            if top_image_path.exists():

                img_top = Image.open(
                    top_image_path
                )

                img_top = img_top.resize(
                    (1100, 300),
                    Image.Resampling.LANCZOS
                )

                self.photoimg_top = ImageTk.PhotoImage(
                    img_top
                )

                top_label = Label(
                    self.root,
                    image=self.photoimg_top,
                    bd=0
                )

                top_label.place(
                    x=0,
                    y=50,
                    width=1100,
                    height=300
                )

            else:

                raise FileNotFoundError(
                    str(top_image_path)
                )

        except Exception as e:

            top_label = Label(
                self.root,
                text="TOP IMAGE NOT FOUND",
                font=(
                    "Times New Roman",
                    25,
                    "bold"
                ),
                bg="lightgray",
                fg="black"
            )

            top_label.place(
                x=0,
                y=50,
                width=1100,
                height=300
            )

            print(
                "Top image error:",
                e
            )

        # =====================================================
        # TRAIN BUTTON
        # =====================================================

        train_button = Button(
            self.root,
            text="TRAIN DATA",
            cursor="hand2",
            font=(
                "Times New Roman",
                16,
                "bold"
            ),
            bg="darkblue",
            fg="white",
            activebackground="blue",
            activeforeground="white",
            command=self.train_classifier
        )

        train_button.place(
            x=0,
            y=350,
            width=1100,
            height=60
        )

        # =====================================================
        # BOTTOM IMAGE
        # =====================================================

        bottom_image_path = (
            self.image_folder /
            "OIP.webp"
        )

        try:

            if bottom_image_path.exists():

                img_bottom = Image.open(
                    bottom_image_path
                )

                img_bottom = img_bottom.resize(
                    (1100, 240),
                    Image.Resampling.LANCZOS
                )

                self.photoimg_bottom = ImageTk.PhotoImage(
                    img_bottom
                )

                bottom_label = Label(
                    self.root,
                    image=self.photoimg_bottom,
                    bd=0
                )

                bottom_label.place(
                    x=0,
                    y=410,
                    width=1100,
                    height=240
                )

            else:

                raise FileNotFoundError(
                    str(bottom_image_path)
                )

        except Exception as e:

            bottom_label = Label(
                self.root,
                text="BOTTOM IMAGE NOT FOUND",
                font=(
                    "Times New Roman",
                    25,
                    "bold"
                ),
                bg="lightgray",
                fg="black"
            )

            bottom_label.place(
                x=0,
                y=410,
                width=1100,
                height=240
            )

            print(
                "Bottom image error:",
                e
            )

    # =========================================================
    # TRAIN CLASSIFIER
    # =========================================================

    def train_classifier(self):

        try:

            print(
                "\n========================================"
            )

            print(
                "STARTING FACE TRAINING"
            )

            print(
                "========================================"
            )

            # =================================================
            # STEP 1 - CHECK OPENCV FACE
            # =================================================

            if not hasattr(
                cv2,
                "face"
            ):

                messagebox.showerror(
                    "OpenCV Error",
                    "cv2.face is not available.\n\n"
                    "Please install opencv-contrib-python."
                )

                return

            print(
                "OpenCV face module: OK"
            )

            # =================================================
            # STEP 2 - CHECK TRAINING FOLDER
            # =================================================

            if not self.training_folder.exists():

                messagebox.showerror(
                    "Training Error",
                    "TrainingImage folder was not found."
                )

                return

            # =================================================
            # STEP 3 - GET TRAINING IMAGES
            # =================================================

            allowed_extensions = {
                ".jpg",
                ".jpeg",
                ".png",
                ".bmp",
                ".webp"
            }

            image_files = []

            for file in self.training_folder.iterdir():

                if (
                    file.is_file()
                    and
                    file.suffix.lower()
                    in allowed_extensions
                ):

                    image_files.append(
                        file
                    )

            # Sort files

            image_files.sort(
                key=lambda x: x.name
            )

            # =================================================
            # CHECK IMAGES
            # =================================================

            if len(image_files) == 0:

                messagebox.showwarning(
                    "No Training Images",
                    "No face images were found.\n\n"
                    "First open Student Management System.\n\n"
                    "1. Enter student details\n"
                    "2. Click SAVE\n"
                    "3. Click TAKE PHOTO SAMPLE\n"
                    "4. Then come back and click TRAIN DATA"
                )

                return

            print(
                "Training images found:",
                len(image_files)
            )

            # =================================================
            # STEP 4 - CREATE LBPH RECOGNIZER
            # =================================================

            recognizer = (
                cv2.face.LBPHFaceRecognizer_create()
            )

            faces = []

            ids = []

            # =================================================
            # STEP 5 - PROCESS EACH IMAGE
            # =================================================

            for image_path in image_files:

                print(
                    "\nProcessing:",
                    image_path.name
                )

                # -------------------------------------------------
                # GET STUDENT ID FROM FILE NAME
                # -------------------------------------------------

                # Expected:
                #
                # User.230349.1.jpg
                # User.230349.2.jpg
                # User.230349.3.jpg
                #
                # Student ID = 230349

                match = re.match(
                    r"^User\.(\d+)\.",
                    image_path.stem,
                    re.IGNORECASE
                )

                if not match:

                    print(
                        "SKIPPED - Wrong filename:",
                        image_path.name
                    )

                    continue

                student_id = int(
                    match.group(1)
                )

                print(
                    "Student ID:",
                    student_id
                )

                # -------------------------------------------------
                # READ IMAGE AS GRAYSCALE
                # -------------------------------------------------

                img = cv2.imread(
                    str(image_path),
                    cv2.IMREAD_GRAYSCALE
                )

                if img is None:

                    print(
                        "SKIPPED - Image could not be read"
                    )

                    continue

                # -------------------------------------------------
                # CHECK IMAGE SIZE
                # -------------------------------------------------

                if img.size == 0:

                    print(
                        "SKIPPED - Empty image"
                    )

                    continue

                height, width = img.shape

                if height < 20 or width < 20:

                    print(
                        "SKIPPED - Image is too small"
                    )

                    continue

                # -------------------------------------------------
                # ADD FACE IMAGE
                # -------------------------------------------------

                faces.append(
                    img
                )

                ids.append(
                    student_id
                )

                print(
                    "Face added for ID:",
                    student_id
                )

            # =================================================
            # STEP 6 - CHECK TRAINING DATA
            # =================================================

            if len(faces) == 0:

                messagebox.showerror(
                    "Training Failed",
                    "No valid face images were found.\n\n"
                    "Please check the TrainingImage folder."
                )

                return

            if len(ids) == 0:

                messagebox.showerror(
                    "Training Failed",
                    "No Student IDs were found."
                )

                return

            # =================================================
            # UNIQUE STUDENT IDS
            # =================================================

            unique_ids = sorted(
                set(ids)
            )

            print(
                "\n========================================"
            )

            print(
                "TRAINING SUMMARY"
            )

            print(
                "========================================"
            )

            print(
                "Total face images:",
                len(faces)
            )

            print(
                "Student IDs:",
                unique_ids
            )

            print(
                "========================================"
            )

            # =================================================
            # STEP 7 - TRAIN
            # =================================================

            print(
                "\nTraining LBPH recognizer..."
            )

            recognizer.train(
                faces,
                np.array(
                    ids,
                    dtype=np.int32
                )
            )

            print(
                "Training completed."
            )

            # =================================================
            # STEP 8 - DELETE OLD CLASSIFIER
            # =================================================

            if self.classifier_path.exists():

                try:

                    self.classifier_path.unlink()

                    print(
                        "Old classifier.xml deleted."
                    )

                except Exception as e:

                    messagebox.showerror(
                        "File Error",
                        "Could not replace the old "
                        "classifier.xml.\n\n"
                        f"{e}"
                    )

                    return

            # =================================================
            # STEP 9 - SAVE NEW CLASSIFIER
            # =================================================

            recognizer.write(
                str(self.classifier_path)
            )

            # =================================================
            # STEP 10 - CHECK FILE
            # =================================================

            if not self.classifier_path.exists():

                messagebox.showerror(
                    "Save Error",
                    "classifier.xml was not created."
                )

                return

            # =================================================
            # SUCCESS
            # =================================================

            print(
                "\n========================================"
            )

            print(
                "TRAINING SUCCESSFUL"
            )

            print(
                "========================================"
            )

            print(
                "Classifier saved at:"
            )

            print(
                self.classifier_path
            )

            print(
                "Student IDs trained:",
                unique_ids
            )

            print(
                "========================================"
            )

            messagebox.showinfo(
                "Training Completed",
                "Training completed successfully!\n\n"
                f"Training images: {len(image_files)}\n"
                f"Faces trained: {len(faces)}\n"
                f"Student IDs: {unique_ids}\n\n"
                "classifier.xml created successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Training Error",
                "Training failed.\n\n"
                f"{e}"
            )

            print(
                "\n========================================"
            )

            print(
                "TRAINING ERROR:"
            )

            print(
                e
            )

            print(
                "========================================"
            )


# =============================================================
# MAIN PROGRAM
# =============================================================

if __name__ == "__main__":

    root = Tk()

    app = Train(
        root
    )

    root.mainloop()