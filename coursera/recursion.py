# a = [[96], [69]]

# print(''.join(list(map(str, a))))

# z = ["alpha","bravo","charlie"]
# new_z = [i[0]*2 for i in z]
# print(new_z)
# def sum(n):
#    if n == 1:
#        return 0
#    return n + sum(n-1)

# a = sum(5)
# print(a)

value = 7
class A:
    value = 5
a = A()
a.value = 3
print(value)
bravo = 3
b = B()
class B:
    bravo = 5
    print("Inside class B")
c = B()
print(b.bravo)