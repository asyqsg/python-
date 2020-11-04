'''
装饰器
'''

from functools import wraps
def a_new_decorator(a_func):

    @wraps(a_func)
    def wrapThrFunction():
        print('func()前')

        a_func()

        print('func()后')

    return wrapThrFunction

@a_new_decorator
def a_func_require_decoration():
    print('装饰器')


a_func_require_decoration()
print(a_func_require_decoration.__name__)