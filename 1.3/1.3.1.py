# Dominic Sciara
# LEVEL 1
# 1.3.1
# this program will output the day of the week given a number from the user


def day(num):
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return days[num]


# helper function to validate user inputs
def valid(user_input):
    try:
        int(user_input)
    except ValueError:
        return False
    else:
        if int(user_input) > 0 and int(user_input) <= 7:
            return True
        else:
            return False


def main():
    print '\t\tEXERCISE 1.3.1 \n############################'
    while True:
        ui = raw_input('please enter a day of the week (represented as a number): ')
        if not valid(ui):
            print 'WARNING! input is invalid'
            continue
        break
    print day(int(ui))



###################################
if __name__ == '__main__':
    main()