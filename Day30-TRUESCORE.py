# cook your dish here
def can_score_change(test_cases):
    results = []
    for case in test_cases:
        A, B, C, D = case
        if C >= A and D >= B:
            results.append("POSSIBLE")
        else:
            results.append("IMPOSSIBLE")
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    test_cases.append((A, B, C, D))

# Process and output results
results = can_score_change(test_cases)
for result in results:
    print(result)
