# -*- coding: utf-8 -*-

import random


def random_str(length=8):
    """"""
    rs = list()
    chars = [chr(i) for i in range(65, 91)]
    chars.extend([chr(i) for i in range(97, 123)])
    chars.extend([str(i) for i in range(10)])
    chars = ''.join(chars)
    for i in range(length):
        rs.append(random.choice(chars))
    return ''.join(rs)


if __name__ == '__main__':
    """"""
    print('Running ...')
    print(random_str())
