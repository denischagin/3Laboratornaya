def inputs():
    while True:
        x = int(input('Введите натуральное число:'))
        if x > 0:
            break
        print('Неверные данные')
    return x


def x2(x):
    return collatz(x // 2)


def x3_1(x):
    return collatz(x * 3 + 1)


def collatz(x):
    s = [x]
    if x == 1:
        pass
    elif x % 2 == 0:
        s.extend(x2(x))
    else:
        s.extend(x3_1(x))
    return s


if __name__ == '__main__':
    a = inputs()
    print(collatz(a))
