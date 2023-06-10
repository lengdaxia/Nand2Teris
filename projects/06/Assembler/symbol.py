import json
import re 
from os.path import dirname, join

re_symbol = re.compile('[$:.\w]+')
digit = ('0','1','2','3','4','5','6','7','8','9')
addr=15


def install_symbol(name):
    pass

def install_label(name,defn):
    pass

def install(name, defn=None):
    if defn is None:
        return install_symbol(name)
    return install_label(name, defn)
