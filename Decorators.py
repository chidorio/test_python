# def outer_func(msg):
#     def inner_func():
#         print(msg)
#     return inner_func
#
#
# hi_func = outer_func('Hi')
# bye_func = outer_func('Bye')
#
# hi_func()
# bye_func()
#
#
# def decorator_func(original_func):
#     def wrapper_func(*args, **kwargs):
#         print('wrapper method executed this before {}'.format(original_func.__name__))
#         return original_func(*args, **kwargs)
#     return wrapper_func
#
#
# class DecoratorClass:
#
#     def __init__(self, original_func):
#         self.original_func = original_func
#
#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(self.original_func.__name__))
#         return self.original_func(*args, **kwargs)
#
#
# @decorator_func
# def display():
#     print('display func run')
#
#
# @decorator_func
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))
#
#
# display_info('John', 25)
# display()
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
        )
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
