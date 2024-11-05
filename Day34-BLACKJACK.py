# cook your dish here
In this problem, Chef is playing a variant of Blackjack, and we need to determine the third number required to win the game, given the first two numbers, \( A \) and \( B \).

### Problem Breakdown:

1. **Goal**: Chef needs the sum of the three numbers (the first two given numbers and a third number) to equal exactly 21.
2. **Input**: 
   - For each test case, you're given two numbers \( A \) and \( B \), both between 1 and 10.
3. **Output**:
   - You need to find the third number \( C \) such that \( A + B + C = 21 \).
   - If such a number \( C \) exists and lies between 1 and 10 (inclusive), print that number.
   - If no such number exists, print -1.

### Steps to Solve:

1. **Equation Setup**:
   \[
   A + B + C = 21
   \]
   Rearranging for \( C \):
   \[
   C = 21 - A - B
   \]
   So, the third number \( C \) is simply \( 21 - A - B \).

2. **Check Validity**:
   - For a valid game, \( C \) should be between 1 and 10 (inclusive). If \( C \) lies in this range, print \( C \), otherwise print -1.

3. **Implementation Details**:
   - First, read the number of test cases \( T \).
   - For each test case, calculate \( C \) and check if it lies between 1 and 10.
   - Output the result for each test case.

### Solution:

```python
def solve():
    T = int(input())  # Number of test cases
    for _ in range(T):
        A, B = map(int, input().split())  # Read A and B
        C = 21 - A - B  # Calculate the third number required to make the sum 21
        if 1 <= C <= 10:  # Check if the third number is valid
            print(C)
        else:
            print(-1)

```

### Explanation of the Code:

1. **Input Reading**:
   - The number of test cases \( T \) is read first.
   - Then, for each test case, the values \( A \) and \( B \) are read using `map(int, input().split())`.
   
2. **Logic**:
   - For each test case, compute \( C = 21 - A - B \).
   - If \( C \) is between 1 and 10 (inclusive), print \( C \), otherwise print -1.

3. **Output**:
   - For each test case, the corresponding result is printed.

### Time Complexity:
- Each test case requires constant time \( O(1) \) for the calculations and comparisons. Given that there are \( T \) test cases, the overall time complexity is \( O(T) \).

### Example Walkthrough:

#### Input:
```
3
5 6
7 8
10 10
```

#### Output:
```
10
6
-1
```

#### Explanation:
1. **Test Case 1**:
   - \( A = 5 \), \( B = 6 \), so \( C = 21 - 5 - 6 = 10 \). Since \( C = 10 \), which is a valid number, the answer is 10.
   
2. **Test Case 2**:
   - \( A = 7 \), \( B = 8 \), so \( C = 21 - 7 - 8 = 6 \). Since \( C = 6 \), which is a valid number, the answer is 6.
   
3. **Test Case 3**:
   - \( A = 10 \), \( B = 10 \), so \( C = 21 - 10 - 10 = 1 \). Since \( C = 1 \), which is valid, the answer is -1.

