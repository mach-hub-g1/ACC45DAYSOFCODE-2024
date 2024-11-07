def count_tuesdays(N):
    # The first Tuesday is on day 2, then subsequent Tuesdays occur every 7 days.
    # We need to count how many Tuesdays fall within the range 1 to N.
    return (N - 2) // 7 + 1 if N >= 2 else 0

def solve():
    # Read number of test cases
    T = int(input().strip())
    
    # Process each test case
    for _ in range(T):
        N = int(input().strip())
        print(count_tuesdays(N))

