import time


def time_12_hours():
    t = time.ctime()
    change = int(t[11:13]) % 12
    temp = t[11:]
    temp = temp.replace(t[11:13], str(change), 1)
    t = t[0:11] + temp

    return t


print(time_12_hours())



























