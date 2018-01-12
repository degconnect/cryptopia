#!/usr/bin/env python

import os

from cryptopia import Cryptopia

CRYPTOPIA_API_KEY = os.environ.get('CRYPTOPIA_API_KEY')
CRYPTOPIA_API_SECRET = os.environ.get('CRYPTOPIA_API_SECRET')


def main():
    crypto = Cryptopia(CRYPTOPIA_API_KEY, CRYPTOPIA_API_SECRET)

    deposits, err = crypto.get_transactions('Deposit')
    if err is None:
        for item in deposits:
            print(item)
    else:
        print(err)


if __name__ == '__main__':
    main()
