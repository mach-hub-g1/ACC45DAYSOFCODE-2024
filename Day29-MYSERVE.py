# cook your dish here
def determine_service(T, scores):
    results = []
    for P, Q in scores:
        total_points = P + Q
        position_in_cycle = total_points % 4
        
        if position_in_cycle == 0 or position_in_cycle == 1:
            results.append("Alice")
        else:
            results.append("Bob")
    
    return results

# Example usage:
T = int(input())
scores = [tuple(map(int, input().split())) for _ in range(T)]
results = determine_service(T, scores)

for result in results:
    print(result)
