# cook your dish here
def max_rent_months(T, cases):
    results = []
    for case in cases:
        X, Y = case
        if X <= 0:  # Handle the case where X is 0 or negative (though not specified)
            results.append(0)
        else:
            max_months = (Y // X) - 1  # Y // X gives the number of full months that can be rented
            results.append(max(0, max_months))  # Ensure result is not negative
    return results

# Input handling
T = int(input("Enter number of test cases: "))
cases = []

for _ in range(T):
    X, Y = map(int, input().split())
    cases.append((X, Y))
