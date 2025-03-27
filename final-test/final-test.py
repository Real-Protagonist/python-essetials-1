
#$ Q.01
my_list = [3, 2]
for v in range(2):
    print(v)
    my_list.insert(-1, my_list[v])

print(my_list)

#$ Q.05
def  function_1(a):
    return None

def function_2(a):
    return function_1(a) * function_2(a)

#$ Q.06
print(1 // 2)

#$ Q.07
def func(a, b):
    return b ** a

# print(func(b=2, 2))

#$ Q.08
z = 0
y = 10

# x = y < z and z > y or y < z and z < y
# print = x
# # print(print)

#$ Q.10
my_list = [x * x for x in range(5)]


def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))

#$ Q.11
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)

#$ Q.12
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(3 ^ 1)

#$ Q.14
nums = [1, 2, 3]

vals = nums
del vals[:]
print(nums)

#$ Q.15
# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x

#$ Q.16
# y = input()
# x = input()

#$ Q.17
print("a", "b", "c", sep="sep")

#$ Q.18
x = 1 // 5 + 1 / 5
print(x)

#$ Q.19
my_tuple = [1, 3]
my_tuple[1] = my_tuple[1] + my_tuple[0]
print(my_tuple)

#$ Q.20
# x = float(input())
# y = float(input())
# print(y ** (1/x))

#$ Q.21
dct = {'one':'two', 'three':'one','two':'three'}
v = dct['three']
for k in range(len(dct)):
    v = dct[v]

print(v)

#$ Q.22
lst = [i for i in range(-1, -2)]
print(lst)

#$ Q.24
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)

print(fun(0, 3))

#$ Q.25
# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*")

#$ Q.26
# tup = (1,2,4,8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)

#$ Q.27
# dd = {"1":"0", "0":"1"}
# for x in dd.vals(): #Erroneous
#     print(x, end="")

#$ Q.28
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end=" ")


#$ Q.29
def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))

#$ Q.30
lst = [[x for x in range(3)] for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

#$ Q.31
# try:
#     value = input("Enter a value: ")
#     print(int(value)/len(value))
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Boo!")

#$ Q.32
# try:
#     print(5/0)
#     break
# except:
#     print("Sorry, something went wrong...")
# except (ValueError, ZeroDivisionError):
#     print("Too bad...")

#$ Q.33
foo = (1, 2, 3)
foo.index(0)
print(foo)

#$ Q. 35
print(Hello, World!)

