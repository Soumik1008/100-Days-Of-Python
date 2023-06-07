import pandas
student_dict={
    "student":['Angela','James','Lily'],
    "score":[56,76,78]
}

student_dataFrame = pandas.DataFrame(student_dict)
# print(student_dataFrame)

for (index,row) in student_dataFrame.iterrows():
    print(row.student)