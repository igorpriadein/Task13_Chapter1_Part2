# For a given integer N, print all the squares of integer numbers where the
# square is less than or equal to N, in ascending order.
integer = int(input("input your integer "))
print([i**2 for i in range(1, integer+1) if i**2 <= integer])
