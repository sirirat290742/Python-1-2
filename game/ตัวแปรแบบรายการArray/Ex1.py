def Check_Grade(grade):
    Grades = ('A','B','C','D','F')
    Values = (4,3,2,1,0)
    for n in range(len(Grades)):
        if grade == Grades[n]:
            return(Values[n])

Done = True
while Done:
    grade = input("Enter grade (Q-exit): ")
    grade = grade.upper()
    if grade == "Q" :
        break
    else:
        value = Check_Grade(grade)
        print (f"Score value of {grade} is {value}")

print("End Programe.")
