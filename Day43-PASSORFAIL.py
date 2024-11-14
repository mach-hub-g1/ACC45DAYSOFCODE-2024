# cook your dish here
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the values for N, X, and P
    N, X, P = map(int, input().split())
    
    # Calculate the total score
    total_score = 4 * X - N
    
    # Check if Chef passes or fails
    if total_score >= P:
        print("PASS")
    else:
        print("FAIL")
