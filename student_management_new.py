# =========================
# ANSI COLOR CODES
# =========================
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"


# =========================
# Global student list
# =========================
students = []


# =========================
# Header
# =========================
def header(title):
    print(f"\n{CYAN}{'=' * 40}{RESET}")
    print(f"{CYAN}{BOLD}{title.center(40)}{RESET}")
    print(f"{CYAN}{'=' * 40}{RESET}")


# =========================
# Menu
# =========================
def show_menu():
    header("STUDENT MANAGEMENT SYSTEM")
    print(f"{YELLOW}➤ 1. Add a student{RESET}")
    print(f"{YELLOW}➤ 2. View all students{RESET}")
    print(f"{YELLOW}➤ 3. Search student by ID{RESET}")
    print(f"{YELLOW}➤ 4. Update marks{RESET}")
    print(f"{YELLOW}➤ 5. Delete a student{RESET}")
    print(f"{YELLOW}➤ 6. Exit program{RESET}")


# =========================
# Add student
# =========================
def add_student():
    header("ADD STUDENT")

    student_id = int(input("Enter Student ID: "))
    for s in students:
        if s['id'] == student_id:
            print(f"{RED}✖ Student with ID {student_id} already exists!{RESET}")
            return

    student = {}
    student["id"] = student_id
    student["name"] = input("Enter Student Name: ")
    student["age"] = int(input("Enter Age: "))

    student["subjects"] = tuple(
        input("Enter Subjects (comma separated): ").split(",")
    )
    student["marks"] = {}

    for subject in student["subjects"]:
        mark = int(input(f"Enter {subject.strip()} mark: "))
        student["marks"][subject.strip()] = mark

    students.append(student)
    print(f"{GREEN}✔ Student added successfully!{RESET}")


# =========================
# View students
# =========================
def view_student():
    header("VIEW STUDENTS")

    if not students:
        print(f"{RED}✖ No student record found{RESET}")
        return

    for s in students:
        print(
            f"{BLUE}➤ ID:{RESET} {s['id']} | "
            f"{BLUE}Name:{RESET} {s['name']} | "
            f"{BLUE}Age:{RESET} {s['age']} | "
            f"{BLUE}Marks:{RESET} {s['marks']}"
        )


# =========================
# Search student
# =========================
def search_student():
    header("SEARCH STUDENT")

    if not students:
        print(f"{RED}✖ No record found{RESET}")
        return

    iid = int(input("Enter Student ID: "))
    for s in students:
        if s['id'] == iid:
            print(f"{GREEN}✔ Student Found{RESET}")
            print(
                f"ID: {s['id']} | "
                f"Name: {s['name']} | "
                f"Age: {s['age']} | "
                f"Marks: {s['marks']}"
            )
            return

    print(f"{RED}✖ No student found with this ID{RESET}")


# =========================
# Update marks
# =========================
def update_marks():
    header("UPDATE MARKS")

    if not students:
        print(f"{RED}✖ No record found{RESET}")
        return

    iid = int(input("Enter Student ID: "))
    for s in students:
        if s['id'] == iid:
            print(f"{YELLOW}Current Marks:{RESET} {s['marks']}")
            for subject in s["subjects"]:
                mark = int(input(f"Enter new mark for {subject.strip()}: "))
                s["marks"][subject.strip()] = mark

            print(f"{GREEN}✔ Marks updated successfully{RESET}")
            return

    print(f"{RED}✖ Student not found{RESET}")


# =========================
# Delete student
# =========================
def delete_student():
    header("DELETE STUDENT")

    if not students:
        print(f"{RED}✖ No record found{RESET}")
        return

    iid = int(input("Enter Student ID to delete: "))
    for i, s in enumerate(students):
        if s['id'] == iid:
            print(
                f"{YELLOW}⚠ Deleting:{RESET} "
                f"ID:{s['id']} | Name:{s['name']}"
            )
            students.pop(i)
            print(f"{GREEN}✔ Student deleted successfully{RESET}")
            return

    print(f"{RED}✖ No student found with this ID{RESET}")


# =========================
# Main loop
# =========================
while True:
    show_menu()
    try:
        choice = int(input(f"\n{BOLD}Select option (1–6): {RESET}"))
    except ValueError:
        print(f"{RED}✖ Enter a valid number{RESET}")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print(f"{GREEN}Exiting program. Goodbye 👋{RESET}")
        break
    else:
        print(f"{RED}✖ Invalid choice. Try again!{RESET}")