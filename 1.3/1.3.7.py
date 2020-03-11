# Dominic Sciara
# LEVEL 1
# 1.3.7
# this program will work with displays key word arguments


def display(name, age, **kwargs):
    print 'Name:', name
    print 'Age:', age
    for kw in kwargs:
        print kw + ':', kwargs[kw]


def main():
    print '\t\tEXERCISE 1.3.7 \n############################'
    display('dominic', '23', State='NY', Height='6 foot')


###################################
if __name__ == '__main__':
    main()
