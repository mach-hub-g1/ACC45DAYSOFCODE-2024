# cook your dish here
def check_water_filling(T, test_cases):
    results = []
    
    for i in range(T):
        B1, B2, B3 = test_cases[i]
        empty_count = (1 - B1) + (1 - B2) + (1 - B3  # Count empty bottles
        
        if empty_count >= 2:
            results.append("Water filling time")
        else:
            results.append("Not now")
    
    return results

# Input
T = int(input())
test_cases = [list(map(int, input().split())) for _ in range(T)]

# Get the results
results = check_water_filling(T, test_cases)

# Output results
for result in results:
    print(result)
