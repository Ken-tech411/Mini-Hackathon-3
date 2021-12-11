# Bai 1
# def expression():
#     count = 1
#     for i in range(2, num + 1):
#         count *= i
#     return count

# num = int(input("Input a number: "))
# print(f"{num}! = {expression()}")

# Bai 2
# list = [5, 1, 8, 92, -1, 30]
# def sorted_list(list):
#     for i in range(len(list)):
#         for j in range(i + 1, len(list)):
#             if list[i] > list[j]:
#                 list[i], list[j] = list[j], list[i]
#     return list

# print(sorted_list(list))

# Bai 3
# def fibonacci(n):
#     n1, n2 = 1, 1
#     count = 0
#     if n <= 0:
#         print("Please input a positive integer")
#     else:
#         print(f"First {n} Fibonacci number(s):")
#         while count < n:
#             print(n1, end = " ")
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
#             count += 1

# n = int(input("Input number: "))
# fibonacci(n)