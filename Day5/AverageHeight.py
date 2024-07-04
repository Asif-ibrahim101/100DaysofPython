#step-1: reading input from the user
input_line = input("Enter all the heights here: ")

#step-2: parse the input
heights = input_line.split()
student_heights = []

#step-3: convert height from string to integer
for height in heights :
    student_heights.append(int(height))

# step-4: calculate the total height
total_height = 0
for height in student_heights:
    total_height += height

# step-5: calculate the number of students
total_students = 0
for _ in student_heights:
    total_students += 1

# step-6: calculate average height
average_height = total_height / total_students

rounded_value = round(average_height);

print("Total_height: ", total_height)
print("Average Height : " , rounded_value)
print("number_of_students: ", total_students)
