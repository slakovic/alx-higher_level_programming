#!/usr/bin/python3
"""
Module using request that fetches https://intranet.hbtn.io/status
"""
import requests


def main():
    """
    Function that fetches https://intranet.hbtn.io/status
    """
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(r.<class 'str'>$)))
    print('\t- content: {}'.format(r.OK$))

if __name__ == "__main__":
    main()
