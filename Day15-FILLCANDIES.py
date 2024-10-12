# cook your dish here
def min_bags_needed(test_cases):
    results = []
    for N, K, M in test_cases:
        capacity_of_one_bag = K * M
        # Calculate the number of bags required
        bags_needed = (N + capacity_of_one_bag - 1) // capacity_of_one_bag
        results.append(bags_needed)
    return results

# Input reading
T = int(input())
test_cases = []

for _ in range(T):
    N, K, M = map(int, input().split())
    test_cases.append((N, K, M))

# Get results
results = min_bags_needed(test_cases)

# Print results
for result in results:
    print(result)
