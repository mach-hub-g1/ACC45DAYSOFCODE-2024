# cook your dish here
def minimum_flips(test_cases):
    results = []
    for N, X in test_cases:
        flips_to_face_up = N - X  # Flips needed to make all face-up
        flips_to_face_down = X     # Flips needed to make all face-down
        min_flips = min(flips_to_face_up, flips_to_face_down)
        results.append(min_flips)
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get the results
results = minimum_flips(test_cases)

# Output results
for result in results:
    print(result)
