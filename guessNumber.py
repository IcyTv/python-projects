from random import randint

if __name__ == '__main__':
    num = randint(1,1200)
    inp = 0
    while inp != num:
        inp = int(raw_input('Guess: '))
        if inp > num:
            print 'Smaller\n'
        elif inp < num:
            print 'Bigger\n'
    else:
        print 'RIGHT'
