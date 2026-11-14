import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main() -> None:
    while True:
        students = ["Alice", "Bob", "Charlie", "David", "Eve"]
        scores = np.array([
            [85, 90, 78],
            [92, 88, 95],
            [70, 80, 75],
            [89, 94, 91],
            [60, 72, 68]
            ])
        student_average = scores.mean(axis=1)
        alice_scores = scores[0, :]
        bob_scores = scores[1, :]
        charlie_scores = scores[2, :]
        david_scores = scores[3, :]
        eve_scores = scores[4, :]
        exam_1 = scores[:, 0]
        exam_3 = scores[:, 2]

        options = {
            1: "Average Score by Student",
            2: "Student Exam Progress",
            3: "Exam Score Distribution",
            4: "Exam 1 vs Exam 3 Scores",
            5: "Exit"
        }
        for key, value in options.items():
            print(f"{key}. {value}")
        option = input("Option: ")
        if option == "1":
            plt.figure()
            plt.bar(students, student_average)
            plt.title("Average Score by Student")
            plt.xlabel("Students")
            plt.ylabel("Scores")
            plt.show()
        elif option == "2":
            exams = [1, 2, 3]
            plt.figure()
            plt.plot(exams, alice_scores, color="blue", marker="o", label="Alice's Scores")
            plt.plot(exams, bob_scores, color="red", marker="o", label="Bob's Scores")
            plt.plot(exams, charlie_scores, color="green", marker="o", label="Charlie's Scores")
            plt.plot(exams, david_scores, color="yellow", marker="o", label="David's Scores")
            plt.plot(exams, eve_scores, color="purple", marker="o", label="Eve's Scores")
            plt.title("Student Exam Progress")
            plt.xlabel("Exam Number")
            plt.ylabel("Score")
            plt.legend()
            plt.show()
        elif option == "3":
            plt.figure()
            plt.hist(scores.flatten(), bins=5, edgecolor="black")
            plt.title("Exam Score Distribution")
            plt.xlabel("Score")
            plt.ylabel("Number of Times Score was Reached")
            plt.show()
        elif option == "4":
            plt.figure()
            plt.scatter(exam_1, exam_3, color="blue",)
            plt.title("Exam 1 vs Exam 3 Scores")
            plt.xlabel("Exam 1 Scores")
            plt.ylabel("Exam 3 Scores")
            plt.show()
        elif option == "5":
            break
        else:
            print("Invalid option!")



if __name__ == "__main__":
    main()