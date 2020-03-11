# Dominic Sciara
# LEVEL 1
# 1.5.5
# this program is a redo of 1.2.8 but with sets


def main():
    print '\t\tEXERCISE 1.5.5 \n############################'
    d = {'China': 1384688986, 'India': 1296834042, 'United States': 329256465, 'Indonesia': 262787403,
         'Brazil': 208846892, 'Pakistan': 207862518, 'Nigeria': 195300343, 'Bangladesh': 159453001,
         'Russia': 142122776, 'Japan': 126168156}
    while True:
        q = raw_input('What country would you like to know the population of? ')
        if q == '0':
            break
        elif q in d.keys():
            print d[q]
        else:
            p = raw_input('this country is not in the database, please enter the population for this country: ')
            d[q] = int(p)

    print '\nunsorted:'
    for key, value in d.iteritems():
        print key, value

    print '\nsorted by country name:'
    for key, value in sorted(d.iteritems(), key=lambda (k, v): k):
        print key, value

    print '\nsorted by country population:'
    for key, value in sorted(d.iteritems(), key=lambda (k, v): -v):
        print key, value

###################################
if __name__ == '__main__':
    main()
