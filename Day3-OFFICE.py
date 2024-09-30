# cook your dish here
Day 02
 
  1. Easy

#Day-03 Easy
#GAJENDRA SINGH 
#BTECH CSE SEC-A

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read X and Y values
    X, Y = map(int, input().split())
    
    # Calculate total working hours in one week
    total_hours = 4 * X + Y
    
    # Print the result
    print(total_hours)