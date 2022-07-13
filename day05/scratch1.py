# average heights

student_heights = [180, 124, 165, 173, 189, 169, 146]

total_heights = 0
for height in student_heights:
    total_heights += height

average_height = total_heights / len(student_heights)
print(f"The average student height is {average_height:.2f}cm")