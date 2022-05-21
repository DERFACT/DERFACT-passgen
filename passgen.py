'''DERFACT-passgen -- Command line password generator
   Copyright (C) 2022 DERFACT Corporation,
   DERFACT-passgen is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   DERFACT-passgen is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
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
