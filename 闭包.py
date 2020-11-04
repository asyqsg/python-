'''
闭包
'''

def print_msg():
    msg = 'print_msg'

    def printer():
        print(msg)

    return print

a = print_msg()
a()