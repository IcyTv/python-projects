import string, sys

def encipher(st, key):
    res = ''
    stl = []
    let = string.ascii_lowercase
    for i in st:
        stl.append([let.index(i.lower()), i.isupper()])
    for n in stl:
        n[0] += key
        if n[0] > 26:
            n[0] -= 26
        if n[1]:
            res += let[n[0]].upper()
        else:
            res += let[n[0]]

    return res

def decipher(st, key):
    res = ''
    stl = []
    let = string.ascii_lowercase
    for i in st:
        stl.append([let.index(i.lower()), i.isupper()])
    for n in stl:
        n[0] -= key
        if n[0] < 0:
            n[0] += 26
        if n[1]:
            res += let[n[0]].upper()
        else:
            res += let[n[0]]
    return res

if __name__ == '__main__':
    print 'Usage: ' + __file__ + ' [EN/DE] [String] [Key]'
    try:
        Code = str(sys.argv[1])
    except:
        Code = raw_input('Encode [EN] or decode [DE]: ')
    try:
        st = str(sys.argv[2])
    except:
        st = raw_input('String: ')
    try:
        key = int(sys.argv[3])
    except:
        key = int(raw_input('Key [1-25]: '))

    if Code == 'EN':
        print encipher(st, key)
    elif Code == 'DE':
        print decipher(st, key)
    else:
        print '"EN" or "DE"'
        sys.exit(0)
