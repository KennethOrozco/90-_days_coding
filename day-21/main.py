import matplotlib.pyplot as plt

# courses = ["Python", "JavaScript", "C++", "Java"]
# students = [120, 95, 70, 85]

# plt.bar(courses, students)

# plt.title("Programming Course Enrollment")

# plt.xlabel("Course")

# plt.ylabel("Number of students")

# plt.show()

# scores = [
#     55, 62, 67, 70, 72, 74, 75, 76, 78, 79,
#     81, 83, 85, 87, 89, 91, 93, 95, 58, 64
# ]

# plt.hist(scores, bins=5, edgecolor="black")
# plt.title("Student Exam Score Distribution")
# plt.xlabel("Exam Score")
# plt.ylabel("Number of Students")
# plt.show()

# sleep_hours = [4, 5, 6, 7, 8, 9, 10]
# productivity = [45, 55, 65, 80, 90, 85, 75]

# plt.scatter(sleep_hours, productivity)
# plt.title("Sleep Hours vs Productivity")
# plt.xlabel("Hours of Sleep")
# plt.ylabel("Productivity Score")
# plt.show()

exams = [1, 2, 3, 4, 5]

alice_scores = [65, 70, 78, 85, 92]
bob_scores = [80, 82, 79, 85, 87]

plt.plot(exams, alice_scores, color="blue", marker="o", label="Alice's Scores")
plt.plot(exams, bob_scores, color="red", marker="s",linestyle="--",  label="Bob's Scores")

plt.title("Student Performance Comparison")
plt.xlabel("Exam number")
plt.ylabel("Score")

plt.legend()
plt.grid(True)
plt.show()
