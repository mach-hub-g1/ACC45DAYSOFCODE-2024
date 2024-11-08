def minimum_flips_to_make_sum_zero(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        # Compute the sum of the array
        total_sum = sum(a)
        
        # If the sum is odd, it's impossible to make the sum zero
        if total_sum % 2 != 0:
            results.append(-1)
        else:
            # Minimum flips needed is half of the absolute sum
            results.append(abs(total_sum) // 2)
    
    return results

# Read the input
T = int(input())  # number of test cases
test_cases = []
for _ in range(T):
    N = int(input())  # length of array
    A = list(map(int, input().split()))  # the array itself
    test_cases.append((N, A))

# Get the results
results = minimum_flips_to_make_sum_zero(T, test_cases)

# Output the results
for result in results:
    print(result)
