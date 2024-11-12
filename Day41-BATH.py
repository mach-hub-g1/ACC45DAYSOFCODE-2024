# cook your dish here
def max_people_for_bath(T, test_cases):
    results = []
    for i in range(T):
        X, Y = test_cases[i]
        # Calculate the number of people that can take a bath
        people = X // (2 * Y)
        results.append(people)
    return results

# Read input
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Calculate and print the result for each test case
results = max_people_for_bath(T, test_cases)
for result in results:
    print(result)
