# cook your dish here
# Read number of test cases
T = int(input())
results = []

for _ in range(T):
    # Read the number of bits for each test case
    N = int(input())
    
    # Check if N is a multiple of 4
    if N % 4 == 0:
        results.append("Good")
    else:
        results.append("Not Good")

# Print all results, each on a new line
print("\n".join(results))
