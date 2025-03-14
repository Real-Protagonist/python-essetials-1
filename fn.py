def f(x):
    if x == None:
        return 0
    return x + f(x - 1)
print(3)
def fn1(a):
    return a ** a

def fn2(a):
    return fn1(a) * fn2(a)

def fnn(x):
    if x % 2 == 0:
        return 1
    else:
        return

def ef(x):
    global y
    y = x * x
    return y

ef(2)
# print(y)
# print(fnn(fnn(2)) + 1)

def any():
    print(var + 1, end='')

var = 1
any()

my = [4, 2, 8, 7]
my[1] = my[1] + my[0]
print(my)

 
# my_list =  ['Mary', 'had', 'a', 'little', 'lamb']


# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'


# print(my_list(my_list))

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
 
for k in range(len(dictionary)):
    v = dictionary[v]
 
print(v)

print()

tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

print()

try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")

try:
    prin("ses")
except:
    print("Errot")