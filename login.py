from tkinter import *
from tkinter import messagebox
from pathlib import Path
import subprocess
import sys


class Login:

    def __init__(self, root):

        self.root = root

        # =========================================================
        # WINDOW
        # =========================================================

        self.root.geometry("500x400+450+150")
        self.root.title("Login - Face Recognition System")
        self.root.resizable(False, False)

        # =========================================================
        # PROJECT FOLDER
        # =========================================================

        # login.py and main.py are in the SAME folder
        self.project_folder = Path(__file__).resolve().parent

        # =========================================================
        # MAIN FRAME
        # =========================================================

        main_frame = Frame(
            self.root,
            bg="white"
        )

        main_frame.place(
            x=0,
            y=0,
            width=500,
            height=400
        )

        # =========================================================
        # TITLE
        # =========================================================

        title = Label(
            main_frame,
            text="FACE RECOGNITION SYSTEM",
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="darkblue"
        )

        title.place(
            x=0,
            y=25,
            width=500,
            height=40
        )

        # =========================================================
        # LOGIN TITLE
        # =========================================================

        login_title = Label(
            main_frame,
            text="LOGIN",
            font=("times new roman", 18, "bold"),
            bg="darkblue",
            fg="white"
        )

        login_title.place(
            x=100,
            y=85,
            width=300,
            height=45
        )

        # =========================================================
        # USERNAME LABEL
        # =========================================================

        username_label = Label(
            main_frame,
            text="Username",
            font=("times new roman", 14, "bold"),
            bg="white",
            fg="black"
        )

        username_label.place(
            x=60,
            y=155,
            width=130,
            height=30
        )

        # =========================================================
        # USERNAME ENTRY
        # =========================================================

        self.username = Entry(
            main_frame,
            font=("times new roman", 14),
            bd=2,
            relief=GROOVE
        )

        self.username.place(
            x=210,
            y=155,
            width=220,
            height=32
        )

        # =========================================================
        # PASSWORD LABEL
        # =========================================================

        password_label = Label(
            main_frame,
            text="Password",
            font=("times new roman", 14, "bold"),
            bg="white",
            fg="black"
        )

        password_label.place(
            x=60,
            y=205,
            width=130,
            height=30
        )

        # =========================================================
        # PASSWORD ENTRY
        # =========================================================

        self.password = Entry(
            main_frame,
            font=("times new roman", 14),
            bd=2,
            relief=GROOVE,
            show="*"
        )

        self.password.place(
            x=210,
            y=205,
            width=220,
            height=32
        )

        # =========================================================
        # SHOW PASSWORD
        # =========================================================

        self.show_password = BooleanVar()

        show_password = Checkbutton(
            main_frame,
            text="Show Password",
            variable=self.show_password,
            command=self.show_hide_password,
            font=("times new roman", 10),
            bg="white"
        )

        show_password.place(
            x=210,
            y=240,
            width=140,
            height=25
        )

        # =========================================================
        # LOGIN BUTTON
        # =========================================================

        login_button = Button(
            main_frame,
            text="Login",
            command=self.login,
            cursor="hand2",
            font=("times new roman", 14, "bold"),
            bg="darkblue",
            fg="white",
            activebackground="blue",
            activeforeground="white"
        )

        login_button.place(
            x=100,
            y=290,
            width=140,
            height=40
        )

        # =========================================================
        # EXIT BUTTON
        # =========================================================

        exit_button = Button(
            main_frame,
            text="Exit",
            command=self.exit_system,
            cursor="hand2",
            font=("times new roman", 14, "bold"),
            bg="red",
            fg="white"
        )

        exit_button.place(
            x=260,
            y=290,
            width=140,
            height=40
        )

        # =========================================================
        # ENTER KEY
        # =========================================================

        self.root.bind(
            "<Return>",
            lambda event: self.login()
        )

        # Put cursor in username box
        self.username.focus()

    # =============================================================
    # SHOW / HIDE PASSWORD
    # =============================================================

    def show_hide_password(self):

        if self.show_password.get():

            self.password.config(
                show=""
            )

        else:

            self.password.config(
                show="*"
            )

    # =============================================================
    # LOGIN
    # =============================================================

    def login(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        # =========================================================
        # USERNAME AND PASSWORD
        # =========================================================

        correct_username = "sharanya"
        correct_password = "123456"

        # =========================================================
        # CHECK EMPTY
        # =========================================================

        if username == "" or password == "":

            messagebox.showwarning(
                "Warning",
                "Please enter username and password."
            )

            return

        # =========================================================
        # CHECK LOGIN
        # =========================================================

        if username == correct_username and password == correct_password:

            messagebox.showinfo(
                "Login Successful",
                "Welcome Sharanya!\n\n"
                "Login successful."
            )

            # Close login window
            self.root.destroy()

            # Open main.py
            self.open_main()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

            self.password.delete(
                0,
                END
            )

            self.password.focus()

    # =============================================================
    # OPEN MAIN.PY
    # =============================================================

    def open_main(self):

        # main.py is in the SAME folder as login.py
        main_file = self.project_folder / "main.py"

        # =========================================================
        # CHECK MAIN.PY
        # =========================================================

        if not main_file.exists():

            messagebox.showerror(
                "File Not Found",
                "main.py was not found.\n\n"
                "Expected location:\n\n"
                + str(main_file)
            )

            return

        # =========================================================
        # OPEN MAIN.PY
        # =========================================================

        try:

            subprocess.Popen(
                [sys.executable, str(main_file)],
                cwd=str(self.project_folder)
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                "Unable to open main.py.\n\n"
                "Error:\n"
                + str(e)
            )

    # =============================================================
    # EXIT
    # =============================================================

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

    obj = Login(root)

    root.mainloop()