# cook your dish here
# Read the input
A, B, C, X = map(int, input().split())

# Check if X is one of the topics Chef has prepared
if X in (A, B, C):
    print("Yes")
else:
    print("No")
