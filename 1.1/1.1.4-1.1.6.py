# Dominic Sciara
# LEVEL 1
# 1.1.4-1.1.6
# This program will take input from a user and store the input
# it will also print the data type of the input from the user
# then the program will display output describing the users input

def main():

    print '\t\tEXERCISE 1.1.4 \n############################'
    x = input('please input something: ')

    print '\n\t\tEXERCISE 1.1.5 \n############################'
    print type(x)

    print '\n\t\tEXERCISE 1.1.6 \n############################'

    if type(x) is int or type(x) is float:
        print'The inputted value is a number'

        if x < 65:
            print 'the inputted number is less than 65'
            if x > 64:
                print 'the inputted number is between 64 and 65'
        if x > 64:
            print 'the inputted number is greater than 64'

    elif type(x) is str:
        print 'the inputted value is a string'

    else:
        print'the inputted value is neither a string nor number'



###################################
if __name__ == '__main__':
    main()