from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path


class Developer:

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
            text="DEVELOPER",
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

        image_path = self.project_folder / "OIP (1).webp"

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
            # MAIN FRAME
            # =================================================

            Main_frame = Frame(
                f_lb1,
                bd=2,
                bg="white"
            )

            Main_frame.place(
                x=600,
                y=20,
                width=480,
                height=550
            )

            # =================================================
            # DEVELOPER IMAGE
            # =================================================

            developer_image_path = (
                self.project_folder /
                "photo_page-0001 - Copy.jpg"
            )

            if developer_image_path.exists():

                img_developer = Image.open(
                    developer_image_path
                )

                image_developer = img_developer.resize(
                    (200, 200),
                    Image.Resampling.LANCZOS
                )

                self.photoimg_developer = ImageTk.PhotoImage(
                    image_developer
                )

                developer_image_label = Label(
                    Main_frame,
                    image=self.photoimg_developer
                )

                developer_image_label.place(
                    x=278,
                    y=10,
                    width=200,
                    height=200
                )

            else:

                messagebox.showerror(
                    "Image Error",
                    f"Developer image file not found:\n\n"
                    f"{developer_image_path}"
                )

            # =================================================
            # DEVELOPER INFO
            # =================================================

            developer_label = Label(
                Main_frame,
                text="Hello my name is Sharanya",
                font=("Times New Roman", 15, "bold"),
                bg="white"
            )

            developer_label.place(
                x=0,
                y=5
            )

            # =================================================
            # DEVELOPER ROLE
            # =================================================

            developer_role = Label(
                Main_frame,
                text="I am Full stack developer",
                font=("Times New Roman", 15, "bold"),
                bg="white"
            )

            developer_role.place(
                x=0,
                y=40
            )

            # =================================================
            # SECOND IMAGE
            # =================================================

            image_path2 = self.project_folder / "th.webp"

            if image_path2.exists():

                img2 = Image.open(image_path2)

                img2 = img2.resize(
                    (500, 300),
                    Image.Resampling.LANCZOS
                )

                self.photoimg2 = ImageTk.PhotoImage(img2)

                f_lb2 = Label(
                    Main_frame,
                    image=self.photoimg2
                )

                f_lb2.place(
                    x=0,
                    y=210,
                    width=500,
                    height=300
                )

            else:

                messagebox.showerror(
                    "Image Error",
                    f"Image file not found:\n\n"
                    f"{image_path2}"
                )

        else:

            # If top image is not found
            messagebox.showerror(
                "Image Error",
                f"Image file not found:\n\n{image_path}"
            )


# =============================================================
# MAIN PROGRAM
# =============================================================

if __name__ == "__main__":

    root = Tk()

    app = Developer(root)

    root.mainloop()

