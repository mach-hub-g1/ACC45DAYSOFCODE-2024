# cook your dish here
def is_cyclic_quadrilateral(A, B, C, D):
    # Check if opposite angles sum to 180 degrees
    return (A + C == 180) and (B + D == 180)

def main():
    # Read number of test cases
    T = int(input())
    
    # Process each test case
    for _ in range(T):
        # Read angles of the quadrilateral
        A, B, C, D = map(int, input().split())
        
        # Check if the quadrilateral is cyclic and print the result
        if is_cyclic_quadrilateral(A, B, C, D):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
