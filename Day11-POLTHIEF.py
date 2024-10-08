# cook your dish here
def minimum_time_to_catch_thief(test_cases):
    results = []
    for X, Y in test_cases:
        time = abs(Y - X)
        results.append(time)
    return results

# Read number of test cases
T = int(input())
test_cases = []
for _ in range(T):
    X, Y = map(int, input().split())
    test_cases.append((X, Y))

# Get the results
results = minimum_time_to_catch_thief(test_cases)

# Output the results
for result in results:
    print(result)
