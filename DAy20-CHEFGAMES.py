# cook your dish here
def chefland_tennis_decision(test_cases):
    results = []
    for decisions in test_cases:
        if all(decision == 0 for decision in decisions):
            results.append("IN")
        else:
            results.append("OUT")
    return results

# Example usage:
T = int(input("Enter number of test cases: "))  # Input number of test cases
test_cases = []

for _ in range(T):
    # Input decisions from referees
    decisions = list(map(int, input().split()))
    test_cases.append(decisions)

results = chefland_tennis_decision(test_cases)
for result in results:
    print(result)

