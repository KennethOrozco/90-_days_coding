import numpy as np

# array = np.array([12, 24, 36, 48, 60, 72, 84, 96])

# print(array[0])
# print(array[-1])
# print(array[3])

# print(array[1:5])
# print(array[::2])
# print(array[5:8])

# selected = array[2:5]
# selected[0] = 999

# print(array)

# independent = array[5:8].copy()
# independent[0] = 555

# print(array)
# print(independent)

# scores = np.array([65, 78, 92, 84, 59, 73, 88, 95])

# bonus_scores = scores + 5

# doubled_scores = scores * 2

# squared_scores = scores **2

# print(bonus_scores)
# print(doubled_scores)
# print(squared_scores)

# a = scores[scores >= 80]
# b = scores[scores < 70]
# c = scores[(scores >= 70) & (scores <= 90)]
# print(a)
# print(b)
# print(c)

# first = np.array([10, 20, 30, 40])
# second = np.array([2, 4, 6, 8])

# add = first + second
# multiply = first * second

# print(add)
# print(multiply)

#Part A
# scores = np.array([
#     [85, 90, 78],
#     [92, 88, 95],
#     [70, 80, 75],
#     [89, 94, 91]
# ])

# print(scores.shape)
# print(scores.ndim)
# print(scores.size)
# print(scores[1, 2])
# print(scores[3, 0])

# #Part B
# print(scores[0, :])
# print(scores[:, 1])
# print(scores[0:2,:])
# print(scores[:, -1])

# #Part C
# sum_column = scores.sum(axis=0)
# sum_row = scores.sum(axis=1)

# print(sum_column)
# print(sum_row)

scores = np.array([
    [80, 90, 70],
    [60, 85, 95],
    [75, 80, 85],
    [90, 95, 88]
])

#Part A

average_score = scores.mean()
highest_score = scores.max()
lowest_score = scores.min()
student_average = scores.mean(axis=1)
average_exam_score = scores.mean(axis=0)

print(average_score)
print(highest_score)
print(lowest_score)
print(student_average)
print(average_exam_score)

#Part B

bonus = np.array([5, 10, 0])

adjusted = scores + bonus

print(adjusted)

print(adjusted.shape)

adjusted_student_average = adjusted.mean(axis=1)

print(adjusted_student_average)

