# 50. Pow(x, n)
# Example 1:
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

x = 2
n = 10
result = 1
for _ in range(abs(n)):
    result *= x
if n < 0:
    result = 1/result
print(result)
