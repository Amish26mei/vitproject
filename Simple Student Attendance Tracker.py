# Simple Student Attendance Tracker
# Uses only basic functions, loops, if-else, dictionaries, and text files

STUDENTS_FILE = "students.txt"
ATTENDANCE_FILE = "attendance.txt"


def load_students():
    students = {}
    try:
        f = open(STUDENTS_FILE, "r")
        for line in f:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                s_id = parts[0]
                name = parts[1]
                course = parts[2]
                students[s_id] = {"name": name, "course": course}
        f.close()
    except FileNotFoundError:
        pass
    return students


def save_student(student_id, name, course):
    f = open(STUDENTS_FILE, "a")
    f.write(student_id + "," + name + "," + course + "\n")
    f.close()


def load_attendance():
    records = []
    try:
        f = open(ATTENDANCE_FILE, "r")
        for line in f:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                records.append({
                    "id": parts[0],
                    "date": parts[1],
                    "status": parts[2]
                })
        f.close()
    except FileNotFoundError:
        pass
    return records


def save_attendance(student_id, date_str, status):
    f = open(ATTENDANCE_FILE, "a")
    f.write(student_id + "," + date_str + "," + status + "\n")
    f.close()


def register_student():
    print("\n--- Register Student ---")
    s_id = input("Enter Student ID: ").strip()

    if len(s_id) < 2:
        print("Error: Student ID is too short.")
        return

    students = load_students()
    if s_id in students:
        print("Error: Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    if len(name) < 2:
        print("Error: Name is too short.")
        return

    course = input("Enter Course: ").strip()

    save_student(s_id, name, course)
    print("Success: Student registered successfully.")


def mark_attendance():
    print("\n--- Mark Daily Attendance ---")
    s_id = input("Enter Student ID: ").strip()
    students = load_students()

    if s_id not in students:
        print("Error: Student not found. Please register first.")
        return

    date_str = input("Enter Date (YYYY-MM-DD): ").strip()
    parts = date_str.split("-")
    if len(parts) != 3:
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        return

    # Check for duplicate entry on the same date
    records = load_attendance()
    for item in records:
        if item["id"] == s_id and item["date"] == date_str:
            print("Error: Attendance already marked for this date.")
            return

    status_input = input("Enter Status (P for Present / A for Absent): ").strip().upper()
    if status_input == "P" or status_input == "PRESENT":
        status = "PRESENT"
    elif status_input == "A" or status_input == "ABSENT":
        status = "ABSENT"
    else:
        print("Error: Invalid status. Enter P or A.")
        return

    save_attendance(s_id, date_str, status)
    print("Success: Attendance marked as", status, "for", students[s_id]["name"])


def view_student_report():
    print("\n--- Student Attendance Report ---")
    s_id = input("Enter Student ID: ").strip()
    students = load_students()

    if s_id not in students:
        print("Error: Student not found.")
        return

    records = load_attendance()
    total = 0
    present = 0

    for item in records:
        if item["id"] == s_id:
            total = total + 1
            if item["status"] == "PRESENT":
                present = present + 1

    absent = total - present
    if total > 0:
        percentage = (present / total) * 100
    else:
        percentage = 0.0

    print("\n" + "=" * 35)
    print("Student ID :", s_id)
    print("Name       :", students[s_id]["name"])
    print("Course     :", students[s_id]["course"])
    print("Total Days :", total)
    print("Present    :", present)
    print("Absent     :", absent)
    print("Percentage :", round(percentage, 2), "%")

    if percentage >= 75.0:
        print("Status     : Eligible for Exams")
    else:
        print("Status     : Low Attendance (< 75%)")
    print("=" * 35)


def view_defaulters():
    print("\n--- Defaulters List (< 75% Attendance) ---")
    students = load_students()
    records = load_attendance()
    found_any = False

    print("-" * 50)
    print("ID\tName\t\tAttended\tPercentage")
    print("-" * 50)

    for s_id in students:
        total = 0
        present = 0
        for item in records:
            if item["id"] == s_id:
                total = total + 1
                if item["status"] == "PRESENT":
                    present = present + 1

        if total > 0:
            pct = (present / total) * 100
            if pct < 75.0:
                found_any = True
                print(s_id + "\t" + students[s_id]["name"] + "\t\t" + str(present) + "/" + str(total) + "\t\t" + str(round(pct, 2)) + "%")

    if not found_any:
        print("No defaulters found. Everyone is at or above 75%.")
    print("-" * 50)


def list_all_students():
    print("\n--- All Registered Students ---")
    students = load_students()
    if len(students) == 0:
        print("No students found.")
        return

    print("-" * 45)
    for s_id in students:
        print("ID:", s_id, "| Name:", students[s_id]["name"], "| Course:", students[s_id]["course"])
    print("-" * 45)


def main():
    while True:
        print("\n==============================")
        print("  STUDENT ATTENDANCE SYSTEM")
        print("==============================")
        print("1. Register Student")
        print("2. Mark Attendance")
        print("3. View Student Report")
        print("4. View Defaulters (< 75%)")
        print("5. List All Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_student_report()
        elif choice == "4":
            view_defaulters()
        elif choice == "5":
            list_all_students()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")


main()