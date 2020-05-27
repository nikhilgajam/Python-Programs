# Pattern printing in python


def right_angled_triangle(num):

    for i in range(1, num+1):           # 1
        for j in range(1, i+1):         # 1 2
            print(j, end=" ")           # 1 2 3
        print()


def another_ra_triangle(num):

    for i in range(num, 1, -1):         # 1 2 3
        for j in range(1, i):           # 1 2
            print(j, end=" ")           # 1
        print()


def ra_triangles_combined(num):

    for i in range(1, num+1):           # 1
        for j in range(1, i+1):         # 1 2
            print(j, end=" ")           # 1
        print()

    for i in range(num, 1, -1):
        for j in range(1, i):
            print(j, end=" ")
        print()


def rl_triangle(num):
    k = 2 * num - 2

    for i in range(1, num+1):
        for j in range(1, k+1):
            print(end=" ")

        k = k - 2
        for j in range(1, i+1):
            print(j, end=" ")
        print()

        '''
            1
          1 2
        1 2 3
        '''


def another_rl_triangle(num):
    k = 2 * num - 2

    for i in range(num, 0, -1):
        for j in range(k-1, 0, -1):
            print(end=" ")

        k = k + 2
        for j in range(1, i+1):
            print(j, end=" ")
        print()

        '''
        1 2 3
          1 2
            1
        '''


def combined_rl_triangle(num):
    k = num * 2 - 2

    for i in range(1, num+1):
        for j in range(1, k+1):
            print(end=" ")
        k = k - 2
        for j in range(1, i+1):
            print(j, end=" ")
        print()

    k = k + 4  # Important line

    for i in range(num-1, 0, -1):
        for j in range(1, k+1):
            print(end=" ")
        k = k + 2
        for j in range(1, i+1):
            print(j, end=" ")
        print()

        '''
            1
          1 2
        1 2 3
          1 2
            1
        '''


def eq_triangle(num):
    k = 2 * num - 2

    for i in range(1, num+1):
        for j in range(1, k+1):
            print(end=" ")

        k = k - 1
        for j in range(1, i+1):
            print(j, end=" ")     # Replace j with * or any symbol to print symbol
        print()

        '''
          1
         1 2 
        1 2 3
        '''


def another_eq_triangle(num):
    k = 2 * num - 2

    for i in range(num, 0, -1):
        for j in range(1, k+1):
            print(end=" ")

        k = k + 1
        for j in range(1, i+1):
            print(j, end=" ")
        print()

        '''
        1 2 3
         1 2
          1
        '''


def combined_eq_triangle(num):
    k = 2 * num - 2

    for i in range(1, num+1):
        for j in range(1, k+1):
            print(end=" ")
        k = k - 1
        for j in range(1, i+1):
            print(j, end=" ")
        print()

    k = num  # Important line

    for i in range(num-1, 0, -1):
        for j in range(1, k+1):
            print(end=" ")
        k = k + 1
        for j in range(1, i+1):
            print(j, end=" ")
        print()

        '''
          1
         1 2
        1 2 3
         1 2
          1
        '''


right_angled_triangle(6)
