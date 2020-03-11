# Dominic Sciara
# LEVEL 1
# 1.5.6
# this program will find the mode of values




def mode(values):
    f = {}
    for value in values:
        if not f.get(value):
            f[value] = 1
        else:
            f[value] += 1
    m = sorted(f.iteritems(), key=lambda (k, v): -v)
    return m[0]


def main():
    print '\t\tEXERCISE 1.5.6 \n############################'
    print mode([1,2,3,4,4,3,2,1,1,1,2,3,4])

###################################
if __name__ == '__main__':
    main()
