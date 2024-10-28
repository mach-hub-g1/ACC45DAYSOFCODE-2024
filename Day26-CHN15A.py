# cook your dish here
def count_wolverine_like_minions(test_cases):
    results = []
    for case in test_cases:
        N, K, characteristic_values = case
        wolverine_count = 0
        
        for value in characteristic_values:
            new_value = value + K
            if new_value % 7 == 0:
                wolverine_count += 1
        
        results.append(wolverine_count)
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    T = int(data[0])
    test_cases = []
    
    index = 1
    for _ in range(T):
        N, K = map(int, data[index].split())
        characteristic_values = list(map(int, data[index + 1].split()))
        test_cases.append((N, K, characteristic_values))
        index += 2
    
    results = count_wolverine_like_minions(test_cases)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
