def sum(a, b):
    res = a + b
    with open('/tmp/logfile', 'a') as file:
        file.write('\n')
        file.write(f'sum: {res}')

    return res


def power(a, b):
    res = a ** b
    with open('/tmp/logfile', 'a') as file:
        file.write('\n')
        file.write(f'power: {res}')

    return res


def multiplication(a, b):
    res = a * b
    with open('/tmp/logfile', 'a') as file:
        file.write('\n')
        file.write(f'multiplication: {res}')

    return res
