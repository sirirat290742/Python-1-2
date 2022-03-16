Done = True
while Done:
    Score = input(f"Enter score value : ")
    if Score != "-1" :
        Mark = float(Score)
        if Mark >= 0 and Mark <= 100:
            Grade = ""
            if Mark >= 80 :
                Grade ="A"
            elif Mark >= 70 :
                Grade ="B"
            elif Mark >= 60 :
                Grade ="C"
            elif Mark >= 50 :
                Grade ="D"
            else:
                Grade = "F"
            print(f"Score is {Mark}, get {Grade}")
        else :
            print("Score out of rang, input again.")
    elif Score == "-1" :
        Done = False

print("Exit Programe")
