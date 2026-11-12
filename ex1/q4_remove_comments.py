"""Experiment 1, Q4 - Copy file contents after removing comments.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Copy the contents of one file to another after removing
comment lines (lines starting with #). The source file is first
created from lines typed in by the user.

Sample run (source: src.txt, dest: dest.txt, lines:
"# comment", "x = 10", "# another", "y = 20"):
    File copied successfully!
    dest.txt then contains "x = 10" and "y = 20".
"""

src = input("Enter source file name: ")
dest = input("Enter destination file name: ")

n = int(input("Enter number of lines: "))

f = open(src, "w")
for i in range(n):
    f.write(input("Enter line: ") + "\n")
f.close()

s = open(src, "r")
d = open(dest, "w")
for line in s:
    if not line.strip().startswith("#"):
        d.write(line)
s.close()
d.close()
print("File copied successfully!")
