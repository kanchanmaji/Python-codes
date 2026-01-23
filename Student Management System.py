# ===================================
#       Student Management System
# ===================================

print(35*"#")
print("\n Student Management System \n")
print(35*"#")

# Global list to store all student records
students = []

# -------------------------------
# Function to display main menu
# -------------------------------
def show_menu():
    menu = {
        1: "\n1. Add a student",
        2: "2. View all students",
        3: "3. Search for a student by ID",
        4: "4. Update marks",
        5: "5. Delete a student",
        6: "6. Exit program"
    }
    for i in menu:
        print(menu[i])

# -------------------------------
# Function to add a new student
# -------------------------------
def add_student():
    print("\n",35*"=")
    print("\n			Add Students \n")
    print(35*"=")
    
    # Input student ID and check for duplicates
    student_id = int(input("Enter Student Id : "))
    for s in students:
        if s['id'] == student_id:
            print(f"\n❌ Student with ID {student_id} already exists! Try again.")
            return  # Stop adding duplicate
    
    # Input student details
    student = {}
    student["id"] = student_id
    student["name"] = input("Enter Student name : ")
    student["age"] = int(input("Enter Your age : "))
    
    # Input subjects and marks
    student["subjects"] = tuple(input("Enter Subjects name (comma separated) : ").split(","))
    student["marks"] = {}
    for subject in student["subjects"]:
        mark = int(input(f"Enter {subject.strip()} mark : "))
        student["marks"][subject.strip()] = mark
    
    # Add the student to the global list
    students.append(student)
    print("\n✅ Student added successfully!")

# -------------------------------
# Function to view all students
# -------------------------------
def view_student():
	print("\n",35*"=")
	print("\n			View Students \n")
	print(35*"=")
	
	if not students:
		print("No Student Record found .....")
		return
	
	for s in students:
		 print(f"\nID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")
	print()

# -------------------------------
# Function to search for a student by ID
# -------------------------------
def search_student():
	print("\n",35*"=")
	print("\n		Search Students \n")
	print(35*"=")
	
	if not students:
		print("\n !!! No record Found !!!")
		return
		
	iid = int(input("Enter Student id : "))
	found = False
	
	for s in students:				
			if s['id'] == iid:
				 print(f"\n ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")
				 found = True 
				 break
				 
	if not found:
				print("No data found !")

# -------------------------------
# Function to update marks of a student
# -------------------------------
def update_marks():
    print("\n",35*"=")
    print("\n       Update Students \n")
    print(35*"=")
    
    if not students:
        print("\n !!! No record Found !!!")
        return
        
    iid = int(input("Enter Student id : "))
    found = False
    
    for s in students:                
        if s['id'] == iid:
            found = True
            print(f"\nCurrent Marks: {s['marks']}")
            for subject in s["subjects"]:
                mark = int(input(f"Enter new mark for {subject.strip()} : "))
                s["marks"][subject.strip()] = mark
            print("\n✅ Marks updated successfully!")
            break
                 
    if not found:
        print("No student found with this ID!")

# -------------------------------
# Function to delete a student by ID
# -------------------------------
def delete_student():
    print("\n", 35*"=")
    print("\n       Delete Students \n")
    print(35*"=")
    
    if not students:
        print("No Record found!")
        return
    
    iid = int(input("Enter Student ID to delete: "))
    found = False
    
    # Use enumerate to get index for deletion
    for i, s in enumerate(students):
        if s['id'] == iid:
            found = True
            print(f"Deleting Student: ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")
            students.pop(i)  # Remove student by index
            print(f"✅ Student with ID {iid} deleted successfully!")
            break  # Exit loop after deleting
    
    if not found:
        print("❌ No student found with this ID!")

# -------------------------------
# Main program loop
# -------------------------------
while True:
    show_menu()
    choice = int(input("\nEnter choice: "))
    
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
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")