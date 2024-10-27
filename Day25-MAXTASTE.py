# cook your dish here
def maximize_tastiness(test_cases):
    results = []
    for a, b, c, d in test_cases:
        # Calculate all combinations of tastiness
        tastiness1 = a + c
        tastiness2 = a + d
        tastiness3 = b + c
        tastiness4 = b + d
        
        # Find the maximum tastiness
        max_tastiness = max(tastiness1, tastiness2, tastiness3, tastiness4)
        
        # Store the result
        results.append(max_tastiness)
    
    return results

# Input reading
T = int(input())
test_cases = []

for _ in range(T):
    a, b, c, d = map(int, input().split())
    test_cases.append((a, b, c, d))

# Get the results
results = maximize_tastiness(test_cases)

# Output results
for result in results:
    print(result)

