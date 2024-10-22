# Function to compute the bitwise AND from Left to Right
def range_bitwise_and(left, right):
   #write your code here
    shift_count = 0
    
    while left != right:
        left >>= 1
        right >>= 1
        shift_count += 1

    return left << shift_count

# Default Test Cases
test_cases = [
    (5, 7),      # Output: 4
    (0, 0),      # Output: 0
    (1, 2147483647)  # Output: 0
]

# Running Test Cases
for left, right in test_cases:
    print(range_bitwise_and(left, right))

# Sample Output:
# 4
# 0
# 0