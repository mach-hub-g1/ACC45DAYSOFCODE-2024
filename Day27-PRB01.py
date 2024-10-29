# cook your dish here
import sys
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    input = sys.stdin.read
    data = input().splitlines()
    T = int(data[0])  # Number of test cases
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        if is_prime(N):
            results.append("yes")
        else:
            results.append("no")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
