# cook your dish here
# Read number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read the values for each test case
    N, A, B = map(int, input().split())
    
    # Calculate number of odd and even indexed episodes
    odd_episodes = (N + 1) // 2  # Odd indexed episodes
    even_episodes = N // 2  # Even indexed episodes
    
    # Calculate total duration
    total_duration = odd_episodes * B + even_episodes * A
    
    # Output the result for this test case
    print(total_duration)
