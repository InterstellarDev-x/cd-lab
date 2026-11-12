"""Experiment 1, Q2: Store student records in a file and compute statistics.

Reads roll no., name and marks for n students, saves them to
students.txt, then prints average, highest and lowest marks.

Usage:
    python q2_student_records.py
"""

import sys

import os

# Files live next to this script, not next to your terminal's folder.
# __file__ is this script's own path, so BASE_DIR is its folder - the
# Python equivalent of JS __dirname. Every file below is resolved
# through _path(), so the program works no matter which folder you
# run it from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def _path(name):
    """Resolve *name* against this script's folder."""
    return os.path.join(BASE_DIR, name)


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

    with open(_path("students.txt"), "w") as f:
        for roll, name, marks in records:
            f.write(f"{roll} {name} {marks}\n")
    print(f"Records saved to {_path('students.txt')}")

    marks_list = [r[2] for r in records]
    print("Average Marks:", sum(marks_list) / n)
    print("Highest Marks:", max(marks_list))
    print("Lowest Marks:", min(marks_list))


if __name__ == "__main__":
    student_data()
