# Dominic Sciara
# LEVEL 1
# 1.1.7
# this program will ask the user for the dimensions of a triangle
# and calculate the area of that triangle


# helper function to validate user inputs
def valid(user_input):
    if type(user_input) is int or type(user_input) is float:
        if user_input > 0:
            return True
    else:
        return False


def main():
    print '\t\tEXERCISE 1.1.7 \n############################'
    while True:
        base = input('please enter the base: ')
        height = input('please enter the height: ')
        if not valid(height) or not valid(base):
            print 'WARNING! input is invalid'
            continue
        break

    area = 0.5 * float(base) * float(height)
    print 'the area is ', area



###################################
if __name__ == '__main__':
    main()