import math

def minimum_attacks(test_cases):
    results = []
    for H, X, Y in test_cases:
        # If using the special attack
        remaining_health_after_special = H - Y
        if remaining_health_after_special <= 0:
            # If special attack alone is enough
            min_attacks_with_special = 1
        else:
            # Calculate regular attacks needed after special
            regular_attacks_needed = math.ceil(remaining_health_after_special / X)
            min_attacks_with_special = 1 + regular_attacks_needed
        
        # Calculate attacks without special
        min_attacks_without_special = math.ceil(H / X)
        
        # Get the minimum of the two
        min_attacks = min(min_attacks_with_special, min_attacks_without_special)
        results.append(min_attacks)
    
    return results

# Input reading and function call
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
results = minimum_attacks(test_cases)

for result in results:
    print(result)
