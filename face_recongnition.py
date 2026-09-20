import cv2
import csv
import os
from pathlib import Path
from datetime import datetime
from tkinter import *
from tkinter import messagebox


class Face_Recognition:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1200x700+50+20")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)

        # =====================================================
        # PROJECT FOLDER
        # =====================================================

        self.project_folder = Path(__file__).resolve().parent

        print("\n========================================")
        print("PROJECT FOLDER")
        print("========================================")
        print(self.project_folder)

        # =====================================================
        # CLASSIFIER
        # =====================================================

        self.classifier_path = self.project_folder / "classifier.xml"

        # =====================================================
        # STUDENT DETAILS CSV
        # =====================================================

        self.student_details_folder = (
            self.project_folder / "StudentDetails"
        )

        self.student_details_file = (
            self.student_details_folder / "student_details.csv"
        )

        self.student_details_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        # =====================================================
        # ATTENDANCE CSV
        # =====================================================

        self.attendance_file = (
            self.project_folder / "sharanya.csv"
        )

        print("\n========================================")
        print("ATTENDANCE FILE")
        print("========================================")
        print(self.attendance_file)
        print("========================================")

        # =====================================================
        # STUDENT DETAILS
        # =====================================================

        self.student_details = {}

        self.load_student_details()

        # =====================================================
        # OPENCV FACE MODULE CHECK
        # =====================================================

        if not hasattr(cv2, "face"):

            messagebox.showerror(
                "OpenCV Error",
                "cv2.face is not available.\n\n"
                "Install opencv-contrib-python."
            )

            self.root.destroy()
            return

        # =====================================================
        # CREATE RECOGNIZER
        # =====================================================

        try:

            self.recognizer = (
                cv2.face.LBPHFaceRecognizer_create()
            )

        except Exception as e:

            messagebox.showerror(
                "Recognizer Error",
                f"Could not create face recognizer.\n\n{e}"
            )

            self.root.destroy()
            return

        # =====================================================
        # CHECK CLASSIFIER
        # =====================================================

        if not self.classifier_path.exists():

            messagebox.showerror(
                "Classifier Not Found",
                "classifier.xml was not found.\n\n"
                f"Expected location:\n\n"
                f"{self.classifier_path}\n\n"
                "Please train your face data first."
            )

            self.root.destroy()
            return

        # =====================================================
        # LOAD CLASSIFIER
        # =====================================================

        try:

            self.recognizer.read(
                str(self.classifier_path)
            )

            print("Classifier loaded successfully.")

        except Exception as e:

            messagebox.showerror(
                "Classifier Error",
                f"Unable to load classifier.xml.\n\n{e}"
            )

            self.root.destroy()
            return

        # =====================================================
        # HAAR CASCADE
        # =====================================================

        haar_path = (
            Path(cv2.data.haarcascades)
            / "haarcascade_frontalface_default.xml"
        )

        # If OpenCV's Haar file is not found,
        # try project folder.

        if not haar_path.exists():

            haar_path = (
                self.project_folder
                / "haarcascade_frontalface_default.xml"
            )

        if not haar_path.exists():

            messagebox.showerror(
                "Haar Cascade Error",
                "haarcascade_frontalface_default.xml "
                "was not found.\n\n"
                f"Expected:\n{haar_path}"
            )

            self.root.destroy()
            return

        self.face_cascade = cv2.CascadeClassifier(
            str(haar_path)
        )

        if self.face_cascade.empty():

            messagebox.showerror(
                "Haar Cascade Error",
                "Unable to load Haar Cascade."
            )

            self.root.destroy()
            return

        print("Haar Cascade loaded successfully.")

        # =====================================================
        # CLEAN ATTENDANCE FILE
        # =====================================================

        self.clean_attendance_file()

        # =====================================================
        # KEEP TRACK OF ATTENDANCE
        # =====================================================

        self.marked_today = set()

        self.load_today_attendance()

        # =====================================================
        # GUI
        # =====================================================

        title = Label(
            self.root,
            text="FACE RECOGNITION SYSTEM",
            font=("times new roman", 28, "bold"),
            bg="darkblue",
            fg="white"
        )

        title.place(
            x=0,
            y=0,
            width=1200,
            height=60
        )

        # =====================================================
        # INFORMATION
        # =====================================================

        info = Label(
            self.root,
            text=(
                "Face Recognition System\n"
                "Click the button below to start recognition"
            ),
            font=("times new roman", 16, "bold"),
            fg="darkblue"
        )

        info.place(
            x=0,
            y=80,
            width=1200,
            height=70
        )

        # =====================================================
        # START BUTTON
        # =====================================================

        start_button = Button(
            self.root,
            text="START FACE RECOGNITION",
            command=self.start_recognition,
            cursor="hand2",
            font=("times new roman", 16, "bold"),
            bg="darkblue",
            fg="white",
            activebackground="blue",
            activeforeground="white"
        )

        start_button.place(
            x=430,
            y=190,
            width=340,
            height=50
        )

        # =====================================================
        # CLOSE BUTTON
        # =====================================================

        close_button = Button(
            self.root,
            text="CLOSE",
            command=self.close_window,
            cursor="hand2",
            font=("times new roman", 14, "bold"),
            bg="red",
            fg="white"
        )

        close_button.place(
            x=500,
            y=270,
            width=200,
            height=45
        )

        # =====================================================
        # STATUS
        # =====================================================

        self.status_label = Label(
            self.root,
            text="Ready to recognize faces",
            font=("times new roman", 14, "bold"),
            fg="green"
        )

        self.status_label.place(
            x=0,
            y=350,
            width=1200,
            height=40
        )

        # =====================================================
        # ATTENDANCE LOCATION LABEL
        # =====================================================

        file_label = Label(
            self.root,
            text=f"Attendance file: {self.attendance_file}",
            font=("Arial", 10),
            fg="gray"
        )

        file_label.place(
            x=0,
            y=410,
            width=1200,
            height=30
        )

    # =========================================================
    # LOAD STUDENT DETAILS
    # =========================================================

    def load_student_details(self):

        print("\n========================================")
        print("LOADING STUDENT DETAILS")
        print("========================================")

        print(
            "Student Details File:",
            self.student_details_file
        )

        # -----------------------------------------------------
        # CREATE FILE IF NOT EXISTS
        # -----------------------------------------------------

        if not self.student_details_file.exists():

            try:

                with open(
                    self.student_details_file,
                    "w",
                    newline="",
                    encoding="utf-8"
                ) as file:

                    writer = csv.writer(file)

                    writer.writerow([
                        "Student ID",
                        "Name",
                        "Department",
                        "Roll No"
                    ])

                print(
                    "student_details.csv created."
                )

            except Exception as e:

                print(
                    "Could not create student details:",
                    e
                )

            return

        # -----------------------------------------------------
        # READ FILE
        # -----------------------------------------------------

        try:

            with open(
                self.student_details_file,
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.DictReader(file)

                print(
                    "CSV Columns:",
                    reader.fieldnames
                )

                for row in reader:

                    student_id = (
                        row.get("Student ID")
                        or row.get("student_id")
                        or row.get("ID")
                        or row.get("Id")
                        or ""
                    )

                    name = (
                        row.get("Name")
                        or row.get("name")
                        or row.get("Student Name")
                        or row.get("student_name")
                        or "Unknown"
                    )

                    department = (
                        row.get("Department")
                        or row.get("department")
                        or row.get("Dept")
                        or row.get("dept")
                        or "Unknown"
                    )

                    roll_no = (
                        row.get("Roll No")
                        or row.get("Roll Number")
                        or row.get("roll_no")
                        or row.get("Roll")
                        or "Unknown"
                    )

                    student_id = str(
                        student_id
                    ).strip()

                    name = str(
                        name
                    ).strip()

                    department = str(
                        department
                    ).strip()

                    roll_no = str(
                        roll_no
                    ).strip()

                    if student_id:

                        self.student_details[
                            student_id
                        ] = {
                            "name": name,
                            "department": department,
                            "roll_no": roll_no
                        }

                        print(
                            f"FOUND: "
                            f"{self.student_details[student_id]}"
                        )

            print(
                "Total Students:",
                len(self.student_details)
            )

        except Exception as e:

            print(
                "Student CSV Error:",
                e
            )

            messagebox.showerror(
                "Student Details Error",
                f"Unable to read student_details.csv.\n\n{e}"
            )

    # =========================================================
    # GET STUDENT DETAILS
    # =========================================================

    def get_student_details(self, student_id):

        student_id = str(
            student_id
        ).strip()

        print(
            "Searching Student ID:",
            student_id
        )

        if student_id in self.student_details:

            print(
                "FOUND:",
                self.student_details[student_id]
            )

            return self.student_details[
                student_id
            ]

        print(
            "NOT FOUND:",
            student_id
        )

        return {
            "name": "Unknown",
            "department": "Unknown",
            "roll_no": "Unknown"
        }

    # =========================================================
    # CLEAN ATTENDANCE CSV
    # =========================================================

    def clean_attendance_file(self):

        header = [
            "Student ID",
            "Name",
            "Department",
            "Roll No",
            "Date",
            "Time",
            "Status"
        ]

        # -----------------------------------------------------
        # CREATE FILE IF NOT EXISTS
        # -----------------------------------------------------

        if not self.attendance_file.exists():

            try:

                with open(
                    self.attendance_file,
                    "w",
                    newline="",
                    encoding="utf-8"
                ) as file:

                    writer = csv.writer(file)
                    writer.writerow(header)

                print(
                    "Created sharanya.csv"
                )

            except Exception as e:

                messagebox.showerror(
                    "Attendance Error",
                    f"Cannot create sharanya.csv.\n\n{e}"
                )

            return

        # -----------------------------------------------------
        # READ EXISTING FILE
        # -----------------------------------------------------

        valid_rows = []

        try:

            with open(
                self.attendance_file,
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.reader(file)

                for row in reader:

                    # Ignore completely empty rows

                    if not row:
                        continue

                    # Ignore rows where every column is empty

                    if all(
                        str(value).strip() == ""
                        for value in row
                    ):
                        continue

                    # Ignore header

                    if (
                        len(row) >= 1
                        and row[0].strip().lower()
                        == "student id"
                    ):
                        continue

                    # Only accept proper attendance rows

                    if len(row) >= 7:

                        cleaned_row = [
                            str(value).strip()
                            for value in row[:7]
                        ]

                        # Student ID must not be empty

                        if cleaned_row[0] != "":

                            valid_rows.append(
                                cleaned_row
                            )

            # -------------------------------------------------
            # REWRITE CLEAN FILE
            # -------------------------------------------------

            with open(
                self.attendance_file,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow(header)

                for row in valid_rows:

                    writer.writerow(row)

            print(
                "Attendance CSV cleaned successfully."
            )

            print(
                "Valid attendance records:",
                len(valid_rows)
            )

        except PermissionError:

            messagebox.showerror(
                "CSV Permission Error",
                "Please CLOSE sharanya.csv "
                "before running the program."
            )

        except Exception as e:

            print(
                "CSV cleaning error:",
                e
            )

    # =========================================================
    # LOAD TODAY'S ATTENDANCE
    # =========================================================

    def load_today_attendance(self):

        today = datetime.now().strftime(
            "%Y-%m-%d"
        )

        print("\n========================================")
        print("LOADING TODAY'S ATTENDANCE")
        print("DATE:", today)
        print("========================================")

        if not self.attendance_file.exists():

            return

        try:

            with open(
                self.attendance_file,
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:

                    student_id = str(
                        row.get("Student ID", "")
                    ).strip()

                    date = str(
                        row.get("Date", "")
                    ).strip()

                    if (
                        student_id
                        and
                        date == today
                    ):

                        self.marked_today.add(
                            student_id
                        )

                        print(
                            "Already marked:",
                            student_id
                        )

            print(
                "Today's marked students:",
                self.marked_today
            )

        except Exception as e:

            print(
                "Could not load today's attendance:",
                e
            )

    # =========================================================
    # CHECK ALREADY MARKED
    # =========================================================

    def already_marked(self, student_id):

        student_id = str(
            student_id
        ).strip()

        today = datetime.now().strftime(
            "%Y-%m-%d"
        )

        # -----------------------------------------------------
        # FIRST CHECK MEMORY
        # -----------------------------------------------------

        if student_id in self.marked_today:

            print(
                f"Student {student_id} "
                f"already marked today."
            )

            return True

        # -----------------------------------------------------
        # CHECK CSV
        # -----------------------------------------------------

        if not self.attendance_file.exists():

            return False

        try:

            with open(
                self.attendance_file,
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:

                    saved_id = str(
                        row.get("Student ID", "")
                    ).strip()

                    saved_date = str(
                        row.get("Date", "")
                    ).strip()

                    if (
                        saved_id == student_id
                        and
                        saved_date == today
                    ):

                        self.marked_today.add(
                            student_id
                        )

                        return True

        except Exception as e:

            print(
                "Attendance checking error:",
                e
            )

        return False

    # =========================================================
    # MARK ATTENDANCE
    # =========================================================

    def mark_attendance(self, student_id):

        student_id = str(
            student_id
        ).strip()

        print("\n========================================")
        print("STARTING ATTENDANCE SAVE")
        print("========================================")

        print(
            "Student ID:",
            student_id
        )

        print(
            "Attendance file:",
            self.attendance_file
        )

        # -----------------------------------------------------
        # CHECK DUPLICATE
        # -----------------------------------------------------

        if self.already_marked(student_id):

            print(
                "\n========================================"
            )
            print(
                "ALREADY MARKED TODAY"
            )
            print(
                "========================================"
            )

            return False

        # -----------------------------------------------------
        # GET STUDENT
        # -----------------------------------------------------

        student = self.get_student_details(
            student_id
        )

        name = student["name"]

        department = student["department"]

        roll_no = student["roll_no"]

        print(
            "Name:",
            name
        )

        print(
            "Department:",
            department
        )

        print(
            "Roll No:",
            roll_no
        )

        # -----------------------------------------------------
        # DON'T SAVE UNKNOWN STUDENT
        # -----------------------------------------------------

        if name == "Unknown":

            print(
                "Student not found. "
                "Attendance NOT saved."
            )

            return False

        # -----------------------------------------------------
        # DATE AND TIME
        # -----------------------------------------------------

        now = datetime.now()

        date = now.strftime(
            "%Y-%m-%d"
        )

        time = now.strftime(
            "%H:%M:%S"
        )

        # -----------------------------------------------------
        # SAVE TO CSV
        # -----------------------------------------------------

        try:

            with open(
                self.attendance_file,
                "a",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    student_id,
                    name,
                    department,
                    roll_no,
                    date,
                    time,
                    "Present"
                ])

                file.flush()
                os.fsync(
                    file.fileno()
                )

            # -------------------------------------------------
            # ADD TO MEMORY
            # -------------------------------------------------

            self.marked_today.add(
                student_id
            )

            print("\n========================================")
            print("ATTENDANCE SAVED SUCCESSFULLY")
            print("========================================")

            print(
                "Student ID :",
                student_id
            )

            print(
                "Name       :",
                name
            )

            print(
                "Department :",
                department
            )

            print(
                "Roll No    :",
                roll_no
            )

            print(
                "Date       :",
                date
            )

            print(
                "Time       :",
                time
            )

            print(
                "Status     : Present"
            )

            print(
                "FILE:",
                self.attendance_file
            )

            print("========================================")

            return True

        except PermissionError:

            messagebox.showerror(
                "CSV Permission Error",
                "Unable to save attendance.\n\n"
                "Please CLOSE sharanya.csv "
                "in Excel or VS Code."
            )

            return False

        except Exception as e:

            print(
                "CSV SAVE ERROR:",
                e
            )

            messagebox.showerror(
                "CSV Save Error",
                f"Attendance could not be saved.\n\n{e}"
            )

            return False

    # =========================================================
    # START RECOGNITION
    # =========================================================

    def start_recognition(self):

        self.status_label.config(
            text="Starting camera...",
            fg="blue"
        )

        self.root.update()

        # =====================================================
        # OPEN CAMERA
        # =====================================================

        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():

            messagebox.showerror(
                "Camera Error",
                "Unable to open camera.\n\n"
                "Please check your webcam."
            )

            self.status_label.config(
                text="Camera could not be opened",
                fg="red"
            )

            return

        self.status_label.config(
            text="Camera started. Looking for faces...",
            fg="green"
        )

        self.root.update()

        # =====================================================
        # RECOGNITION LOOP
        # =====================================================

        while True:

            ret, frame = video_capture.read()

            if not ret:

                print(
                    "Unable to read camera frame."
                )

                break

            # =================================================
            # GRAYSCALE
            # =================================================

            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )

            # =================================================
            # FACE DETECTION
            # =================================================

            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(100, 100)
            )

            # =================================================
            # PROCESS FACES
            # =================================================

            for (x, y, w, h) in faces:

                face_gray = gray[
                    y:y + h,
                    x:x + w
                ]

                try:

                    student_id, confidence = (
                        self.recognizer.predict(
                            face_gray
                        )
                    )

                    print(
                        f"Predicted ID: {student_id} "
                        f"Confidence: {confidence}"
                    )

                    # =================================================
                    # RECOGNIZED
                    # =================================================

                    if confidence < 70:

                        student = (
                            self.get_student_details(
                                student_id
                            )
                        )

                        name = student["name"]

                        department = (
                            student["department"]
                        )

                        roll_no = student["roll_no"]

                        confidence_percent = max(
                            0,
                            int(100 - confidence)
                        )

                        # -------------------------------------------------
                        # GREEN BOX
                        # -------------------------------------------------

                        cv2.rectangle(
                            frame,
                            (x, y),
                            (x + w, y + h),
                            (0, 255, 0),
                            2
                        )

                        # -------------------------------------------------
                        # NAME
                        # -------------------------------------------------

                        cv2.putText(
                            frame,
                            f"Name: {name}",
                            (x, max(30, y - 90)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.65,
                            (0, 255, 0),
                            2
                        )

                        # -------------------------------------------------
                        # DEPARTMENT
                        # -------------------------------------------------

                        cv2.putText(
                            frame,
                            f"Department: {department}",
                            (x, max(55, y - 65)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.55,
                            (0, 255, 0),
                            2
                        )

                        # -------------------------------------------------
                        # ROLL NO
                        # -------------------------------------------------

                        cv2.putText(
                            frame,
                            f"Roll No: {roll_no}",
                            (x, max(80, y - 40)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.60,
                            (0, 255, 0),
                            2
                        )

                        # -------------------------------------------------
                        # STUDENT ID
                        # -------------------------------------------------

                        cv2.putText(
                            frame,
                            f"Student ID: {student_id}",
                            (x, y + h + 25),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.55,
                            (0, 255, 0),
                            2
                        )

                        # -------------------------------------------------
                        # CONFIDENCE
                        # -------------------------------------------------

                        cv2.putText(
                            frame,
                            f"Confidence: {confidence_percent}%",
                            (x, y + h + 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.55,
                            (0, 255, 0),
                            2
                        )

                        # =================================================
                        # ATTENDANCE
                        # =================================================

                        if student_id not in self.marked_today:

                            attendance_saved = (
                                self.mark_attendance(
                                    student_id
                                )
                            )

                            if attendance_saved:

                                self.status_label.config(
                                    text=(
                                        f"Attendance marked successfully: "
                                        f"{name} | "
                                        f"ID: {student_id}"
                                    ),
                                    fg="green"
                                )

                                self.root.update()

                        else:

                            self.status_label.config(
                                text=(
                                    f"{name} is already "
                                    f"Present today"
                                ),
                                fg="blue"
                            )

                    # =================================================
                    # UNKNOWN
                    # =================================================

                    else:

                        cv2.rectangle(
                            frame,
                            (x, y),
                            (x + w, y + h),
                            (0, 0, 255),
                            2
                        )

                        cv2.putText(
                            frame,
                            "UNKNOWN FACE",
                            (x, max(30, y - 15)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 0, 255),
                            2
                        )

                        self.status_label.config(
                            text="Unknown face detected",
                            fg="red"
                        )

                except Exception as e:

                    print(
                        "Recognition error:",
                        e
                    )

            # =================================================
            # SHOW CAMERA
            # =================================================

            cv2.imshow(
                "Face Recognition - Press Q to Exit",
                frame
            )

            # =================================================
            # KEY
            # =================================================

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):

                break

            if key == 27:

                break

        # =====================================================
        # RELEASE CAMERA
        # =====================================================

        video_capture.release()

        cv2.destroyAllWindows()

        self.status_label.config(
            text="Face recognition stopped",
            fg="blue"
        )

    # =========================================================
    # CLOSE
    # =========================================================

    def close_window(self):

        cv2.destroyAllWindows()

        self.root.destroy()


# =============================================================
# MAIN PROGRAM
# =============================================================

if __name__ == "__main__":

    root = Tk()

    app = Face_Recognition(root)

    root.mainloop()