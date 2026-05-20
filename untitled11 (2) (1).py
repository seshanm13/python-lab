employee_db = {"Alice": 50000, "Bob": 60000}

def add_employee(name, salary):
    employee_db[name] = salary
    print(f"Added employee {name}.")

def update_salary(name, new_salary):
    if name in employee_db:
        employee_db[name] = new_salary
        print(f"Updated {name}'s salary.")
    else:
        print("Employee not found.")

def search_employee(name):
    if name in employee_db:
        print(f"{name}'s Salary: ₹{employee_db[name]}")
    else:
        print("Employee not found.")

# Demo run
add_employee("Charlie", 55000)
update_salary("Alice", 52000)
search_employee("Bob")                                      