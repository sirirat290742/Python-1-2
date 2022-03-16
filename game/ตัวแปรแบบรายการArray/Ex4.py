def Check_Grade(grade):
    Grades = ['A','B+','B','C+','C','D+','D','F']
    Values = [4, 3.5, 3, 2.5, 2, 1.5, 1, 0]
    for n in range (len(Grades)):
        if grade == Grades[n]:
            return(Values[n])


Done = True
while Done:
    grade = input("Enter grade (Q-exit): ")
    grade = grade.upper()
    if grade == "Q":
        break
    else:
        Value = Check_Grade(grade)
        print (f"Score value of {grade}is {Value}")

print ("End Program.")
