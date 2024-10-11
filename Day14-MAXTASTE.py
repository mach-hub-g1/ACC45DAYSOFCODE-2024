# cook your dish here
def max_tastiness(T, test_cases):
    results = []
    for i in range(T):
        a, b, c, d = test_cases[i]
        # Calculate all possible tastiness values
        tastiness_1 = a + c
        tastiness_2 = a + d
        tastiness_3 = b + c
        tastiness_4 = b + d
        
        # Find the maximum tastiness
        max_tastiness_value = max(tastiness_1, tastiness_2, tastiness_3, tastiness_4)
        results.append(max_tastiness_value)
    
    return results

# Example usage:
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
results = max_tastiness(T, test_cases)

# Print the results
for result in results:
    print(result)
