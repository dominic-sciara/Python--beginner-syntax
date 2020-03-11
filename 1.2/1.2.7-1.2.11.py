# Dominic Sciara
# LEVEL 1
# 1.2.7-1.2.11
# this program will create and filter lists using using list comprehensions

import time

def main():
    print '\t\tEXERCISE 1.2.7 \n############################'
    list1 = [x ** 2 for x in range(0, 101)]
    print 'initial list:', list1

    list2 = [x for x in list1 if x > 1000]
    print '\nA.', list2

    list3 = [x for x in list2 if x % 2 == 0]
    print '\nB.', list3

    ###################################################

    print '\n\n\t\tEXERCISE 1.2.8 \n############################'
    players = ['dom', 'grant', 'craig', 'joe', 'rob', 'john', 'jt', 'mike', 'kieran', 'joey']
    print 'players:', players

    injured_players = ['grant', 'rob', 'mike']
    print '\ninjured players:', injured_players

    active_players = [p for p in players if p not in injured_players]
    print '\nactive players:', active_players

    ###################################################

    print '\n\n\t\tEXERCISE 1.2.9 \n############################'
    names = ['brandon', 'nick', 'rick', 'russel', 'chris']
    print 'names:', names

    ages = [12, 33, 61, 3, 40]
    print '\nages:', ages

    names_ages = zip(names, ages)
    print '\nnames with ages:', names_ages

    over18 = [name for name, age in names_ages if age > 18]
    print '\nnames with ages over 18:', over18

    ###################################################

    print '\n\n\t\tEXERCISE 1.2.10 \n############################'
    big_list = range(10000001)
    start =  time.time()
    loop_list = []
    for num in big_list:
        if num % 10 == 0:
            loop_list.append(num)
    print 'the loop took', time.time() - start

    start = time.time()
    comp_list =  [num for num in big_list if num % 10 == 0]
    print 'the list comprehension took', time.time() - start

    print '\n\n\t\tEXERCISE 1.2.11 \n############################'
    double_list = [[3, 2, 1, 3, 3], ['charlie', 'sam', 'steve'], [3, 'hey', 8]]
    print 'double list:', double_list

    flat_list = [item for lst in double_list for item in lst]
    print 'flat list:', flat_list


###################################
if __name__ == '__main__':
    main()