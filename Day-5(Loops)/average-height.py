student_heights = input("Enter the height of the students:").split(",")
total_height = 0
print(student_heights)
for i in range(0,len(student_heights)):
    student_heights[i] = int(student_heights[i])
    total_height += student_heights[i]
    
print("Average Height:",(total_height)/len(student_heights))