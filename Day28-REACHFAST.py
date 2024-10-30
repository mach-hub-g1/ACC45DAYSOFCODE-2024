# cook your dish here
def min_steps_to_reach_chefina(test_cases):
    results = []
    for A, B, K in test_cases:
        distance = abs(A - B)
        steps = (distance + K - 1) // K  # This effectively calculates ceil(distance / K)
        results.append(steps)
    return results

# Input reading and output handling
T = int(input().strip())
test_cases = []
for _ in range(T):
    A, B, K = map(int, input().strip().split())
    test_cases.append((A, B, K))

results = min_steps_to_reach_chefina(test_cases)
for res in results:
    print(res)
