students_list = ["Rahul", "Sneha", "Amit"]

def add_student(name):
    students_list.append(name)
    print(f"Added {name} successfully.")

def remove_student(name):
    if name in students_list:
        students_list.remove(name)
        print(f"Removed {name} successfully.")
    else:
        print(f"{name} not found in attendance.")

def display_students():
    print("Present Students:", students_list)

# Demo run
add_student("Vijay")
remove_student("Sneha")
display_students()