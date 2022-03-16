# Example 6_4
import math
def select_menu():
    print("Menu")
    print("1. circle 2.rectangle")
    menu = input("please choose : ")
    return(menu)

def cal_circle(radius):
    area = math.pi*radius*radius
    return(area)

def cal_rectangle(wigth, height):
    area = width * height
    return(area)

print("Program calculate area.")
menu = select_menu()
if menu == "1":
    radius = int(input("Enter radius : "))
    print("Area of circle = ", cal_circle(radius))
else:
    width = int(input("Enter width : "))
    height = int(input("Enter height : "))
    print("Area of rectangle = ",cal_rectangle(width,height))
