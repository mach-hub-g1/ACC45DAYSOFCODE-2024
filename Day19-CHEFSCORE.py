# cook your dish here
def can_achieve_score(T, test_cases):
    results = []
    for i in range(T):
        N, X, Y = test_cases[i]
        if Y % X == 0 and Y <= N * X:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input Reading
T = int(input())
test_cases = []
for _ in range(T):
    N, X, Y = map(int, input().split())
    test_cases.append((N, X, Y))

# Get results
results = can_achieve_score(T, test_cases)

# Output results
for result in results:
    print(result)
