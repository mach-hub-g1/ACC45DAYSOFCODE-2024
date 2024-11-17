# cook your dish here
import math

def solve():
    T = int(input())  # Number of test cases
    for _ in range(T):
        # Read the values for X, Y, R
        X, Y, R = map(int, input().split())
        
        # Calculate the number of extra sticks
        extra_sticks = R // 30
        
        # Total number of sticks eaten
        total_sticks = X + extra_sticks
        
        # Calculate the number of plates (round up division)
        plates = math.ceil(total_sticks / Y)
        
        # Output the result
        print(plates)

# Read the input and execute the solution
solve()
