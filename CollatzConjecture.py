num = int(raw_input('Number: '))
steps = 0

while num > 1:
    if num%2 == 0:
        num /= 2
    else:
        num *= 3
        num += 1
    steps += 1

print "Amount of steps: " + str(steps)
