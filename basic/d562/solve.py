"""
每次處理方法:
    1. 翻轉
    2. 消除最後一個
"""

numbers = [99, 77, 66, 44, 11]
# new_nembers = []
# for i in range(5-1, -1, -1):
#     # print(numbers[i])
#     new_nembers.append(numbers[i])
# numbers = new_nembers

# print(numbers)
numbers.reverse()
print(numbers)
numbers.pop()
print(numbers)

[11,44,66,77,0]