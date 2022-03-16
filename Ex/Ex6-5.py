# Example 6_4
def check_grade(score):
    grade = ""
    if score >= 80:
        grade = "A"
    elif score >= 75:
        grade = "B+"
    elif score >= 70:
        grade = "B"
    elif score >= 65:
        grade = "C+"
    elif score >= 60:
        grade = "C"
    elif score >= 55:
        grade = "D+"
    elif score >= 50:
        grade = "D"
    else :
        grade = "F"
    return(grade)
#main Program
print ("Program calculate grade.")
done = True
while done:
    score = int(input("Enter score (-1 to exit) : "))
    if score >= 0 and score <= 100:
        grade = check_grade(score)
        print(f"score {score} , get garde : {grade}")
    elif score == -1:
        done = False
    else:
        print("Score ereor, enter again.")

    print("Exit program...")
