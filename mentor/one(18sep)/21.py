# Question - Write a program that will ask the user to enter his/her marks (out of 100). Define a method that will display grades according
#      to the marks entered as below:
#  	 Marks        Grade 
#  	 91-100          AA 
# 	 81-90           AB 
# 	 71-80           BB 
#    61-70           BC 
#    51-60           CD 
#    41-50           DD 
#    <=40            F
def calculate_grade(marks):
    if 91 <= marks <= 100:
        return "AA"
    elif 81 <= marks <= 90:
        return "AB"
    elif 71 <= marks <= 80:
        return "BB"
    elif 61 <= marks <= 70:
        return "BC"
    elif 51 <= marks <= 60:
        return "CD"
    elif 41 <= marks <= 50:
        return "DD"
    else:
        return "F"

marks = int(input("Enter your marks (out of 100): "))

grade = calculate_grade(marks)
print(f"Your grade is: {grade}")
