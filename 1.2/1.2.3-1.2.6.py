# Dominic Sciara
# LEVEL 1
# 1.2.3-1.2.6
# this program will create, manipulate and print lists using loops


def main():
    print '\t\tEXERCISE 1.2.3 \n############################'
    numbers1 = range(1, 1000)
    for num in numbers1:
        print str(num) + ','
    print 1000

    print '\t\tEXERCISE 1.2.4 \n############################'
    numbers2 = range(1, 998, 2)
    for num in numbers2:
        print str(num) + ','
    print 999

    print '\t\tEXERCISE 1.2.5 \n############################'
    numbers3 = numbers1 + numbers2
    for num in numbers3:
        print str(num) + ','
    print 997

    print '\t\tEXERCISE 1.2.6 \n############################'
    numbers4 = numbers3[::-1]
    numbers4 = numbers4[:-1]
    for num in numbers4:
        print str(num) + ','
    print 1


###################################
if __name__ == '__main__':
    main()