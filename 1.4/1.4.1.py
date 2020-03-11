# Dominic Sciara
# LEVEL 1
# 1.4.1
# this program will filter lists of mortgages


def mortgages():
    return [123, 804, 445, 265, 534, 423, 505, 746, 457, 999, 323, 433, 438, 262, 875]

def main():
    print '\t\tEXERCISE 1.4.1 \n############################'
    m = mortgages()
    mini_m = [x for x in m if x < 200]
    standard_m = [x for x in m if 200 <= x <= 467]
    jumbo_m = [x for x in m if x > 467]

    print '\nA. '
    print 'mortgages:', m

    print '\nB. '
    print 'mini mortgages:', mini_m
    print 'standard mortgages:', standard_m
    print 'jumbo mortgages:', jumbo_m

    print '\nC. '
    print 'verification of mini mortgages:', all([x < 200 for x in mini_m])
    print 'verification of standard mortgages:', all([200 <= x <= 467 for x in standard_m])
    print 'verification of jumbo mortgages:', all([x > 467 for x in jumbo_m])

    print '\nD. '
    print 'second verification of mini mortgages:', not(any([x > 200 for x in mini_m]))
    print 'second verification of standard mortgages:', not(any([x < 200 or x > 467 for x in standard_m]))
    print 'second verification of jumbo mortgages:', not(any([x < 467 for x in jumbo_m]))

    print '\n\t\tEXERCISE 1.4.2 \n############################'

    print '\nlength of mini mortgages:', len(mini_m)
    print 'length of standard mortgages:', len(standard_m)
    print 'length of jumbo mortgages:', len(jumbo_m)
    print 'verification of lengths:', len(mini_m) + len(standard_m) + len(jumbo_m) == len(m)

    print '\n\t\tEXERCISE 1.4.3 \n############################'
    print '\n sum of all mortgages (in thousands):', sum(m)

    print '\n\t\tEXERCISE 1.4.4 \n############################'
    print '\nminimum of all mortgages (in thousands):', min(m)
    print 'max of all mortgages (in thousands):', max(m)


###################################
if __name__ == '__main__':
    main()
