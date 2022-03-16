# Example 6_8
def enter_data():
    global total, n
    total = 0
    n = 0
    num = 0
    while num != -1:
        num = int(input(f"Enter Value {n+1} : "))
        if (num != -1):
            total += num
            n += 1

#main Program
total = 0
n = 0
enter_data()
print("Total number : ",total)
print("Average Value : ",total/n)            
