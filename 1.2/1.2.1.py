# Dominic Sciara
# LEVEL 1
# 1.2.1
# this program will take number from a user until the user enters 's'
# then calculate the mean of the numbers inputted


# helper function to validate user inputs
def valid(user_input):
    try:
        float(user_input)
    except ValueError:
        return False
    else:
        if float(user_input) > 0:
            return True
        else:
            return False


def main():
    print '\t\tEXERCISE 1.2.1 \n############################'
    numbers = []
    while True:
        number = raw_input('please enter a number (type "s" when done with input): ')
        if number == 's':
            break
        elif valid(number):
            numbers.append(float(number))
        else:
            print 'WARNING! number is entered is not valid'
            continue
    if len(numbers):
        ttl = 0.0
        for num in numbers:
            ttl += num
        print 'the average of the numbers entered is', ttl / len(numbers)
    else:
        print 'no numbers inputted'


###################################
if __name__ == '__main__':
    main()