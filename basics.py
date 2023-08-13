# n = int(input("How many rows you want to have? "))


# for i in range(n):
#     for j in range(n, i, -1):
#         print(" ", end="")
#     for k in range(i+1):
#         print("*", end="")
#     print()


# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(n, i, -1):
#         print("*", end="")
#     print()

# n = int(input("Which Fibo you want to calculate? "))


# def fibonacci(n, memo={}):
#     if n <= 1:
#         return n

#     if n not in memo:
#         memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)

#     return memo[n]


# print(f"Fibo{n} is: {fibonacci(n)}")


dic = {1, 2, 3, 4, 5}
print(dic["1"])
