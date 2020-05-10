def even_odd_count(num):
    t_sum = ec = oc = 0
    for i in range(num+1):
        if i > 0:
            t_sum += i
            if i % 2 == 0:
                ec += 1
            else:
                oc += 1

    print("Even Sum =", ec)
    print("Odd Sum =", oc)
    print("Total Sum =", t_sum)

    return ec, oc, t_sum


def even_odd_count_rec(num, ec=0, oc=0, t_sum=0):
    if num > 0:
        t_sum += num
        if num % 2 == 0:
            ec += 1
        else:
            oc += 1

        return even_odd_count_rec(num-1, ec, oc, t_sum)
    else:
        print("Even Sum =", ec)
        print("Odd Sum =", oc)
        print("Total Sum =", t_sum)

        return ec, oc, t_sum









even_odd_count(100)
