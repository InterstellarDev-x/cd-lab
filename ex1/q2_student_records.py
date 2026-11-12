"""Experiment 1, Q2: Store student records in a file and compute statistics.

Reads roll no., name and marks for n students, saves them to
students.txt, then prints average, highest and lowest marks.

Usage:
    python q2_student_records.py
"""

import sys


def student_data():
    try:
        n = int(input("Enter number of students: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if n <= 0:
        print("Number of students must be at least 1.")
        return

    records = []
    for i in range(n):
        print(f"--- Student {i + 1} ---")
        roll = input("Roll No: ").strip()
        name = input("Name: ").strip()
        while True:
            try:
                marks = float(input("Marks: "))
                break
            except ValueError:
                print("Please enter a number for marks.")
        records.append((roll, name, marks))

    with open("students.txt", "w") as f:
        for roll, name, marks in records:
            f.write(f"{roll} {name} {marks}\n")
    print("Records saved to students.txt")

    marks_list = [r[2] for r in records]
    print("Average Marks:", sum(marks_list) / n)
    print("Highest Marks:", max(marks_list))
    print("Lowest Marks:", min(marks_list))


if __name__ == "__main__":
    student_data()
