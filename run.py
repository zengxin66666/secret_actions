import git_base
from git_base import *
from sys import exit as sys_exit
from getconf import getConf
from base64 import b64decode

import argparse
parser = argparse.ArgumentParser(description = 'run.py @Limour')
parser.add_argument('-nup','--notuseprint', action='store_true', default=False,
        dest='nup',
        help='not use print')
config = getConf(parser)
results = parser.parse_args()

upstream = config["upstream"]
codes = config["exec"]
codes = b64decode(codes).decode('utf-8')
# https://tool.oschina.net/encrypt?type=3
usePip = config["usePip"]
usePrint = config["usePrint"]
if (not usePrint) or results.nup:
    tmp_print = print
    def print(*arg, **kw):
        tmp_print('not allow to print')
    git_base.print = print

try_call(git_add_upstream, upstream)

git_c2upstream()

if usePip:
    ret = pip_install()
    if ret:
        sys_exit(ret)

exec(codes)

