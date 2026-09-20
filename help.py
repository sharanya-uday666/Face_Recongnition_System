from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path


class Help:

    def __init__(self, root):

        self.root = root

        # =====================================================
        # WINDOW
        # =====================================================

        self.root.geometry("1100x650+50+20")
        self.root.title("Student Management System")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        # =====================================================
        # PROJECT FOLDER
        # =====================================================

        self.project_folder = Path(__file__).resolve().parent

        # =====================================================
        # TITLE
        # =====================================================

        title_lbl = Label(
            self.root,
            text="HELP DESK",
            font=("Times New Roman", 23, "bold"),
            bg="white",
            fg="blue"
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

        image_path = self.project_folder / "OIP.webp"

        # Check whether image exists
        if image_path.exists():

            img_top = Image.open(image_path)

            # Resize image
            image_top = img_top.resize(
                (1100, 595),
                Image.Resampling.LANCZOS
            )

            # Convert image for Tkinter
            self.photoimg_top = ImageTk.PhotoImage(image_top)

            # Display image
            f_lb1 = Label(
                self.root,
                image=self.photoimg_top
            )

            f_lb1.place(
                x=0,
                y=55,
                width=1100,
                height=595
            )

            # =================================================
            # EMAIL ON LAPTOP SCREEN
            # =================================================

            email_label = Label(
                f_lb1,
                text="Email:gowdasharanya@gmail.com",
                font=("Times New Roman", 14, "bold"),
                bg="#ffffff",
                fg="blue",
                justify="center"
            )

            email_label.place(
                x=420,
                y=40,
                width=350,
                height=70
            )

        else:

            messagebox.showerror(
                "Image Error",
                f"Image file not found:\n\n{image_path}"
            )


# =============================================================
# MAIN PROGRAM
# =============================================================

if __name__ == "__main__":

    root = Tk()

    app = Help(root)

    root.mainloop()