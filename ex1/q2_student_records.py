"""Experiment 1, Q2 - Store student records in a file and calculate statistics.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Store student records (roll no, name, marks) in a file and
calculate the class average, highest and lowest marks. Records are
saved to students.txt.

Sample run (2 students: 101 Aditya 85, 102 Rohan 92):
    Average Marks: 88.5
    Highest Marks: 92.0
    Lowest Marks: 85.0
"""

n = int(input("Enter number of students: "))
marks = []

f = open("students.txt", "w")

for i in range(n):
    roll = input("Roll No: ")
    name = input("Name: ")
    m = float(input("Marks: "))

    marks.append(m)

    f.write(roll + " " + name + " " + str(m) + "\n")
f.close()

print("Average Marks:", sum(marks) / n)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
