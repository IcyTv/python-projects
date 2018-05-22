from copy import copy
import math

def square(a):
    return a*a

def rectangle(a, b):
    return a*b

def circle(r):
    return 2*r*math.pi

def triangle(b,h):
    return b*h/2

def ball(r):
    return 4*math.pi*r**2

def cuboid(a, b, c):
    return 2*a+2*b+2*c

def cube(a):
    return 6*a*a


def switch(n):
    return opt.get(n,None)


def striplngth(st):
    res = st.split(' ')
    return (int(res[0]), res[1])


opt = {
    1: square,
    2: rectangle,
    3: circle,
    4: triangle
    }
opt2 = {
'square': 1,
'rectangle': 2,
'circle': 1,
'triangle': 2
}


if __name__ == '__main__':
    lst = []
    for n, i in opt.iteritems():
        print str(n) + ': ' + i.__name__
    iopt = int(raw_input('Option: '))
    num = opt2[opt[iopt].__name__]
    for i in xrange(num):
        inp = striplngth(raw_input('Value: '))
        lst.append(inp[0])
    if num == 1:
        print str(opt[iopt](lst[0])) + ' q' + inp[1]
    elif num == 2:
        print str(opt[iopt](lst[0], lst[1])) + ' q' + inp[1]
    elif num == 3:
        print str(opt[iopt](lst[0], lst[1], lst[2])) + ' q' + inp[1]
