# cook your dish here
def min_coins_for_gifts(N):
    # Number of full sets of 5 gifts, each costing 4 coins
    full_sets = N // 5
    # Remaining gifts (less than 5) which cost 1 coin each
    remaining = N % 5
    # Total coins is the cost of full sets (4 coins per set) plus the remaining gifts
    return full_sets * 4 + remaining

def main():
    T = int(input())  # number of test cases
    for _ in range(T):
        N = int(input())  # number of gifts for this test case
        print(min_coins_for_gifts(N))

if __name__ == "__main__":
    main()
