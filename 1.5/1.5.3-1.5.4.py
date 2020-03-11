# Dominic Sciara
# LEVEL 1
# 1.5.3-1.5.4
# this program is a redo of 1.2.8 but with sets


def main():
    print '\t\tEXERCISE 1.5.3 \n############################'
    m = [100, 650, 671, 489, 501, 390, 299, 106, 178, 478, 711]
    print '\nmortgages:', m

    print '\n\t\tEXERCISE 1.5.4 \n############################'
    t = {10, 15, 30}
    print 'terms:', t
    t.add(5)
    print 'terms after add:', t
    t.remove(15)
    print 'terms after remove:', t
    t.discard(45)
    print 'terms after discard:', t
    # we use discard here instead of remove because we are not sure if 45 is in the set
    # and if it is not remove would throw an error and discard would not


###################################
if __name__ == '__main__':
    main()
