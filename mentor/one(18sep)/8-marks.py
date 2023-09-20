# Question - Accept the marks of Robert in three subjects Maths, Computer,
# English respectively (each out of 100 ), Write a program to calculate his
# total marks and percentage marks.

maths_marks = int(input("Enter marks in Maths (out of 100): "))
computer_marks = int(input("Enter marks in Computer (out of 100): "))
english_marks = int(input("Enter marks in English (out of 100): "))

total_marks = maths_marks + computer_marks + english_marks
percentage_marks = (total_marks / 300) * 100

print(f"Total Marks: {total_marks}")
print(f"Percentage Marks: {percentage_marks}%")