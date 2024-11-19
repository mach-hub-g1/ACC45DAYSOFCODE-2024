# cook your dish here
def solve():
    # Read number of test cases
    T = int(input())
    
    # Loop through each test case
    for _ in range(T):
        # Read values for each test case
        S, X, Y, Z = map(int, input().split())
        
        # Calculate the free space left after the two installed apps
        free_space = S - X - Y
        
        # Case 1: If there's enough space already, no need to delete anything
        if free_space >= Z:
            print(0)
        # Case 2: If deleting one app is enough
        elif free_space + X >= Z or free_space + Y >= Z:
            print(1)
        # Case 3: If deleting both apps is required
        else:
            print(2)

