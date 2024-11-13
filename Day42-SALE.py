# cook your dish here
# Function to solve the problem
def calculate_payment(A, B, C):
    # Sum of all prices minus the minimum price
    return A + B + C - min(A, B, C)

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the prices A, B, C
    A, B, C = map(int, input().split())
    # Calculate the payment Chef needs to make
    result = calculate_payment(A, B, C)
    # Print the result for this test case
    print(result)
