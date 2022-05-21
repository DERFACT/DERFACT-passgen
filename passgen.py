import sys
import random

numbers = '1234567890'
letters_l = 'abcdefghijklmnopqrstuvwxyz'
letters_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!#$%&()*+./:;=>?@[\]^`{|}~\'_-'

arg = sys.argv
password_symbols = letters_l

def passgen(password_symbols, password_len = 12, count = 10):
    for c in range(count):
        result = ''
        for i in range(password_len):
            r = random.randint(0, len(password_symbols) - 1)
            result += password_symbols[r]
        print(result)

def arg_nums(arg):
    password_len = 12
    count = 10
    if arg[0].isnumeric():
            password_len = int(arg[0])
            if len(arg) > 1:
                if arg[1].isnumeric():
                    count = int(arg[1])
    passgen(password_symbols, password_len, count)

if len(arg) > 1:
    arg.pop(0)
    if '-' in arg[0]:
        if 'n' in arg[0]:
            password_symbols += numbers
        if 'u' in arg[0]:
            password_symbols += letters_u
        if 's' in arg[0]:
            password_symbols += symbols
            
        if len(arg) > 1:
            arg.pop(0)
            arg_nums(arg)
        else:
            passgen(password_symbols)
    else:
        password_symbols += letters_u + numbers
        arg_nums(arg)
else:
    password_symbols += letters_u + numbers
    passgen(password_symbols)