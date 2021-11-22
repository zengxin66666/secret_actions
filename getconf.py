from json import loads as json_loads
from sys import argv as sys_argv
from aes_cbc import encrypt, decrypt

import argparse
def add_argument(parser):
    parser.add_argument('-cde','--confdecrypt', action='store_true', default=False,
        dest='cde',
        help='decrypt mode')
    parser.add_argument('-ck','--confkey', action='store',
            dest='key',
            help='aes_cbc KEY')
    parser.add_argument('-civ','--confiv', action='store',
            dest='iv',
            help='aes_cbc IV')
    parser.add_argument('-cp','--confpath', action='store', default='conf.json',
            dest='path',
            help='conf.json path')
    return parser
def get_parser_results():
    parser = argparse.ArgumentParser(description = 'getconf.py @Limour')
    parser = add_argument(parser)
    results = parser.parse_args()
    return results

if __name__ == "__main__":
    results = get_parser_results()
    path = results.path
    k = input('Please input k \n') if not results.key else results.key
    iv = input('Please input iv \n') if not results.iv else results.iv
    ec = input('encrypt?(y/n)') == 'y' if not results.cde else not results.cde
    with open(path, 'rb') as f:
        pdata = f.read()
    if ec:
        pdata = encrypt(k, iv, pdata)
    else:
        pdata = decrypt(k, iv, pdata)
    with open(path, 'wb') as f:
        f.write(pdata)
    print(f'-ck "{k}"', f'-civ "{iv}"')
    input('exit?')

def getConf(parser=None):
    if not parser:
        results = get_parser_results()
    else:
        parser = add_argument(parser)
        results = parser.parse_args()
    path = results.path
    with open(path, 'rb') as f:
        pdata = f.read()
    if results.key and results.iv:
        k = results.key
        iv = results.iv
        pdata = decrypt(k, iv, pdata)
    pdata = pdata.decode('utf-8')
    config = json_loads(pdata)
    return config
        
