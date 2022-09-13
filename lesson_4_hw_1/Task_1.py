import math


def degrees2radians(degrees):  # returns float: radians value
    return degrees * (math.pi / 180.0)


print('cos 45 :' + str((degrees2radians(math.cos(45)))))
print('cos 40 :' + str((degrees2radians(math.cos(40)))))
print('cos 60 :' + str((degrees2radians(math.cos(60)))))
