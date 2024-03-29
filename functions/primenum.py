# def is_prime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True
#
# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()

def is_prime(num):
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()