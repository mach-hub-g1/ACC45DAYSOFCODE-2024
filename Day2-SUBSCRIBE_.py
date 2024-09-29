# cook your dish here
Day 02
  
 1. Easy

# Day-2 Easy 
# Gajendra Singh 
# BTech (CSE) SEC-A

def min_cost_for_subscriptions(test_cases):
    results = []
    for N, X in test_cases:
        # Calculate number of subscriptions needed
        subscriptions_needed = (N + 5) // 6
        # Calculate total cost
        total_cost = subscriptions_needed * X
        results.append(total_cost)
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    N, X = map(int, input().split())
    test_cases.append((N, X))

# Get results
results = min_cost_for_subscriptions(test_cases)

# Print results
for result in results:
    print(result)