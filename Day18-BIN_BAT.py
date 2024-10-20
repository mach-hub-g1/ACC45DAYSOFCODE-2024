# cook your dish here
def calculate_total_time(T, test_cases):
    results = []
    for i in range(T):
        N, A, B = test_cases[i]
        rounds = N.bit_length() - 1  # log2(N) gives the number of rounds
        total_time = (rounds * A) + ((rounds - 1) * B)
        results.append(total_time)
    return results

# Input Handling
T = int(input())
test_cases = []
for _ in range(T):
    N, A, B = map(int, input().split())
    test_cases.append((N, A, B))

# Calculate and Output Results
results = calculate_total_time(T, test_cases)
for result in results:
    print(result)
