# Question - Accept the length and width of a rectangle. Calculate
#  & print the area and perimiter.

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area of the rectangle: {area} sq. units")
print(f"Perimeter of the rectangle: {perimeter} units")