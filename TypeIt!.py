#-------INFO-------
# Name : TypeIt!
# Creator : Daxeel Soni
# Language : Python 3.3.3
# Connect me : http://www.linkedin.com/in/daxeel

#-------SOURCE CODE-------
import random
import time
import sys

print('Application Name : TypeIt!')
print('Version          : 1.0')
print('Developer        : Daxeel Soni\n')

def level():
    total_time = 0
    crrct = 0
    while True:
        randoms = []
        i = 1
        while i <= int(lvl):
            x = chr(random.randint(65, 90))
            randoms.append(x)
            i = i + 1
        word = ''
        i = 0
        while i < len(randoms):
            word = word + randoms[i]
            i = i + 1
        print('\n' + word)
        start = time.time()
        y = input('Enter : ')
        if word == y.upper():
            end = time.time() - start
            total_time = total_time + end
            crrct = crrct + 1
        else:
            end = time.time() - start
            total_time = total_time + end
            print('\nGame Over')
            print('Number correct questions is ' + str(crrct))
            print('Your total time is ' + str(format(total_time, '.2f')) + ' seconds')
            ch = input('\nPress any key for replay and E for exit : ')
            if ch.lower() == 'e':
                sys.exit()
            else:
                level()

while True:
    lvl = input('Enter length (eg.5) : ')
    if len(lvl) != 0:
        level()
        break
    else:
        print('Invalid length input!')

