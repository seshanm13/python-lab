def analyze_results(marks_list):
    avg = sum(marks_list) / len(marks_list)
    highest = max(marks_list)
    lowest = min(marks_list)
    passed = [m for m in marks_list if m > 40]
    
    print(f"Average Marks: {avg}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Number of Students Passed (>40): {len(passed)}")

# Collecting input for 5 students
student_marks = []
for i in range(5):
    m = float(input(f"Enter marks for student {i+1}: "))
    student_marks.append(m)

analyze_results(student_marks)