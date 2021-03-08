def a(*args):
    print(args, type(args))


a(10, 11, 12)


def a(arg1, arg2, arg3=3):  # default value
    print(arg1, arg2, arg3)


a(10, 11, 12)
a(arg2=11, arg1=10, arg3=12)


def a(**kwargs):
    print(kwargs, type(kwargs))


a(arg2=11, arg1=10, arg3=12)


def a(*args, **kwargs):
    print(args, type(args), kwargs, type(kwargs))


a(10, 11, 12, arg1=10, arg2=11, arg3=12)
