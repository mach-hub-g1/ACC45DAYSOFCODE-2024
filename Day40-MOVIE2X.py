# cook your dish here
# Reading input
X, Y = map(int, input().split())

# Time spent on first Y minutes at 2x speed
time_for_first_Y = Y // 2

# Time spent on the remaining part of the movie
time_for_remaining = X - Y

# Total time Chef spends watching the movie
total_time = time_for_first_Y + time_for_remaining

# Output the total time
print(total_time)
