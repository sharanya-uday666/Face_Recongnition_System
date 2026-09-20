from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path
import os


class Photos:
    
    def __init__(self, root):

        self.root = root

        # =========================================================
        # WINDOW
        # =========================================================

        self.root.geometry("1100x650+50+20")
        self.root.title("Photos Face")
        self.root.resizable(False, False)

        # =========================================================
        # PROJECT FOLDER
        # =========================================================

        self.project_folder = Path(__file__).resolve().parent

        # =========================================================
        # TRAINING IMAGE FOLDER
        # =========================================================

        self.training_folder = self.project_folder / "TrainingImage"

        # =========================================================
        # TITLE
        # =========================================================

        title = Label(
            self.root,
            text="PHOTOS FACE",
            font=("times new roman", 25, "bold"),
            bg="darkblue",
            fg="white"
        )

        title.pack(
            side=TOP,
            fill=X
        )

        # =========================================================
        # INFORMATION
        # =========================================================

        info = Label(
            self.root,
            text="Training Images",
            font=("times new roman", 16, "bold")
        )

        info.pack(
            pady=10
        )

        # =========================================================
        # IMAGE FRAME
        # =========================================================

        self.image_frame = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        self.image_frame.place(
            x=20,
            y=100,
            width=1060,
            height=480
        )

        # =========================================================
        # LOAD IMAGES
        # =========================================================

        self.load_images()

        # =========================================================
        # CLOSE BUTTON
        # =========================================================

        close_button = Button(
            self.root,
            text="Close",
            command=self.root.destroy,
            font=("times new roman", 13, "bold"),
            bg="red",
            fg="white",
            cursor="hand2"
        )

        close_button.place(
            x=490,
            y=595,
            width=120,
            height=35
        )

    # =============================================================
    # LOAD IMAGES
    # =============================================================

    def load_images(self):

        # Check TrainingImage folder

        if not self.training_folder.exists():

            messagebox.showerror(
                "Folder Not Found",
                "TrainingImage folder was not found.\n\n"
                f"Expected location:\n\n"
                f"{self.training_folder}"
            )

            return

        # Get image files

        image_files = []

        for file in self.training_folder.iterdir():

            if file.is_file():

                if file.suffix.lower() in [
                    ".jpg",
                    ".jpeg",
                    ".png",
                    ".webp"
                ]:

                    image_files.append(file)

        # No images

        if len(image_files) == 0:

            messagebox.showinfo(
                "No Images",
                "No face images were found in the TrainingImage folder."
            )

            return

        # =========================================================
        # CANVAS
        # =========================================================

        canvas = Canvas(
            self.image_frame,
            bg="white"
        )

        scrollbar = Scrollbar(
            self.image_frame,
            orient=VERTICAL,
            command=canvas.yview
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side=RIGHT,
            fill=Y
        )

        canvas.pack(
            side=LEFT,
            fill=BOTH,
            expand=True
        )

        # Frame inside canvas

        image_container = Frame(
            canvas,
            bg="white"
        )

        canvas_window = canvas.create_window(
            (0, 0),
            window=image_container,
            anchor="nw"
        )

        # =========================================================
        # DISPLAY IMAGES
        # =========================================================

        self.photo_list = []

        columns = 5

        row = 0
        column = 0

        for image_file in image_files:

            try:

                img = Image.open(image_file)

                img.thumbnail(
                    (170, 130),
                    Image.Resampling.LANCZOS
                )

                photo = ImageTk.PhotoImage(img)

                self.photo_list.append(photo)

                # Image label

                image_label = Label(
                    image_container,
                    image=photo,
                    bg="white",
                    bd=2,
                    relief=RIDGE
                )

                image_label.grid(
                    row=row * 2,
                    column=column,
                    padx=10,
                    pady=10
                )

                # File name

                name_label = Label(
                    image_container,
                    text=image_file.name,
                    bg="white",
                    font=("times new roman", 9)
                )

                name_label.grid(
                    row=row * 2 + 1,
                    column=column,
                    padx=10,
                    pady=(0, 10)
                )

                column += 1

                if column >= columns:

                    column = 0
                    row += 1

            except Exception as e:

                print(
                    f"Unable to load {image_file}: {e}"
                )

        # =========================================================
        # UPDATE SCROLL REGION
        # =========================================================

        image_container.update_idletasks()

        canvas.configure(
            scrollregion=canvas.bbox("all")
        )


# ==============================================================
# MAIN PROGRAM
# ==============================================================

if __name__ == "__main__":

    root = Tk()

    obj = Photos(root)

    root.mainloop()

