# Dominic Sciara
# LEVEL 1
# 1.5.8
# this program will filter dicts of tuples


def mortgages():
    return {
            '867E23': (100000, 5, 300), '151E23': (981091, 5, 300), '967E23': (330892, 3.5, 360),
            '267E23': (451900, 3.5, 360),
            '367E23': (600422, 7, 100), '467E23': (407190, 4, 180), '467E23': (219432, 7, 360),
            '867E25': (800728, 5, 120),
            '867E24': (211121, 5, 120), '687E23': (781789, 8, 120), '911E23': (900432, 5, 360),
            '777E23': (321234, 3, 120),
            '913E23': (111243, 4, 180), '887E23': (654890, 6, 180), '667E23': (728876, 6, 300),
            '999E23': (601109, 7, 180),
            '000E23': (948234, 5, 360), '001E23': (891543, 5.5, 120), '002E23': (431395, 4, 300),
            '003E23': (444234, 8, 180),
            '0004E23': (577123, 4, 120), '006E23': (129783, 7, 100), '007E23': (670781, 3.5, 360),
            '008E23': (600671, 6.3, 120)
            }


def war(mt):
    pool = float(sum([a for (a, r, t) in mt]))
    weights = [(a/pool) * (r/100.0) for (a, r, t) in mt]
    return sum(weights) * 100


def wam(mt):
    pool = float(sum([a for (a, r, t) in mt]))
    weights = [(a / pool) * t for (a, r, t) in mt]
    return sum(weights)


def main():
    print '\t\tEXERCISE 1.5.8 \n############################'

    print 'sorting tuple values:'
    s = [val for tup in mortgages().values() for val in tup]
    print sorted(s, reverse=True)

    print '\nweighted average rate:', round(war(mortgages().values()), 2)

    print '\nweighted average maturity:', round(wam(mortgages().values()), 2)

    new_m = {}
    for (a, r, t) in mortgages().values():
        if new_m.get(t):
            new_m[t].append((a, r))
        else:
            new_m[t] = [(a, r)]
    print new_m


###################################
if __name__ == '__main__':
    main()

