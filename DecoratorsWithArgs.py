def prefix_decorator(prefix):
    def decorator_func(orig_func):
        def wrapper_func(*args, **kwargs):
            print(prefix, 'Executed Before', orig_func.__name__)
            result = orig_func(*args, **kwargs)
            print(prefix, 'Executed After', orig_func.__name__, '\n')
            return result

        return wrapper_func
    return decorator_func


@prefix_decorator('TESTING:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 35)
