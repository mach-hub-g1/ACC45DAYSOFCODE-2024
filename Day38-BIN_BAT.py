# cook your dish here
import math

def total_time(N, A, B):
    # Number of rounds is log2(N)
    rounds = int(math.log2(N))
    
    # Total time for rounds
    time_for_rounds = rounds * A
    
    # Total break time (no break after the last round)
    break_time = (rounds - 1) * B
    
    # Total time for the event
    total_event_time = time_for_rounds + break_time
    
    return total_event_time

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N, A, B = map(int, input().split())
    print(total_time(N, A, B))
