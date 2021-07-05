#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def order(n):
    list = []
    string = str(n)
    for i in range(0,len(string)):
        list.append(string[i])
    list =sorted(list)
    string = ''.join(list)
    integer = int(string)
    return integer

def check(n,m):
    m = order(m)
    n = order(n)
    if ((n-m) == 0):
        return True
    else:
        return False

def b(list):
    for i in range(0,len(list)):
        if list[i] != True:
            return False

for x in range(2,1000000):
    for i in range(2,6):
        values = []
        boolean = check(i*x,x)
        values.append(boolean)
    f = b(values)
    if(f != False):
        print(x)
        break;

