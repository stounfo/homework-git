def logging(func_name, result):
    with open('/tmp/logfile', 'a') as file:
        file.write('\n')
        file.write(f'{func_name}: {result}')


def sum(a, b):
    res = a + b
    logging(func_name='sum', result=res)
    return res


def power(a, b):
    res = a ** b
    logging(func_name='power', result=res)
    return res


def multiplication(a, b):
    res = a * b
    logging(func_name='multiplication', result=res)
    return res
