def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# A more compact version


# def is_a_triangle(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:  # you can also use "and" rather than using "or" to make it more compact
#         return False
#     return True
#
#
# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))