# Dominic Sciara
# LEVEL 1
# 1.5.7
# this program will filter dicts of mortgages


def mortgages():
    return {
            '6HJ218': 123, 'HFG461': 804, 'POQ123': 445, 'KKL910': 265,
            'LIJ445': 534, 'FNM221': 423, 'QOP112': 505, '09KLNM': 746,
            'ABF12F': 457, 'ALSDK45': 999, 'ASDK90': 323, 'BVLA78': 433,
            'KDFJLA': 438, 'OBLIVI': 262, 'MONEY1': 875
            }


def main():
    print '\t\tEXERCISE 1.5.7 \n############################'
    m = mortgages()
    mini_m = {}
    standard_m = {}
    jumbo_m = {}

    for k, v in m.iteritems():
        if v < 200:
            mini_m[k] = v
        elif 200 <= v <= 467:
            standard_m[k] = v
        else:
            jumbo_m[k] = v

    print '\nA. '
    print 'original mortgages:', m

    print '\nmini mortgages:', mini_m
    print 'standard mortgages:', standard_m
    print 'jumbo mortgages:', jumbo_m

    # modifying a mortgage in jumbo mortgages
    jumbo_m['QOP112'] = 506
    print '\nafter modification to jumbo mortgages'
    print 'jumbo mortgages:', jumbo_m
    print 'original mortgages:', m

    # extracting lists of values from each dict
    mini_vals = mini_m.values()

    mini_vals[0] = 1
    print '\nafter modification to mini mortgages values'
    print 'mini mortgages:', mini_m
    print 'original mortgages:', m






###################################
if __name__ == '__main__':
    main()
