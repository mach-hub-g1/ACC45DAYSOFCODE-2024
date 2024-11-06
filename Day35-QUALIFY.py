# cook your dish here
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read X, A, and B for this test case
    X, A, B = map(int, input().split())
    
    # Calculate the total score
    score = A * 1 + B * 2
    
    # Check if the score is enough to qualify
    if score >= X:
        print("Qualify")
    else:
        print("NotQualify")
