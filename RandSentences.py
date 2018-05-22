from random import shuffle

def get_dupes(ls):
    tmp = []
    for i in ls:
        if i in tmp:
            del ls[ls.index(i)]
        else:
            tmp.append(i)
    return ls

if __name__ == '__main__':
    inp = raw_input('Sentence: ').split(' ')
    res = []
    while len(res) < len(inp):
        shuffle(inp)
        res.append(' '.join(inp))
        res = get_dupes(res)

    for i in res:
        print i
