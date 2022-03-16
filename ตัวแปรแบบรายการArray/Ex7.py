from random import randint

#main program
student = int(input("Enter number student :"))
subject = int(input("Enter number subject :"))
scores = []
for r in range(student):
    scores.append([])
    for c in range(subject):
        scores[r].append(randint(0,100))


for score in scores:
    for s in score:
        print (s)
    print()
