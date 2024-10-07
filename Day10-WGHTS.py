# cook your dish here
def can_measure_weight(T, test_cases):
    results = []
    for i in range(T):
        W, X, Y, Z = test_cases[i]
        
        # Check all combinations
        if (W == X or 
            W == Y or 
            W == Z or 
            W == X + Y or 
            W == X + Z or 
            W == Y + Z or 
            W == X + Y + Z):
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = can_measure_weight(T, test_cases)

# Print results
for result in results:
    print(result)
