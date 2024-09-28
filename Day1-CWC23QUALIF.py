# cook your dish here
Day 01 

1. Easy

# Day-1 Easy
# Gajendra singh
# Btech CSE SEC A

while True:
    try:
        x= int(input("Please enter the Points : "))
        if 0 <= x <= 20:
            if x>=12: 
                print("Yes, Qualified!")
            else : 
                print("Not Qualified!")
            break
        else : 
            print(" \n \n Please enter Valid Value 0-20 \n \n")
    except ValueError:
        print("Please enter Correct Score Point")