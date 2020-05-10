def print_n_times(num):

    for i in range(num):
        print(i)


def print_n_times_rec(num):
    if num >= 0:
        print(num)
        return print_n_times_rec(num-1)
    else:
        return None


def print_n_times_asc_rec(num, count=0):
    if num > count:
        num += 1
        print(count)
        return print_n_times_asc_rec(num - 1, count + 1)
    else:
        return


print_n_times(100)
