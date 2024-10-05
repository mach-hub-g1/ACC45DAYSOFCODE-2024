# cook your dish here
def is_monopoly(T, test_cases):
    results = []
    for i in range(T):
        P, Q, R, S = test_cases[i]
        total_profit = P + Q + R + S
        
        if (P > total_profit - P) or (Q > total_profit - Q) or (R > total_profit - R) or (S > total_profit - S):
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Example usage:
T = int(input())
test_cases = [list(map(int, input().split())) for _ in range(T)]
results = is_monopoly(T, test_cases)

for result in results:
    print(result)