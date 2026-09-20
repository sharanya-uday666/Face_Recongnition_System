from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from pathlib import Path
import mysql.connector
from mysql.connector import Error
import cv2


class Student:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1100x650+50+20")
        self.root.title("Student Management System")
        self.root.resizable(False, False)

        # =====================================================
        # MYSQL SETTINGS
        # =====================================================

        self.MYSQL_HOST = "localhost"
        self.MYSQL_USER = "root"
        self.MYSQL_PASSWORD = "sharu666"
        self.DATABASE = "face_recognition_system"

        # =====================================================
        # VARIABLES
        # =====================================================

        self.var_dep = StringVar(value="Select Department")
        self.var_course = StringVar(value="Select Course")
        self.var_year = StringVar(value="Select Year")
        self.var_semester = StringVar(value="Select Semester")

        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar(value="Select Division")
        self.var_roll = StringVar()
        self.var_gender = StringVar(value="Select Gender")
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar(value="No")

        # =====================================================
        # PROJECT FOLDER
        # =====================================================

        self.project_folder = Path(__file__).resolve().parent

        # =====================================================
        # IMAGE FOLDER
        # =====================================================

        self.image_folder = self.project_folder / "college_images"

        # =====================================================
        # TRAINING IMAGE FOLDER


        # =====================================================

        self.training_folder = self.project_folder / "TrainingImage"
        self.training_folder.mkdir(parents=True, exist_ok=True)

        # =====================================================
        # TOP IMAGES
        # =====================================================

        self.load_top_image(
            "premium_photo-1683887034491-f58b4c4fca72.avif",
            0,
            366,
            "Student Management"
        )

        self.load_top_image(
            "gettyimages-1351416161-612x612.jpg",
            366,
            366,
            "Student"
        )

        self.load_top_image(
            "happy-indian-group-school-kids-students-study-in-class-education-learning-K6P0YK.jpg",
            732,
            368,
            "Students"
        )

        # =====================================================
        # MAIN BACKGROUND
        # =====================================================

        background = Frame(self.root, bg="white")

        background.place(
            x=0,
            y=70,
            width=1100,
            height=580
        )

        # =====================================================
        # TITLE
        # =====================================================

        title_lbl = Label(
            background,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("Times New Roman", 23, "bold"),
            bg="white",
            fg="darkgreen"
        )

        title_lbl.place(
            x=0,
            y=0,
            width=1100,
            height=42
        )

        # =====================================================
        # MAIN FRAME
        # =====================================================

        main_frame = Frame(
            background,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        main_frame.place(
            x=8,
            y=45,
            width=1084,
            height=525
        )

        # =====================================================
        # LEFT FRAME
        # =====================================================

        left_frame = LabelFrame(
            main_frame,
            text="Student Details",
            font=("Times New Roman", 10, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE
        )

        left_frame.place(
            x=7,
            y=7,
            width=525,
            height=505
        )

        # =====================================================
        # LEFT IMAGE
        # =====================================================

        image_path4 = (
            self.image_folder /
            "20240514171831915_img.jpg"
        )

        try:

            img4 = Image.open(image_path4)
            img4 = img4.resize((495, 65))

            self.photoimg4 = ImageTk.PhotoImage(img4)

            left_image = Label(
                left_frame,
                image=self.photoimg4
            )

            left_image.place(
                x=10,
                y=2,
                width=495,
                height=65
            )

        except Exception:

            Label(
                left_frame,
                text="STUDENT INFORMATION",
                font=("Times New Roman", 16, "bold"),
                bg="lightgray"
            ).place(
                x=10,
                y=2,
                width=495,
                height=65
            )

        # =====================================================
        # COURSE FRAME
        # =====================================================

        course_frame = LabelFrame(
            left_frame,
            text="Current Course Information",
            font=("Times New Roman", 10, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE
        )

        course_frame.place(
            x=10,
            y=70,
            width=495,
            height=105
        )

        # Department

        Label(
            course_frame,
            text="Department",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=7
        )

        self.dep_combo = ttk.Combobox(
            course_frame,
            textvariable=self.var_dep,
            font=("Times New Roman", 9),
            width=15,
            state="readonly"
        )

        self.dep_combo["values"] = (
            "Select Department",
            "Computer Science",
            "Information Science",
            "Electronics",
            "Mechanical",
            "Civil"
        )

        self.dep_combo.current(0)

        self.dep_combo.grid(
            row=0,
            column=1,
            padx=3,
            pady=7
        )

        # Course

        Label(
            course_frame,
            text="Course",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=7
        )

        self.course_combo = ttk.Combobox(
            course_frame,
            textvariable=self.var_course,
            font=("Times New Roman", 9),
            width=14,
            state="readonly"
        )

        self.course_combo["values"] = (
            "Select Course",
            "BE",
            "BTech",
            "MCA",
            "MTech"
        )

        self.course_combo.current(0)

        self.course_combo.grid(
            row=0,
            column=3,
            padx=3,
            pady=7
        )

        # Year

        Label(
            course_frame,
            text="Year",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.year_combo = ttk.Combobox(
            course_frame,
            textvariable=self.var_year,
            font=("Times New Roman", 9),
            width=15,
            state="readonly"
        )

        self.year_combo["values"] = (
            "Select Year",
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year"
        )

        self.year_combo.current(0)

        self.year_combo.grid(
            row=1,
            column=1,
            padx=3,
            pady=5
        )

        # Semester

        Label(
            course_frame,
            text="Semester",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

        self.semester_combo = ttk.Combobox(
            course_frame,
            textvariable=self.var_semester,
            font=("Times New Roman", 9),
            width=14,
            state="readonly"
        )

        self.semester_combo["values"] = (
            "Select Semester",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8"
        )

        self.semester_combo.current(0)

        self.semester_combo.grid(
            row=1,
            column=3,
            padx=3,
            pady=5
        )

        # =====================================================
        # STUDENT INFORMATION FRAME
        # =====================================================

        student_frame = LabelFrame(
            left_frame,
            text="Class Student Information",
            font=("Times New Roman", 10, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE
        )

        student_frame.place(
            x=10,
            y=180,
            width=495,
            height=315
        )

        # Student ID

        Label(
            student_frame,
            text="Student ID",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=4
        )

        Entry(
            student_frame,
            textvariable=self.var_std_id,
            font=("Times New Roman", 9),
            width=17
        ).grid(
            row=0,
            column=1,
            padx=3,
            pady=4
        )

        # Student Name

        Label(
            student_frame,
            text="Student Name",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=4
        )

        Entry(
            student_frame,
            textvariable=self.var_std_name,
            font=("Times New Roman", 9),
            width=17
        ).grid(
            row=0,
            column=3,
            padx=3,
            pady=4
        )

        # Division

        Label(
            student_frame,
            text="Class Division",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=4
        )

        self.division_combo = ttk.Combobox(
            student_frame,
            textvariable=self.var_div,
            font=("Times New Roman", 9),
            width=15,
            state="readonly"
        )

        self.division_combo["values"] = (
            "Select Division",
            "A",
            "B",
            "C",
            "D"
        )

        self.division_combo.current(0)

        self.division_combo.grid(
            row=1,
            column=1,
            padx=3,
            pady=4
        )

        # Roll No

        Label(
            student_frame,
            text="Roll No",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=4
        )

        Entry(
            student_frame,
            textvariable=self.var_roll,
            font=("Times New Roman", 9),
            width=17
        ).grid(
            row=1,
            column=3,
            padx=3,
            pady=4
        )

        # Gender

        Label(
            student_frame,
            text="Gender",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=4
        )

        self.gender_combo = ttk.Combobox(
            student_frame,
            textvariable=self.var_gender,
            font=("Times New Roman", 9),
            width=15,
            state="readonly"
        )

        self.gender_combo["values"] = (
            "Select Gender",
            "Male",
            "Female",
            "Other"
        )

        self.gender_combo.current(0)

        self.gender_combo.grid(
            row=2,
            column=1,
            padx=3,
            pady=4
        )

        # DOB

        Label(
            student_frame,
            text="DOB",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=2,
            column=2,
            padx=5,
            pady=4
        )

        Entry(
            student_frame,
            textvariable=self.var_dob,
            font=("Times New Roman", 9),
            width=17
        ).grid(
            row=2,
            column=3,
            padx=3,
            pady=4
        )

        # Email

        Label(
            student_frame,
            text="Email",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=3,
            column=0,
            padx=5,
            pady=4
        )

        Entry(
            student_frame,
            textvariable=self.var_email,
            font=("Times New Roman", 9),
            width=17
        ).grid(
            row=3,
            column=1,
            padx=3,
            pady=4
        )

        # Phone

        Label(
            student_frame,
            text="PhoneNo",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=3,
            column=2,
            padx=5,
            pady=4
        )

        Entry(
            student_frame,
            textvariable=self.var_phone,
            font=("Times New Roman", 9),
            width=17
        ).grid(
            row=3,
            column=3,
            padx=3,
            pady=4
        )

        # Address

        Label(
            student_frame,
            text="Address",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=4,
            column=0,
            padx=5,
            pady=4
        )

        Entry(
            student_frame,
            textvariable=self.var_address,
            font=("Times New Roman", 9),
            width=17
        ).grid(
            row=4,
            column=1,
            padx=3,
            pady=4
        )

        # Teacher

        Label(
            student_frame,
            text="Teacher Name",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=4,
            column=2,
            padx=5,
            pady=4
        )

        Entry(
            student_frame,
            textvariable=self.var_teacher,
            font=("Times New Roman", 9),
            width=17
        ).grid(
            row=4,
            column=3,
            padx=3,
            pady=4
        )

        # =====================================================
        # RADIO BUTTONS
        # =====================================================

        Radiobutton(
            student_frame,
            text="Take Photo Sample",
            variable=self.var_radio1,
            value="Yes",
            font=("Times New Roman", 9, "bold"),
            bg="white",
            activebackground="white"
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            padx=5,
            pady=5
        )

        Radiobutton(
            student_frame,
            text="No Photo Sample",
            variable=self.var_radio1,
            value="No",
            font=("Times New Roman", 9, "bold"),
            bg="white",
            activebackground="white"
        ).grid(
            row=5,
            column=2,
            columnspan=2,
            padx=5,
            pady=5
        )

        # =====================================================
        # BUTTON FRAME
        # =====================================================

        button_frame = Frame(
            student_frame,
            bg="white",
            bd=1,
            relief=RIDGE
        )

        button_frame.place(
            x=5,
            y=185,
            width=477,
            height=120
        )

        Button(
            button_frame,
            text="Save",
            command=self.add_data,
            font=("Times New Roman", 8, "bold"),
            bg="blue",
            fg="white",
            width=9
        ).grid(row=0, column=0, padx=3, pady=4)

        Button(
            button_frame,
            text="Update",
            command=self.update_data,
            font=("Times New Roman", 8, "bold"),
            bg="blue",
            fg="white",
            width=9
        ).grid(row=0, column=1, padx=3, pady=4)

        Button(
            button_frame,
            text="Delete",
            command=self.delete_data,
            font=("Times New Roman", 8, "bold"),
            bg="blue",
            fg="white",
            width=9
        ).grid(row=0, column=2, padx=3, pady=4)

        Button(
            button_frame,
            text="Reset",
            command=self.reset_data,
            font=("Times New Roman", 8, "bold"),
            bg="blue",
            fg="white",
            width=9
        ).grid(row=0, column=3, padx=3, pady=4)

        Button(
            button_frame,
            text="Take Photo Sample",
            command=self.generate_dataset,
            font=("Times New Roman", 8, "bold"),
            bg="blue",
            fg="white",
            width=20
        ).grid(
            row=1,
            column=0,
            columnspan=2,
            padx=3,
            pady=8
        )

        Button(
            button_frame,
            text="Update Photo Sample",
            command=self.generate_dataset,
            font=("Times New Roman", 8, "bold"),
            bg="blue",
            fg="white",
            width=20
        ).grid(
            row=1,
            column=2,
            columnspan=2,
            padx=3,
            pady=8
        )

        # =====================================================
        # RIGHT FRAME
        # =====================================================

        right_frame = LabelFrame(
            main_frame,
            text="Student Details",
            font=("Times New Roman", 10, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE
        )

        right_frame.place(
            x=540,
            y=7,
            width=525,
            height=505
        )

        # =====================================================
        # RIGHT IMAGE
        # =====================================================

        image_path5 = (
            self.image_folder /
            "gettyimages-1351416161-612x612.jpg"
        )

        try:

            img5 = Image.open(image_path5)
            img5 = img5.resize((495, 65))

            self.photoimg5 = ImageTk.PhotoImage(img5)

            Label(
                right_frame,
                image=self.photoimg5
            ).place(
                x=10,
                y=2,
                width=495,
                height=65
            )

        except Exception:

            Label(
                right_frame,
                text="STUDENT DETAILS",
                font=("Times New Roman", 16, "bold"),
                bg="lightgray"
            ).place(
                x=10,
                y=2,
                width=495,
                height=65
            )

        # =====================================================
        # SEARCH FRAME
        # =====================================================

        search_frame = LabelFrame(
            right_frame,
            text="Search System",
            font=("Times New Roman", 10, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE
        )

        search_frame.place(
            x=10,
            y=70,
            width=495,
            height=70
        )

        Label(
            search_frame,
            text="Search By",
            font=("Times New Roman", 9, "bold"),
            bg="white"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=15
        )

        self.search_combo = ttk.Combobox(
            search_frame,
            font=("Times New Roman", 9),
            width=13,
            state="readonly"
        )

        self.search_combo["values"] = (
            "Select",
            "Student ID",
            "Student Name",
            "Phone"
        )

        self.search_combo.current(0)

        self.search_combo.grid(
            row=0,
            column=1,
            padx=3,
            pady=15
        )

        self.search_entry = Entry(
            search_frame,
            font=("Times New Roman", 9),
            width=15
        )

        self.search_entry.grid(
            row=0,
            column=2,
            padx=3,
            pady=15
        )

        Button(
            search_frame,
            text="Search",
            command=self.search_data,
            font=("Times New Roman", 8, "bold"),
            bg="blue",
            fg="white",
            width=9
        ).grid(
            row=0,
            column=3,
            padx=3,
            pady=15
        )

        Button(
            search_frame,
            text="Show All",
            command=self.fetch_data,
            font=("Times New Roman", 8, "bold"),
            bg="blue",
            fg="white",
            width=9
        ).grid(
            row=0,
            column=4,
            padx=3,
            pady=15
        )

        # =====================================================
        # TABLE
        # =====================================================

        table_frame = Frame(
            right_frame,
            bd=2,
            relief=RIDGE,
            bg="white"
        )

        table_frame.place(
            x=10,
            y=145,
            width=495,
            height=345
        )

        scroll_x = ttk.Scrollbar(
            table_frame,
            orient=HORIZONTAL
        )

        scroll_y = ttk.Scrollbar(
            table_frame,
            orient=VERTICAL
        )

        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "dep",
                "course",
                "year",
                "semester",
                "student_id",
                "student_name",
                "division",
                "roll_no",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher_name",
                "photosample"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
            show="headings"
        )

        scroll_x.pack(
            side=BOTTOM,
            fill=X
        )

        scroll_y.pack(
            side=RIGHT,
            fill=Y
        )

        scroll_x.config(
            command=self.student_table.xview
        )

        scroll_y.config(
            command=self.student_table.yview
        )

        headings = {
            "dep": "Department",
            "course": "Course",
            "year": "Year",
            "semester": "Semester",
            "student_id": "Student ID",
            "student_name": "Student Name",
            "division": "Division",
            "roll_no": "Roll No",
            "gender": "Gender",
            "dob": "DOB",
            "email": "Email",
            "phone": "Phone",
            "address": "Address",
            "teacher_name": "Teacher",
            "photosample": "Photo"
        }

        for column, heading in headings.items():

            self.student_table.heading(
                column,
                text=heading
            )

            self.student_table.column(
                column,
                width=100,
                anchor=CENTER
            )

        self.student_table.pack(
            fill=BOTH,
            expand=True
        )

        self.student_table.bind(
            "<ButtonRelease-1>",
            self.get_cursor
        )

        # =====================================================
        # LOAD DATA
        # =====================================================

        self.fetch_data()

    # =========================================================
    # TOP IMAGE
    # =========================================================

    def load_top_image(
        self,
        filename,
        x,
        width,
        fallback_text
    ):

        image_path = self.image_folder / filename

        try:

            img = Image.open(image_path)

            img = img.resize(
                (width, 70)
            )

            photo = ImageTk.PhotoImage(img)

            label = Label(
                self.root,
                image=photo
            )

            label.image = photo

            label.place(
                x=x,
                y=0,
                width=width,
                height=70
            )

        except Exception:

            Label(
                self.root,
                text=fallback_text,
                font=("Times New Roman", 18, "bold"),
                bg="lightgray"
            ).place(
                x=x,
                y=0,
                width=width,
                height=70
            )

    # =========================================================
    # DATABASE CONNECTION
    # =========================================================

    def connect_db(self):

        try:

            conn = mysql.connector.connect(
                host=self.MYSQL_HOST,
                user=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD,
                database=self.DATABASE
            )

            return conn

        except Error as e:

            messagebox.showerror(
                "Database Error",
                f"MySQL connection failed:\n\n{e}\n\n"
                "Make sure MySQL80 service is running.",
                parent=self.root
            )

            return None

    # =========================================================
    # ADD DATA
    # =========================================================

    def add_data(self):

        if (
            self.var_dep.get() == "Select Department"
            or self.var_course.get() == "Select Course"
            or self.var_year.get() == "Select Year"
            or self.var_semester.get() == "Select Semester"
            or self.var_std_id.get().strip() == ""
            or self.var_std_name.get().strip() == ""
            or self.var_div.get() == "Select Division"
            or self.var_gender.get() == "Select Gender"
        ):

            messagebox.showerror(
                "Error",
                "Please fill all required fields.",
                parent=self.root
            )

            return

        # Check numeric Student ID

        try:
            student_id = int(self.var_std_id.get().strip())
        except ValueError:

            messagebox.showerror(
                "Error",
                "Student ID must contain numbers only.",
                parent=self.root
            )

            return

        # Check Roll Number

        roll_no_text = self.var_roll.get().strip()

        if roll_no_text != "":

            try:
                roll_no = int(roll_no_text)
            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Roll No must contain numbers only.",
                    parent=self.root
                )

                return

        else:
            roll_no = None

        # Check semester

        try:
            semester = int(self.var_semester.get())
        except ValueError:

            messagebox.showerror(
                "Error",
                "Please select a valid semester.",
                parent=self.root
            )

            return

        # Check DOB

        dob = self.var_dob.get().strip()

        if dob == "":
            dob = None

        conn = self.connect_db()

        if conn is None:
            return

        cursor = None

        try:

            cursor = conn.cursor()

            query = """
                INSERT INTO student
                (
                    dep,
                    course,
                    year,
                    semester,
                    student_id,
                    student_name,
                    division,
                    roll_no,
                    gender,
                    dob,
                    email,
                    PhoneNo,
                    address,
                    teacher_name,
                    photosample
                )
                VALUES
                (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s
                )
            """

            values = (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                semester,
                student_id,
                self.var_std_name.get().strip(),
                self.var_div.get(),
                roll_no,
                self.var_gender.get(),
                dob,
                self.var_email.get().strip(),
                self.var_phone.get().strip(),
                self.var_address.get().strip(),
                self.var_teacher.get().strip(),
                self.var_radio1.get()
            )

            cursor.execute(
                query,
                values
            )

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Student details saved successfully.",
                parent=self.root
            )

            self.fetch_data()

        except mysql.connector.IntegrityError as e:

            conn.rollback()

            messagebox.showerror(
                "Error",
                f"Student ID already exists or data is invalid.\n\n{e}",
                parent=self.root
            )

        except Error as e:

            conn.rollback()

            messagebox.showerror(
                "Database Error",
                f"Unable to save data:\n\n{e}",
                parent=self.root
            )

        finally:

            if cursor:
                cursor.close()

            if conn.is_connected():
                conn.close()

    # =========================================================
    # FETCH DATA
    # =========================================================

    def fetch_data(self):

        conn = self.connect_db()

        if conn is None:
            return

        cursor = None

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT
                    dep,
                    course,
                    year,
                    semester,
                    student_id,
                    student_name,
                    division,
                    roll_no,
                    gender,
                    dob,
                    email,
                    PhoneNo,
                    address,
                    teacher_name,
                    photosample
                FROM student
                ORDER BY student_id
                """
            )

            rows = cursor.fetchall()

            self.student_table.delete(
                *self.student_table.get_children()
            )

            for row in rows:

                self.student_table.insert(
                    "",
                    END,
                    values=row
                )

        except Error as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to fetch data:\n\n{e}",
                parent=self.root
            )

        finally:

            if cursor:
                cursor.close()

            if conn.is_connected():
                conn.close()

    # =========================================================
    # GET CURSOR
    # =========================================================

    def get_cursor(self, event=""):

        selected = self.student_table.focus()

        if not selected:
            return

        data = self.student_table.item(
            selected
        )

        row = data.get("values")

        if not row:
            return

        self.var_dep.set(row[0])
        self.var_course.set(row[1])
        self.var_year.set(row[2])
        self.var_semester.set(str(row[3]))
        self.var_std_id.set(str(row[4]))
        self.var_std_name.set(row[5])
        self.var_div.set(row[6])
        self.var_roll.set("" if row[7] is None else str(row[7]))
        self.var_gender.set(row[8])

        if row[9] is None:
            self.var_dob.set("")
        else:
            self.var_dob.set(str(row[9]))

        self.var_email.set(row[10])
        self.var_phone.set(row[11])
        self.var_address.set(row[12])
        self.var_teacher.set(row[13])
        self.var_radio1.set(row[14])

    # =========================================================
    # UPDATE DATA
    # =========================================================

    def update_data(self):

        student_id_text = self.var_std_id.get().strip()

        if student_id_text == "":
            messagebox.showerror(
                "Error",
                "Please select a student first.",
                parent=self.root
            )
            return

        try:
            student_id = int(student_id_text)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Student ID must contain numbers only.",
                parent=self.root
            )
            return

        try:
            semester = int(self.var_semester.get())
        except ValueError:
            messagebox.showerror(
                "Error",
                "Please select a valid semester.",
                parent=self.root
            )
            return

        roll_no_text = self.var_roll.get().strip()

        if roll_no_text == "":
            roll_no = None
        else:
            try:
                roll_no = int(roll_no_text)
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Roll No must contain numbers only.",
                    parent=self.root
                )
                return

        dob = self.var_dob.get().strip()

        if dob == "":
            dob = None

        confirm = messagebox.askyesno(
            "Update",
            "Do you want to update this student?",
            parent=self.root
        )

        if not confirm:
            return

        conn = self.connect_db()

        if conn is None:
            return

        cursor = None

        try:

            cursor = conn.cursor()

            query = """
                UPDATE student
                SET
                    dep=%s,
                    course=%s,
                    year=%s,
                    semester=%s,
                    student_name=%s,
                    division=%s,
                    roll_no=%s,
                    gender=%s,
                    dob=%s,
                    email=%s,
                    PhoneNo=%s,
                    address=%s,
                    teacher_name=%s,
                    photosample=%s
                WHERE student_id=%s
            """

            values = (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                semester,
                self.var_std_name.get().strip(),
                self.var_div.get(),
                roll_no,
                self.var_gender.get(),
                dob,
                self.var_email.get().strip(),
                self.var_phone.get().strip(),
                self.var_address.get().strip(),
                self.var_teacher.get().strip(),
                self.var_radio1.get(),
                student_id
            )

            cursor.execute(
                query,
                values
            )

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Student details updated successfully.",
                parent=self.root
            )

            self.fetch_data()

        except Error as e:

            conn.rollback()

            messagebox.showerror(
                "Database Error",
                f"Unable to update data:\n\n{e}",
                parent=self.root
            )

        finally:

            if cursor:
                cursor.close()

            if conn.is_connected():
                conn.close()

    # =========================================================
    # DELETE DATA
    # =========================================================

    def delete_data(self):

        student_id_text = self.var_std_id.get().strip()

        if student_id_text == "":
            messagebox.showerror(
                "Error",
                "Please select a student first.",
                parent=self.root
            )
            return

        try:
            student_id = int(student_id_text)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Invalid Student ID.",
                parent=self.root
            )
            return

        confirm = messagebox.askyesno(
            "Delete",
            "Are you sure you want to delete this student?",
            parent=self.root
        )

        if not confirm:
            return

        conn = self.connect_db()

        if conn is None:
            return

        cursor = None

        try:

            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM student WHERE student_id=%s",
                (student_id,)
            )

            conn.commit()

            # Delete face images

            for photo in self.training_folder.glob(
                f"User.{student_id}.*.jpg"
            ):

                try:
                    photo.unlink()
                except Exception:
                    pass

            messagebox.showinfo(
                "Success",
                "Student deleted successfully.",
                parent=self.root
            )

            self.fetch_data()
            self.reset_data()

        except Error as e:

            conn.rollback()

            messagebox.showerror(
                "Database Error",
                f"Unable to delete data:\n\n{e}",
                parent=self.root
            )

        finally:

            if cursor:
                cursor.close()

            if conn.is_connected():
                conn.close()

    # =========================================================
    # SEARCH
    # =========================================================

    def search_data(self):

        search_by = self.search_combo.get()
        search_value = self.search_entry.get().strip()

        if search_by == "Select":

            messagebox.showerror(
                "Error",
                "Please select a search option.",
                parent=self.root
            )

            return

        if search_value == "":

            messagebox.showerror(
                "Error",
                "Please enter search value.",
                parent=self.root
            )

            return

        column_map = {
            "Student ID": "student_id",
            "Student Name": "student_name",
            "Phone": "PhoneNo"
        }

        column = column_map[search_by]

        conn = self.connect_db()

        if conn is None:
            return

        cursor = None

        try:

            cursor = conn.cursor()

            query = f"""
                SELECT
                    dep,
                    course,
                    year,
                    semester,
                    student_id,
                    student_name,
                    division,
                    roll_no,
                    gender,
                    dob,
                    email,
                    PhoneNo,
                    address,
                    teacher_name,
                    photosample
                FROM student
                WHERE {column} LIKE %s
            """

            cursor.execute(
                query,
                (f"%{search_value}%",)
            )

            rows = cursor.fetchall()

            self.student_table.delete(
                *self.student_table.get_children()
            )

            for row in rows:

                self.student_table.insert(
                    "",
                    END,
                    values=row
                )

            if not rows:

                messagebox.showinfo(
                    "Search",
                    "No student found.",
                    parent=self.root
                )

        except Error as e:

            messagebox.showerror(
                "Database Error",
                f"Search failed:\n\n{e}",
                parent=self.root
            )

        finally:

            if cursor:
                cursor.close()

            if conn.is_connected():
                conn.close()

    # =========================================================
    # RESET
    # =========================================================

    def reset_data(self):

        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")

        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("No")

        self.search_entry.delete(
            0,
            END
        )

        self.search_combo.current(0)

    # =========================================================
    # TAKE PHOTO SAMPLE
    # =========================================================

    def generate_dataset(self):

        student_id_text = self.var_std_id.get().strip()
        student_name = self.var_std_name.get().strip()

        if student_id_text == "":

            messagebox.showerror(
                "Error",
                "Please enter Student ID first.",
                parent=self.root
            )

            return

        try:
            student_id = int(student_id_text)
        except ValueError:

            messagebox.showerror(
                "Error",
                "Student ID must contain numbers only.",
                parent=self.root
            )

            return

        if student_name == "":

            messagebox.showerror(
                "Error",
                "Please enter Student Name first.",
                parent=self.root
            )

            return

        # =====================================================
        # CHECK STUDENT EXISTS
        # =====================================================

        conn = self.connect_db()

        if conn is None:
            return

        cursor = None

        try:

            cursor = conn.cursor()

            cursor.execute(
                "SELECT student_id FROM student WHERE student_id=%s",
                (student_id,)
            )

            result = cursor.fetchone()

        except Error as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to check student:\n\n{e}",
                parent=self.root
            )

            return

        finally:

            if cursor:
                cursor.close()

            if conn.is_connected():
                conn.close()

        if result is None:

            messagebox.showerror(
                "Error",
                "Student is not saved in the database.\n\n"
                "First click SAVE.\n\n"
                "Then click Take Photo Sample.",
                parent=self.root
            )

            return

        # =====================================================
        # HAAR CASCADE
        # =====================================================

        cascade_path = (
            self.project_folder /
            "haarcascade_frontalface_default.xml"
        )

        if not cascade_path.exists():

            cascade_path = (
                Path(cv2.data.haarcascades) /
                "haarcascade_frontalface_default.xml"
            )

        if not cascade_path.exists():

            messagebox.showerror(
                "Face Detector Error",
                "haarcascade_frontalface_default.xml was not found.",
                parent=self.root
            )

            return

        face_detector = cv2.CascadeClassifier(
            str(cascade_path)
        )

        if face_detector.empty():

            messagebox.showerror(
                "Face Detector Error",
                "Could not load Haar Cascade.",
                parent=self.root
            )

            return

        # =====================================================
        # DELETE OLD PHOTOS
        # =====================================================

        for old_photo in self.training_folder.glob(
            f"User.{student_id}.*.jpg"
        ):

            try:
                old_photo.unlink()
            except Exception:
                pass

        # =====================================================
        # CAMERA
        # =====================================================

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():

            messagebox.showerror(
                "Camera Error",
                "Camera could not be opened.\n\n"
                "Check your camera connection.",
                parent=self.root
            )

            return

        messagebox.showinfo(
            "Camera",
            "Camera will open now.\n\n"
            "Look directly at the camera.\n\n"
            "20 photos will be captured automatically.\n\n"
            "Press Q to stop.",
            parent=self.root
        )

        sample_number = 0
        required_samples = 20

        while True:

            ret, img = cap.read()

            if not ret:
                break

            gray = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2GRAY
            )

            faces = face_detector.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(100, 100)
            )

            for (x, y, w, h) in faces:

                cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    (255, 0, 0),
                    2
                )

                if sample_number < required_samples:

                    sample_number += 1

                    face_image = gray[
                        y:y + h,
                        x:x + w
                    ]

                    file_path = (
                        self.training_folder /
                        f"User.{student_id}.{sample_number}.jpg"
                    )

                    cv2.imwrite(
                        str(file_path),
                        face_image
                    )

            cv2.putText(
                img,
                f"Photos: {sample_number}/{required_samples}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            cv2.putText(
                img,
                "Press Q to stop",
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            cv2.imshow(
                "Take Photo Sample",
                img
            )

            key = cv2.waitKey(100) & 0xFF

            if key == ord("q"):
                break

            if sample_number >= required_samples:
                break

        cap.release()
        cv2.destroyAllWindows()

        # =====================================================
        # RESULT
        # =====================================================

        if sample_number > 0:

            self.var_radio1.set("Yes")

            self.update_photo_status(
                student_id
            )

            messagebox.showinfo(
                "Success",
                f"{sample_number} face photos saved successfully!\n\n"
                f"Student ID: {student_id}\n"
                f"Student Name: {student_name}\n\n"
                f"Folder:\n{self.training_folder}",
                parent=self.root
            )

        else:

            messagebox.showwarning(
                "No Photos",
                "No face was detected.\n\n"
                "Please try again.",
                parent=self.root
            )

    # =========================================================
    # UPDATE PHOTO STATUS
    # =========================================================

    def update_photo_status(self, student_id):

        conn = self.connect_db()

        if conn is None:
            return

        cursor = None

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE student
                SET photosample=%s
                WHERE student_id=%s
                """,
                ("Yes", student_id)
            )

            conn.commit()

            self.fetch_data()

        except Error as e:

            conn.rollback()

            messagebox.showerror(
                "Database Error",
                f"Unable to update photo status:\n\n{e}",
                parent=self.root
            )

        finally:

            if cursor:
                cursor.close()

            if conn.is_connected():
                conn.close()


# =============================================================
# MAIN
# =============================================================

if __name__ == "__main__":

    root = Tk()

    app = Student(root)

    root.mainloop()