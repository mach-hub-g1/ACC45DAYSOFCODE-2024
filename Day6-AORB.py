# cook your dish here
def max_points(T, test_cases):
    results = []
    for X, Y in test_cases:
        score_A_first = max(1500 - 6 * X - 4 * Y, 0)
        score_B_first = max(1500 - 6 * Y - 2 * X, 0)
        max_score = max(score_A_first, score_B_first)
        results.append(max_score)
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = max_points(T, test_cases)

# Output results
for result in results:
    print(result)
    
