# Dominic Sciara
# LEVEL 1
# 1.3.3-1.3.6
# this program will calculate the mean and variance in different ways


def mean(lst):
    return sum(lst) / len(lst)


def variance(sample, df = 0):
    m = mean(sample)
    v = [((x - m) ** 2) for x in sample]
    if (df == 0):
        return sum(v) / (len(v) - 1)
    else:
        return sum(v) / len(v)


def alt_mean(*args):
    return sum(args) / len(args)


def main():
    print '\t\tEXERCISE 1.3.3 \n############################'
    lst = []

    print 'input a list on numbers (enter "s" to stop): '
    while True:
        x = raw_input('')
        if x == 's':
            break
        else:
            lst.append(float(x))

    print 'mean', mean(lst)

    print '\n\t\tEXERCISE 1.3.4 \n############################'

    print 'variance for sample', variance(lst)

    print '\n\t\tEXERCISE 1.3.5 \n############################'

    print 'variance for population', variance(lst, 1)

    print '\n\t\tEXERCISE 1.3.6 \n############################'

    print 'alt mean', alt_mean(12, 3, 3, 5, 5, 3)


###################################
if __name__ == '__main__':
    main()