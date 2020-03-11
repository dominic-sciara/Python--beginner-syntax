# Dominic Sciara
# LEVEL 1
# 1.6.1
# this program will demonstrate importing and using a package

import math
from math import factorial

def main():
    print '\t\tEXERCISE 1.6.1 \n############################'

    print dir(math)

    print math.factorial(5)

    print math.floor(5.8)

    print factorial(5)


###################################
if __name__ == '__main__':
    main()
