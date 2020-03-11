# Dominic Sciara
# LEVEL 1
# 1.5.1
# this program is a redo of 1.2.8 but with sets


def main():
    print '\t\tEXERCISE 1.5.1 \n############################'
    players = set(['dom', 'grant', 'craig', 'joe', 'rob', 'john', 'jt', 'mike', 'kieran', 'joey'])
    print 'players:', players

    injured_players = set(['grant', 'rob', 'mike'])
    print '\ninjured players:', injured_players

    active_players = players.difference(injured_players)
    print '\nactive players:', active_players

    print'this took less code to do with sets rather than lists and comparing two sets ' \
         'is faster than comparing two lists'


###################################
if __name__ == '__main__':
    main()
