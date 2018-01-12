#!/usr/bin/env python

from cryptopia import Cryptopia


def main():
    crypto = Cryptopia()

    currencies, err = crypto.get_currencies()
    if err is None:
        for coin in currencies:
            print(coin)


if __name__ == '__main__':
    main()
