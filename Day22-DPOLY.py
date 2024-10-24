# cook your dish here
def find_degree_of_polynomial(test_cases):
    results = []
    for case in test_cases:
        N, coefficients = case
        degree = -1
        for i in range(N - 1, -1, -1):
            if coefficients[i] != 0:
                degree = i
                break
        results.append(degree)
    return results

# Read number of test cases
T = int(input())
test_cases = []

# Read each test case
for _ in range(T):
    N = int(input())
    coefficients = list(map(int, input().split()))
    test_cases.append((N, coefficients))

# Find degrees for each test case
results = find_degree_of_polynomial(test_cases)

# Output results
for result in results:
    print(result)
