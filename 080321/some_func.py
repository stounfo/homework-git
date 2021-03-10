def logging(func):
    def wrapper(*args):
        result = func(*args)
        with open('/tmp/logfile', 'a') as file:
            file.write('\n')
            file.write(f'{func.__name__}: {result}')

        return result

    return wrapper


@logging
def sum(a, b):
    res = a + b
    return res


@logging
def power(a, b):
    res = a ** b
    return res


@logging
def multiplication(a, b):
    res = a * b
    return res


if __name__ == '__main__':
    a = sum(1, 10)
