n = int(input("Enter the number of students: "))
marks = []
for i in range(n):
    mark = int(input("Enter student mark: "))
    marks.append(mark)
print("Marks before sorting:", marks)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

print("Marks after sorting:", marks)
