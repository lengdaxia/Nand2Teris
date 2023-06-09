#!/usr/bin/env python3

from os.path import basename
from sys import argv, exit
from instruction import asm2hack
from ass_symbol import install 


PROG = basename(argv[0])

def abort_assembly(nl=None, line=None, *args):
    print(PROG + ':error', end='')
    nl is not None and print(' on line ', nl)
    print('\t >'+line.rstrip() if line else ': program argument')
    for l in args:
        print(l)
    exit(1)

if len(argv) != 2:
    abort_assembly(0,0,'Usage: ' + PROG + ' FILE')

infile = argv[1]

if not infile.endswith('.asm'):
    abort_assembly(0,0,"expectd 'asm' file extension")

# test.asm => test.hack
outfile = infile[:-4] + '.hack'

def decomment(line):
    '''remove comments and external white space'''
    return line.split("//")[0].strip()

with open(infile, 'r') as fi:
    asm = fi.readlines()

ninstr = 0 # instruction number
#install tables to symbol tables
for nl, asm_line in enumerate(asm):
    nl += 1
    asm_instr = decomment(asm_line)
    if not asm_instr:
        continue
    if asm_instr.startswith('('):
        if install(asm_instr, ninstr) is None:
            abort_assembly(nl, asm_line, 'label invalid or redefined')
    else:
        ninstr += 1

with open(outfile, 'w') as fo:
    for nl, asm_line in enumerate(asm):
        nl+=1
        asm_instr=decomment(asm_line)
        if not asm_instr or asm_instr.startswith('('):
            continue
        hack=asm2hack(asm_instr)
        if not hack:
            abort_assembly(nl,asm_line)
        fo.write(hack)
