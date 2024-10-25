# cook your dish here
def count_problems(test_cases):
    results = []
    
    for n, codes in test_cases:
        count_start38 = 0
        count_ltime108 = 0
        
        for code in codes:
            if code == 'START38':
                count_start38 += 1
            elif code == 'LTIME108':
                count_ltime108 += 1
        
        results.append((count_start38, count_ltime108))
    
    return results

# Input reading
T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    codes = input().split()
    test_cases.append((N, codes))

# Get the results
results = count_problems(test_cases)

# Output the results
for start38_count, ltime108_count in results:
    print(start38_count, ltime108_count)
