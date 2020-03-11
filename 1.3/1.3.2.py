# Dominic Sciara
# LEVEL 1
# 1.3.2
# this program will return the fibonacci sequence as a list

import time


# recursive with memoization
def recursive_memo_fib(n, mem = {0: 1, 1: 1}):
    if n in mem.keys():
        return mem[n]
    else:
        mem[n] = (recursive_memo_fib(n - 1, mem) + recursive_memo_fib(n - 2, mem))
        return mem[n]


# just recursive
def recursive_fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)


# iterative
def iterative_fib(n):
    lst = [1, 1]
    if n >= 2:
        for x in range(2, n + 1):
            lst.append(lst[x - 1] + lst[x - 2])
        return lst[-1]
    else:
        return 1


def main():
    ui = raw_input('input n: ')

    start = time.time()
    print '\nrecursive with memo:', recursive_memo_fib(int(ui))
    print 'time elapsed:', time.time() - start

    start = time.time()
    print '\nrecursive:', recursive_fib(int(ui))
    print 'time elapsed:', time.time() - start

    start = time.time()
    print '\niterative:', iterative_fib(int(ui))
    print 'time elapsed:', time.time() - start


###################################
if __name__ == '__main__':
    main()
