# cook your dish here
# Number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    X = int(input())
    
    # Check if he can finish on time
    if X <= 7:
        print("Yes")
    else:
        print("No")
