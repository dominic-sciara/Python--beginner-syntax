# Dominic Sciara
# LEVEL 1
# 1.5.2
# this program will analyze popular names in the usa and britain using sets


def main():
    print '\t\tEXERCISE 1.5.2 \n############################'
    usa = {
        'James', 'John', 'Robert', 'Micheal', 'William', 'David', 'Richard', 'Charles', 'Joseph',
        'Thomas', 'Christopher', 'Daniel', 'Paul',  'Mark', 'Donald', 'George', 'Kenneth', 'Steven',
        'Edward', 'Brian'}
    britain = {
        'Muhammad', 'Oliver', 'Harry','Jack', 'George', 'Noah', 'Leo', 'Jacob', 'Oscar', 'Charlie',
        'Jackson', 'William', 'Joshua', 'Ethan', 'James', 'Freddie', 'Alfie', 'Logan', 'Lucas',
        'Finley'}
    print '\nUSA:', usa
    print 'Britain:', britain

    print '\nnames in both countries:', usa.intersection(britain)
    print 'names in usa but not britain', usa.difference(britain)
    print 'name in britain but not usa', britain.difference(usa)


###################################
if __name__ == '__main__':
    main()
