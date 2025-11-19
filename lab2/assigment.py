#Name-Tarun Shekhar
#Course-Btech cse(FSD)
#Roll no.-2501350051
import csv


def show_menu():
    print("\nWelcome to GradeBook Analyzer")
    print("1. Enter marks manually")
    print("2. Load marks from CSV file")
    print("3. Exit")

def manual_entry():
    marks = {}
    n = int(input("How many students? "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        score = int(input(f"Enter marks for {name}: "))
        marks[name] = score
    return marks

def load_csv():
    marks = {}
    filename = input("Enter CSV filename (with .csv): ")
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                name = row[0]
                score = int(row[1])
                marks[name] = score
    except:
        print("Error loading file. Make sure it exists and is formatted correctly.")
    return marks

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    scores = sorted(marks.values())
    n = len(scores)
    if n % 2 == 0:
        return (scores[n//2 - 1] + scores[n//2]) / 2
    else:
        return scores[n//2]

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades[name] = grade
    return grades

def grade_distribution(grades):
    dist = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for grade in grades.values():
        dist[grade] += 1
    print("\nGrade Distribution:")
    for grade, count in dist.items():
        print(f"{grade}: {count} students")

def pass_fail(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    print(f"\nPassed Students ({len(passed)}): {passed}")
    print(f"Failed Students ({len(failed)}): {failed}")

def print_table(marks, grades):
    print("\nResults Table:")
    print("{:<10} {:<6} {:<6}".format("Name", "Marks", "Grade"))
    for name in marks:
        print("{:<10} {:<6} {:<6}".format(name, marks[name], grades[name]))


while True:
    show_menu()
    choice = input("Choose option (1/2/3): ")
    if choice == '1':
        marks = manual_entry()
    elif choice == '2':
        marks = load_csv()
    elif choice == '3':
        print("See You!")
        break
    else:
        print("Invalid choice. Try again.")
        continue

    if marks:
        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_score = find_max_score(marks)
        min_score = find_min_score(marks)
        print(f"\nAverage: {avg:.2f}")
        print(f"Median: {med}")
        print(f"Highest Score: {max_score}")
        print(f"Lowest Score: {min_score}")

        grades = assign_grades(marks)
        grade_distribution(grades)
        pass_fail(marks)
        print_table(marks, grades)
