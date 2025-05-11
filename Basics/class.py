# By default, functions return None
def test():
    print('in test function')

def disk_area(radius:float) -> float:
    return 3.14 * radius ** 2

# Default values are evaluated when the function is defined, not when it is called. This can be problematic when using mutable types
# and modifying them in the function body, since the modifications will be persistent across invocations of the function.
bigx = 10
def double_it(x = bigx):
    return x * 2
bigx = 1e9
double_it()


def add_to_dict(args=None):
    if args is None:
        args = {'a': 1, 'b': 2}
    for i in args.keys():
        args[i] += 1
    print(args)

def variable_args(*args, **kwargs):
    print('args is', args)
    print('kwargs is', kwargs)

variable_args('one', 'two', x =1, y = 2, z = 3)
va = variable_args
va('three', x = 1, y = 2)
