# cook your dish here
# Read the number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read X and Y
    X, Y = map(int, input().split())
    
    # Check if Munchy is an expert
    if 2 * Y >= X:
        print("YES")
    else:
        print("NO")
