
import json
import re 
from os.path import dirname, join
from ass_symbol import install, lookup

re_asm = re.compile('[01ADMEGJLNPQT=;!+&|-]{1,11}')
r_pattern = re.compile(r'^R(0|1[0-5])$')

json_file = join(dirname(__file__), 'tables.json')
with open(json_file) as f:
    tables = json.load(f)

comptable = tables['comp']
desttable = tables['dest']
jumptable = tables['jump']
del tables

def int2hack(n):
    return '{:016b}\n'.format(n)

def a_type(asm):
    expr = asm[1:] # remove '@'
    print('a_type expr:',expr)
    if expr.isdigit():
        hack = int(expr)
    elif r_pattern.match(expr): # R0~R15
        hack = int(expr[1:]) # remove 'R'
    else:
        hack = lookup(expr) or install(expr)
    if hack is None:
        return None
    
    return int2hack(hack)

def c_type(asm):
    cmd = ''.join(asm.split())
    if not re_asm.fullmatch(cmd) or cmd.count('=') > 1 or cmd.count(';') > 1:
        return None

    eq = cmd.index('=') if '=' in cmd else 0
    sc = cmd.index(';') if ';' in cmd else  len(cmd)

    dest = cmd[:eq]
    comp = cmd[eq:sc].lstrip('=')
    jump = cmd[sc:].lstrip(';')

    hack = '111'

    # a field
    hack += '1' if 'M' in comp else '0'

    # comp filed 
    if comp not in comptable:
        return None
    hack += comptable[comp]

    # dest filed
    if dest not in desttable:
        return None
    hack += desttable[dest]

    # jump field
    if jump not in jumptable:
        return None
    hack += jumptable[jump]

    hack += '\n'
    return hack

def asm2hack(asm):
    if asm.startswith("@"):
        return a_type(asm)
    else:
        return c_type(asm)