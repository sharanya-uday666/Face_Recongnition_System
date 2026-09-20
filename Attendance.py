from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from pathlib import Path
import csv
import shutil


class Attendance:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1100x650+50+20")
        self.root.title("Attendance Management System")
        self.root.resizable(False, False)

        # =====================================================
        # PROJECT FOLDER
        # =====================================================

        self.project_folder = Path(__file__).resolve().parent

        self.image_folder = (
            self.project_folder / "college_images"
        )

        # =====================================================
        # VARIABLES
        # =====================================================

        self.var_attendance_id = StringVar()
        self.var_roll_no = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()

        # =====================================================
        # CSV FILE
        # =====================================================

        self.csv_file = (
            self.project_folder / "sharanya.csv"
        )

        self.create_csv_file()

        # =====================================================
        # TOP IMAGE 1
        # =====================================================

        image1_path = (
            self.image_folder /
            "360_F_35308534_WGRVXlymcjQqoRXzeWEfVCOfBHBq9YdW.jpg"
        )

        self.create_image_label(
            image1_path,
            0,
            0,
            550,
            130,
            "STUDENT ATTENDANCE"
        )

        # =====================================================
        # TOP IMAGE 2
        # =====================================================

        image2_path = (
            self.image_folder / "OIP.webp"
        )

        self.create_image_label(
            image2_path,
            550,
            0,
            550,
            130,
            "ATTENDANCE RECORD"
        )

        # =====================================================
        # MAIN FRAME
        # =====================================================

        main_frame = Frame(
            self.root,
            bd=2,
            relief=RIDGE,
            bg="white"
        )

        main_frame.place(
            x=5,
            y=135,
            width=1090,
            height=510
        )

        # =====================================================
        # LEFT FRAME
        # =====================================================

        left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Attendance Details",
            font=("Times New Roman", 14, "bold"),
            bg="white"
        )

        left_frame.place(
            x=5,
            y=5,
            width=500,
            height=495
        )

        # =====================================================
        # LEFT IMAGE
        # =====================================================

        left_image_path = (
            self.image_folder /
            "happy-indian-group-school-kids-students-study-in-class-education-learning-K6P0YK.jpg"
        )

        if left_image_path.exists():

            try:

                left_img = Image.open(
                    left_image_path
                )

                left_img = left_img.resize(
                    (480, 80),
                    Image.Resampling.LANCZOS
                )

                self.left_photo = ImageTk.PhotoImage(
                    left_img
                )

                Label(
                    left_frame,
                    image=self.left_photo
                ).place(
                    x=8,
                    y=5,
                    width=480,
                    height=80
                )

            except Exception:
                pass

        # =====================================================
        # ATTENDANCE ID
        # =====================================================

        Label(
            left_frame,
            text="Attendance ID",
            font=("Times New Roman", 12, "bold"),
            bg="white"
        ).place(
            x=10,
            y=95
        )

        Entry(
            left_frame,
            textvariable=self.var_attendance_id,
            font=("Times New Roman", 12),
            width=25
        ).place(
            x=170,
            y=95
        )

        # =====================================================
        # ROLL NO
        # =====================================================

        Label(
            left_frame,
            text="Roll No",
            font=("Times New Roman", 12, "bold"),
            bg="white"
        ).place(
            x=10,
            y=130
        )

        Entry(
            left_frame,
            textvariable=self.var_roll_no,
            font=("Times New Roman", 12),
            width=25
        ).place(
            x=170,
            y=130
        )

        # =====================================================
        # NAME
        # =====================================================

        Label(
            left_frame,
            text="Name",
            font=("Times New Roman", 12, "bold"),
            bg="white"
        ).place(
            x=10,
            y=165
        )

        Entry(
            left_frame,
            textvariable=self.var_name,
            font=("Times New Roman", 12),
            width=25
        ).place(
            x=170,
            y=165
        )

        # =====================================================
        # DEPARTMENT
        # =====================================================

        Label(
            left_frame,
            text="Department",
            font=("Times New Roman", 12, "bold"),
            bg="white"
        ).place(
            x=10,
            y=200
        )

        self.department_combo = ttk.Combobox(
            left_frame,
            textvariable=self.var_department,
            font=("Times New Roman", 11),
            state="readonly",
            width=23
        )

        self.department_combo["values"] = (
            "Computer Science",
            "Information Science",
            "Electronics and Communication",
            "Electrical and Electronics",
            "Mechanical",
            "Civil",
            "Artificial Intelligence",
            "Data Science",
            "MCA",
            "MBA"
        )

        self.department_combo.place(
            x=170,
            y=200
        )

        # =====================================================
        # TIME
        # =====================================================

        Label(
            left_frame,
            text="Time",
            font=("Times New Roman", 12, "bold"),
            bg="white"
        ).place(
            x=10,
            y=235
        )

        Entry(
            left_frame,
            textvariable=self.var_time,
            font=("Times New Roman", 12),
            width=25
        ).place(
            x=170,
            y=235
        )

        # =====================================================
        # DATE
        # =====================================================

        Label(
            left_frame,
            text="Date",
            font=("Times New Roman", 12, "bold"),
            bg="white"
        ).place(
            x=10,
            y=270
        )

        Entry(
            left_frame,
            textvariable=self.var_date,
            font=("Times New Roman", 12),
            width=25
        ).place(
            x=170,
            y=270
        )

        # =====================================================
        # ATTENDANCE STATUS
        # =====================================================

        Label(
            left_frame,
            text="Attendance Status",
            font=("Times New Roman", 12, "bold"),
            bg="white"
        ).place(
            x=10,
            y=305
        )

        self.status_combo = ttk.Combobox(
            left_frame,
            textvariable=self.var_status,
            font=("Times New Roman", 11),
            state="readonly",
            width=23
        )

        self.status_combo["values"] = (
            "Present",
            "Absent"
        )

        self.status_combo.place(
            x=170,
            y=305
        )

        # =====================================================
        # BUTTON FRAME
        # =====================================================

        button_frame = Frame(
            left_frame,
            bg="white"
        )

        button_frame.place(
            x=10,
            y=345,
            width=475,
            height=130
        )

        # =====================================================
        # SAVE BUTTON
        # =====================================================

        Button(
            button_frame,
            text="Save",
            command=self.save_data,
            font=("Times New Roman", 11, "bold"),
            bg="green",
            fg="white",
            width=18,
            cursor="hand2"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        # =====================================================
        # UPDATE BUTTON
        # =====================================================

        Button(
            button_frame,
            text="Update",
            command=self.update_data,
            font=("Times New Roman", 11, "bold"),
            bg="orange",
            fg="white",
            width=18,
            cursor="hand2"
        ).grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # =====================================================
        # RESET BUTTON
        # =====================================================

        Button(
            button_frame,
            text="Reset",
            command=self.reset_data,
            font=("Times New Roman", 11, "bold"),
            bg="red",
            fg="white",
            width=18,
            cursor="hand2"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        # =====================================================
        # IMPORT CSV BUTTON
        # =====================================================

        Button(
            button_frame,
            text="Import CSV",
            command=self.import_csv,
            font=("Times New Roman", 11, "bold"),
            bg="darkgreen",
            fg="white",
            width=18,
            cursor="hand2"
        ).grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # =====================================================
        # EXPORT CSV BUTTON
        # =====================================================

        Button(
            button_frame,
            text="Export CSV",
            command=self.export_csv,
            font=("Times New Roman", 11, "bold"),
            bg="blue",
            fg="white",
            width=18,
            cursor="hand2"
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            padx=5,
            pady=5
        )

        # =====================================================
        # RIGHT FRAME
        # =====================================================

        right_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Attendance Records",
            font=("Times New Roman", 14, "bold"),
            bg="white"
        )

        right_frame.place(
            x=510,
            y=5,
            width=570,
            height=495
        )

        # =====================================================
        # TABLE FRAME
        # =====================================================

        table_frame = Frame(
            right_frame,
            bd=2,
            relief=RIDGE
        )

        table_frame.place(
            x=5,
            y=5,
            width=555,
            height=460
        )

        # =====================================================
        # SCROLLBARS
        # =====================================================

        scroll_y = ttk.Scrollbar(
            table_frame,
            orient=VERTICAL
        )

        scroll_x = ttk.Scrollbar(
            table_frame,
            orient=HORIZONTAL
        )

        # =====================================================
        # TABLE COLUMNS
        # =====================================================

        columns = (
            "Attendance ID",
            "Roll No",
            "Name",
            "Department",
            "Time",
            "Date",
            "Status"
        )

        # =====================================================
        # TREEVIEW
        # =====================================================

        self.attendance_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_y.config(
            command=self.attendance_table.yview
        )

        scroll_x.config(
            command=self.attendance_table.xview
        )

        for column in columns:

            self.attendance_table.heading(
                column,
                text=column
            )

            self.attendance_table.column(
                column,
                width=120,
                anchor=CENTER
            )

        self.attendance_table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scroll_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scroll_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        table_frame.grid_rowconfigure(
            0,
            weight=1
        )

        table_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.attendance_table.bind(
            "<ButtonRelease-1>",
            self.get_cursor
        )

        # =====================================================
        # LOAD DATA
        # =====================================================

        self.fetch_data()

    # =========================================================
    # IMAGE FUNCTION
    # =========================================================

    def create_image_label(
        self,
        image_path,
        x,
        y,
        width,
        height,
        fallback_text
    ):

        if image_path.exists():

            try:

                img = Image.open(
                    image_path
                )

                img = img.resize(
                    (width, height),
                    Image.Resampling.LANCZOS
                )

                photo = ImageTk.PhotoImage(
                    img
                )

                if not hasattr(
                    self,
                    "_top_images"
                ):
                    self._top_images = []

                self._top_images.append(
                    photo
                )

                Label(
                    self.root,
                    image=photo
                ).place(
                    x=x,
                    y=y,
                    width=width,
                    height=height
                )

                return

            except Exception:
                pass

        Label(
            self.root,
            text=fallback_text,
            font=(
                "Times New Roman",
                25,
                "bold"
            ),
            bg="white"
        ).place(
            x=x,
            y=y,
            width=width,
            height=height
        )

    # =========================================================
    # CSV HEADERS
    # =========================================================

    @staticmethod
    def csv_headers():

        return [
            "Attendance ID",
            "Roll No",
            "Name",
            "Department",
            "Time",
            "Date",
            "Status"
        ]

    # =========================================================
    # NORMALIZE HEADER
    # =========================================================

    @staticmethod
    def normalize_header(header):

        if header is None:
            return ""

        return (
            str(header)
            .replace("\ufeff", "")
            .strip()
            .lower()
            .replace("_", " ")
        )

    # =========================================================
    # FIND COLUMN
    # =========================================================

    def find_column(
        self,
        headers,
        *names
    ):

        normalized_headers = {
            self.normalize_header(header): header
            for header in headers
            if header is not None
        }

        for name in names:

            normalized_name = (
                self.normalize_header(name)
            )

            if normalized_name in normalized_headers:

                return normalized_headers[
                    normalized_name
                ]

        return None

    # =========================================================
    # READ CSV
    # =========================================================

    def read_csv_records(
        self,
        file_path
    ):

        with open(
            file_path,
            "r",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            sample = file.read(4096)

            file.seek(0)

            try:

                dialect = csv.Sniffer().sniff(
                    sample,
                    delimiters=",;\t"
                )

            except csv.Error:

                dialect = csv.excel

            reader = csv.DictReader(
                file,
                dialect=dialect
            )

            headers = reader.fieldnames

            if not headers:

                raise ValueError(
                    "The CSV file is empty or "
                    "has no header row."
                )

            # =================================================
            # FIND COLUMNS
            # =================================================

            attendance_id_column = self.find_column(
                headers,
                "Attendance ID",
                "Student ID",
                "attendance_id",
                "student_id"
            )

            roll_no_column = self.find_column(
                headers,
                "Roll No",
                "Roll Number",
                "roll_no"
            )

            name_column = self.find_column(
                headers,
                "Name",
                "Student Name",
                "student_name"
            )

            department_column = self.find_column(
                headers,
                "Department",
                "Dept"
            )

            time_column = self.find_column(
                headers,
                "Time",
                "Attendance Time"
            )

            date_column = self.find_column(
                headers,
                "Date",
                "Attendance Date"
            )

            status_column = self.find_column(
                headers,
                "Status",
                "Attendance Status"
            )

            # =================================================
            # CHECK MISSING COLUMNS
            # =================================================

            required = {
                "Attendance ID": attendance_id_column,
                "Roll No": roll_no_column,
                "Name": name_column,
                "Department": department_column,
                "Time": time_column,
                "Date": date_column,
                "Status": status_column
            }

            missing = []

            for name, column in required.items():

                if column is None:

                    missing.append(name)

            if missing:

                raise ValueError(
                    "The selected CSV is missing "
                    "these columns:\n\n"
                    + "\n".join(missing)
                )

            # =================================================
            # READ RECORDS
            # =================================================

            records = []

            for row in reader:

                values = [

                    str(
                        row.get(
                            attendance_id_column,
                            ""
                        ) or ""
                    ).strip(),

                    str(
                        row.get(
                            roll_no_column,
                            ""
                        ) or ""
                    ).strip(),

                    str(
                        row.get(
                            name_column,
                            ""
                        ) or ""
                    ).strip(),

                    str(
                        row.get(
                            department_column,
                            ""
                        ) or ""
                    ).strip(),

                    str(
                        row.get(
                            time_column,
                            ""
                        ) or ""
                    ).strip(),

                    str(
                        row.get(
                            date_column,
                            ""
                        ) or ""
                    ).strip(),

                    str(
                        row.get(
                            status_column,
                            ""
                        ) or ""
                    ).strip()
                ]

                if not any(values):

                    continue

                records.append(values)

        return records

    # =========================================================
    # CHECK CSV LOCK
    # =========================================================

    def is_file_locked(self):

        try:

            with open(
                self.csv_file,
                "a",
                newline="",
                encoding="utf-8"
            ):
                pass

            return False

        except PermissionError:

            return True

        except OSError as e:

            if (
                getattr(
                    e,
                    "winerror",
                    None
                ) == 32
                or "busy" in str(e).lower()
                or "locked" in str(e).lower()
            ):

                return True

            return False

    # =========================================================
    # LOCK MESSAGE
    # =========================================================

    def show_file_locked_message(self):

        messagebox.showerror(
            "CSV File Is Busy",
            "sharanya.csv is currently being "
            "used by another program.\n\n"
            "Please close:\n\n"
            "• Excel\n"
            "• Notepad\n"
            "• Another VS Code window\n"
            "• Any program using sharanya.csv\n\n"
            "If OneDrive is synchronizing the file, "
            "wait a few seconds and try again."
        )

    # =========================================================
    # CREATE CSV
    # =========================================================

    def create_csv_file(self):

        if self.csv_file.exists():

            return

        try:

            with open(
                self.csv_file,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow(
                    self.csv_headers()
                )

        except (
            PermissionError,
            OSError
        ) as e:

            messagebox.showerror(
                "CSV File Error",
                "Unable to create sharanya.csv.\n\n"
                "The file may be locked or being "
                "used by OneDrive.\n\n"
                f"Details:\n{e}"
            )

    # =========================================================
    # FETCH DATA
    # =========================================================

    def fetch_data(self):

        self.attendance_table.delete(
            *self.attendance_table.get_children()
        )

        try:

            records = self.read_csv_records(
                self.csv_file
            )

            for values in records:

                if not values[0]:

                    continue

                self.attendance_table.insert(
                    "",
                    END,
                    values=tuple(values)
                )

        except FileNotFoundError:

            self.create_csv_file()

        except PermissionError:

            self.show_file_locked_message()

        except ValueError as e:

            messagebox.showerror(
                "CSV Error",
                str(e)
            )

        except UnicodeDecodeError:

            messagebox.showerror(
                "CSV Error",
                "Unable to read the CSV because "
                "its text encoding is not supported."
            )

        except OSError as e:

            if (
                getattr(
                    e,
                    "winerror",
                    None
                ) == 32
                or "busy" in str(e).lower()
                or "locked" in str(e).lower()
            ):

                self.show_file_locked_message()

            else:

                messagebox.showerror(
                    "CSV Error",
                    f"Unable to load data.\n\n{e}"
                )

        except Exception as e:

            messagebox.showerror(
                "CSV Error",
                f"Unable to load data.\n\n{e}"
            )

    # =========================================================
    # SAVE DATA
    # =========================================================

    def save_data(self):

        values = [

            self.var_attendance_id.get().strip(),

            self.var_roll_no.get().strip(),

            self.var_name.get().strip(),

            self.var_department.get().strip(),

            self.var_time.get().strip(),

            self.var_date.get().strip(),

            self.var_status.get().strip()
        ]

        # =====================================================
        # EMPTY CHECK
        # =====================================================

        if "" in values:

            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )

            return

        # =====================================================
        # LOCK CHECK
        # =====================================================

        if self.is_file_locked():

            self.show_file_locked_message()

            return

        try:

            if not self.csv_file.exists():

                self.create_csv_file()

            with open(
                self.csv_file,
                "a",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow(
                    values
                )

            messagebox.showinfo(
                "Success",
                "Attendance saved successfully."
            )

            self.fetch_data()

            self.reset_data()

        except PermissionError:

            self.show_file_locked_message()

        except OSError as e:

            if (
                getattr(
                    e,
                    "winerror",
                    None
                ) == 32
                or "busy" in str(e).lower()
                or "locked" in str(e).lower()
            ):

                self.show_file_locked_message()

            else:

                messagebox.showerror(
                    "Save Error",
                    f"Unable to save attendance.\n\n{e}"
                )

        except Exception as e:

            messagebox.showerror(
                "Save Error",
                f"Unable to save attendance.\n\n{e}"
            )

    # =========================================================
    # GET SELECTED ROW
    # =========================================================

    def get_cursor(
        self,
        event=None
    ):

        selected = (
            self.attendance_table.focus()
        )

        if not selected:

            return

        values = (
            self.attendance_table.item(
                selected,
                "values"
            )
        )

        if not values:

            return

        self.var_attendance_id.set(
            values[0]
        )

        self.var_roll_no.set(
            values[1]
        )

        self.var_name.set(
            values[2]
        )

        self.var_department.set(
            values[3]
        )

        self.var_time.set(
            values[4]
        )

        self.var_date.set(
            values[5]
        )

        self.var_status.set(
            values[6]
        )

    # =========================================================
    # UPDATE DATA
    # =========================================================

    def update_data(self):

        selected = (
            self.attendance_table.focus()
        )

        if not selected:

            messagebox.showerror(
                "Error",
                "Please select a record "
                "from the table."
            )

            return

        old_values = list(
            self.attendance_table.item(
                selected,
                "values"
            )
        )

        new_values = [

            self.var_attendance_id.get().strip(),

            self.var_roll_no.get().strip(),

            self.var_name.get().strip(),

            self.var_department.get().strip(),

            self.var_time.get().strip(),

            self.var_date.get().strip(),

            self.var_status.get().strip()
        ]

        if "" in new_values:

            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )

            return

        if self.is_file_locked():

            self.show_file_locked_message()

            return

        try:

            records = self.read_csv_records(
                self.csv_file
            )

            updated = False

            for index, record in enumerate(
                records
            ):

                if list(record) == old_values:

                    records[index] = new_values

                    updated = True

                    break

            if not updated:

                messagebox.showerror(
                    "Update Error",
                    "The selected record could "
                    "not be found in sharanya.csv."
                )

                return

            with open(
                self.csv_file,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow(
                    self.csv_headers()
                )

                writer.writerows(
                    records
                )

            messagebox.showinfo(
                "Success",
                "Attendance updated successfully."
            )

            self.fetch_data()

            self.reset_data()

        except PermissionError:

            self.show_file_locked_message()

        except ValueError as e:

            messagebox.showerror(
                "Update Error",
                str(e)
            )

        except OSError as e:

            if (
                getattr(
                    e,
                    "winerror",
                    None
                ) == 32
                or "busy" in str(e).lower()
                or "locked" in str(e).lower()
            ):

                self.show_file_locked_message()

            else:

                messagebox.showerror(
                    "Update Error",
                    f"Unable to update data.\n\n{e}"
                )

        except Exception as e:

            messagebox.showerror(
                "Update Error",
                f"Unable to update data.\n\n{e}"
            )

    # =========================================================
    # RESET
    # =========================================================

    def reset_data(self):

        self.var_attendance_id.set("")

        self.var_roll_no.set("")

        self.var_name.set("")

        self.var_department.set("")

        self.var_time.set("")

        self.var_date.set("")

        self.var_status.set("")

        self.attendance_table.selection_remove(
            self.attendance_table.selection()
        )

    # =========================================================
    # IMPORT CSV
    # =========================================================

    def import_csv(self):

        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[
                ("CSV Files", "*.csv"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:

            return

        try:

            rows = self.read_csv_records(
                file_path
            )

            if not rows:

                messagebox.showwarning(
                    "Import CSV",
                    "The selected CSV contains "
                    "no attendance records."
                )

                return

            selected_path = (
                Path(file_path).resolve()
            )

            own_path = (
                self.csv_file.resolve()
            )

            # =================================================
            # SAME FILE
            # =================================================

            if selected_path == own_path:

                self.fetch_data()

                messagebox.showinfo(
                    "Success",
                    "sharanya.csv is already the "
                    "current attendance file.\n\n"
                    f"{len(rows)} record(s) found."
                )

                return

            # =================================================
            # LOCK CHECK
            # =================================================

            if self.is_file_locked():

                self.show_file_locked_message()

                return

            # =================================================
            # WRITE IMPORTED DATA
            # =================================================

            with open(
                self.csv_file,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow(
                    self.csv_headers()
                )

                writer.writerows(
                    rows
                )

            self.fetch_data()

            messagebox.showinfo(
                "Success",
                "CSV imported successfully.\n\n"
                f"{len(rows)} attendance "
                "record(s) imported."
            )

        except FileNotFoundError:

            messagebox.showerror(
                "Import Error",
                "The selected CSV file "
                "could not be found."
            )

        except PermissionError:

            self.show_file_locked_message()

        except UnicodeDecodeError:

            messagebox.showerror(
                "Import Error",
                "The CSV file encoding "
                "is not supported."
            )

        except ValueError as e:

            messagebox.showerror(
                "Invalid CSV",
                str(e)
            )

        except csv.Error as e:

            messagebox.showerror(
                "CSV Error",
                "The CSV file is not formatted "
                "correctly.\n\n"
                f"{e}"
            )

        except OSError as e:

            if (
                getattr(
                    e,
                    "winerror",
                    None
                ) == 32
                or "busy" in str(e).lower()
                or "locked" in str(e).lower()
            ):

                self.show_file_locked_message()

            else:

                messagebox.showerror(
                    "Import Error",
                    f"Unable to import CSV.\n\n{e}"
                )

        except Exception as e:

            messagebox.showerror(
                "Import Error",
                f"Unable to import CSV.\n\n{e}"
            )

    # =========================================================
    # EXPORT CSV
    # =========================================================

    def export_csv(self):

        save_path = filedialog.asksaveasfilename(
            title="Export Attendance CSV",
            defaultextension=".csv",
            filetypes=[
                ("CSV Files", "*.csv")
            ]
        )

        if not save_path:

            return

        try:

            if not self.csv_file.exists():

                self.create_csv_file()

            shutil.copyfile(
                self.csv_file,
                save_path
            )

            messagebox.showinfo(
                "Success",
                "Attendance exported successfully."
            )

        except PermissionError:

            messagebox.showerror(
                "Export Error",
                "The CSV file is currently being "
                "used by another program.\n\n"
                "Please close the CSV file "
                "and try again."
            )

        except OSError as e:

            if (
                getattr(
                    e,
                    "winerror",
                    None
                ) == 32
                or "busy" in str(e).lower()
                or "locked" in str(e).lower()
            ):

                messagebox.showerror(
                    "CSV File Is Busy",
                    "sharanya.csv is currently "
                    "being used by another program.\n\n"
                    "Please close Excel, Notepad, "
                    "or another program using "
                    "the CSV file and try again."
                )

            else:

                messagebox.showerror(
                    "Export Error",
                    f"Unable to export CSV.\n\n{e}"
                )

        except Exception as e:

            messagebox.showerror(
                "Export Error",
                f"Unable to export CSV.\n\n{e}"
            )


# =============================================================
# MAIN PROGRAM
# =============================================================

if __name__ == "__main__":

    root = Tk()

    app = Attendance(root)

    root.mainloop()