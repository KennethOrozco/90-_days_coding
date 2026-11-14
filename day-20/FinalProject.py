import numpy as np

students = np.array(["Alice", "Bob", "Charlie", "David", "Eve"])

scores = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [70, 80, 75],
    [89, 94, 91],
    [60, 72, 68]
])

#Part A

print(scores.shape)
print(scores.ndim)
print(scores.size)
print(scores[2, :])
print(scores[:, 1])


#Part B

average_student_score = scores.mean(axis=1)
average_exam_score = scores.mean(axis=0)
average_score = scores.mean()
highest = scores.max()
lowest = scores.min()

print(average_student_score)
print(average_exam_score)
print(average_score)
print(highest)
print(lowest)

#Part C

bonus = np.array([5, 3, 2])

adjusted_scores = scores + bonus

print(adjusted_scores)

new_average_student_score = adjusted_scores.mean(axis=1)

print(new_average_student_score)

print(scores)

#Part D

filtered_scores = scores[scores >= 90]

print(filtered_scores)

filtered_average = students[new_average_student_score >= 85]

print(filtered_average)

#Part E
for index, student in enumerate(students):
    print(f"Name: {student} -- Original average: : {average_student_score[index]} -- Adjusted average: {new_average_student_score[index]}")

