# Dominic Sciara
# LEVEL 1
# 1.2.2
# this program will preform various operations on a developer initiated list of numbers


def main():
    print '\t\tEXERCISE 1.2.2 \n############################'
    numbers = [6, 4.4, 11.8, 55, -7, 0, 100, 75.1, 3, 81]

    print '\nA. first two numbers'
    print 'BEFORE:', numbers
    print 'AFTER:',  numbers[:2]

    print'\n#################'

    print '\nB. last two numbers'
    print 'BEFORE:', numbers
    print 'AFTER:',  numbers[-2:]

    print'\n#################'

    print '\nC. all numbers, excluding the last one'
    print 'BEFORE:', numbers
    print 'AFTER:', numbers[:-1]


    print'\n#################'

    print '\nD. all numbers, excluding the first one'
    print 'BEFORE:', numbers
    print 'AFTER:',  numbers[1:]

    print'\n#################'

    print '\nE. all numbers, excluding the first two and the last three'
    print 'BEFORE:', numbers
    print 'AFTER:',  numbers[2:-3]

    print'\n#################'

    print '\nF. all numbers, with an extra one appended at the end'
    print 'BEFORE:', numbers
    numbers.append(101)
    print 'AFTER:', numbers

    print'\n#################'

    print '\nG. all numbers, with an extra 5 appended at the end'
    print 'BEFORE:', numbers
    print 'AFTER:', numbers + [-42, 6, 2, 600, 1001]

    print'\n#################'

    print '\nH. all numbers, with "300" inserted after the third number'
    print 'BEFORE:', numbers
    numbers.insert(3, 300)
    print 'AFTER:', numbers

    print'\n#################'

    print '\nI. all numbers, with the fourth to last number modified'
    print 'BEFORE:', numbers
    numbers[-4] = 500
    print 'AFTER:', numbers

    print'\n#################'

    print '\nJ. all numbers printed backwards'
    print 'BEFORE:', numbers
    print 'AFTER:', numbers[::-1]

    print'\n#################'

    print '\nK. every secong item in the list'
    print 'BEFORE:', numbers
    print 'AFTER:', numbers[::2]

    print'\n#################'

    print '\nK. every secong item in the list backwards'
    print 'BEFORE:', numbers
    print 'AFTER:', numbers[::-2]


###################################
if __name__ == '__main__':
    main()