# cook your dish here
# Read number of test cases
T = int(input().strip())
results = []

for _ in range(T):
    N = int(input().strip())
    # Calculate number of ways to choose captain and vice-captain
    choices = N * (N - 1)
    results.append(choices)

# Print all results
for result in results:
    print(result)
