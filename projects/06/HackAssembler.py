import sys, os

ST = {
    "R0":0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,

    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}

def main():
    if len(sys.argv) != 2:
        print('Usage: python HackAssembler.py xxx.asm')
        sys.exit(1)

    input_file = sys.argv[1]
    output_fule = input_file[:-3] + "hack"

    # add labels to ST and strip whitespace and comments
    with open(input_file, 'r') as program, open('temp.asm', 'w') as temp:
        instrcution_number = 0

        for line in program:
            line = line.strip()

            # remove blank lines
            if line == "":
                continue
            # ignore comment line
            if line.startswith('//'):
                continue
            #  remove trailing comments
            line = line.split('//')[0]

            # write clean line to temo.asm, 
            # or add label and its value to ST
            if line.startswith('('):
                symbol = line[1:-1]
                value = instrcution_number
                ST[symbol] = value
            else:
                temp.write(line + '\n')
                instrcution_number += 1

    # second: parse and decode instructions
    with open("temp.asm","r") as temp, open(output_fule, 'w') as out:
        n = 16
        binary_instruction = "0000000000000000"

        for instruction in temp:
            instruction = instruction.strip()
            # handle A command
            if instruction.startswith("@"):
                if not is_symbol(instruction[1:]): 
                    # @constant
                    binary_instruction = code_a_command(int(instruction[1:]))

                else: # var or label
                    if instruction[1:] in ST:
                        binary_instruction = code_a_command(ST[instruction[1:]])
                    else:
                        ST[instruction[1:]] = n 
                        binary_instruction = code_a_command(n)
                        n += 1
            else: #handl C command
                dest, comp, jump = parser(instruction)
                binary_instruction = code_c_command(dest,comp, jump)
        
            # write to output file   
            out.write(binary_instruction + "\n")


    # remove temp.asm file 
    os.remove('temp.asm')
    

def is_symbol(string):
    try:
        int(string)
        return False
    except ValueError:
        return True

def dec_to_bin(num:int, current=''):
    if num < 1:
        return current
    current = str(num%2) + current
    x = dec_to_bin(num // 2, current)
    return x 

def parser(c_instrcution):
    # c => desc, comp, jump
    parse1 = c_instrcution.split('=')

    if len(parse1) == 2:
        dest = parse1[0].strip()
        comp = parse1[1].split(';')[0].strip()
    else:
        dest = None 
        comp = parse1[0].split(';')[0].strip()
    
    jump = c_instrcution.split(';')[-1].strip()
    if jump not in ["JEQ", "JNE", "JGT", "JGE", "JLT", "JLE", "JMP"]:
        jump = None

    return dest, comp, jump

# @1 -> 
def code_a_command(value: int):
    bin_val = dec_to_bin(value)
    if len(bin_val) > 15:
        raise Exception('A-command memmory address out of ranges, Tried @' + str(value))
    return '0'*(16-len(bin_val)) + bin_val

def code_c_command(dest, comp, jump):
    # encode dest
    if dest:
        bin_dest = ''.join([
            '1' if 'A' in dest else '0',
            '1' if 'D' in dest else '0',
            '1' if 'M' in dest else '0',
        ])
    else:
        bin_dest = '000'
    
    # encode jump
    if jump:
        if jump == 'JMP':
            bin_jump = '111'
        elif jump == 'JNE':
            bin_jump = '101'
        else:
            bin_jump = ''.join([
                '1' if 'L' in jump else '0',
                '1' if 'E' in jump else '0',
                '1' if 'G' in jump else '0'
            ])
    else:
        bin_jump = '000'

    # encode comp which cannot be None
    bin_a = '1' if 'M' in comp else '0'
    if '0' in comp:
        bin_comp = '101010'
    
    elif '1' in comp:
        if "-" in comp:
            if "D" in comp:
                # D - 1
                bin_comp =  "001110"
            elif "A" in comp or "M" in comp:
                # A - 1 or M - 1
                bin_comp =  "110010"
            else:
                # -1
                bin_comp = "111010"
        elif "+" in comp:
            if "D" in comp:
                # D + 1
                bin_comp =  "011111"
            elif "A" in comp or "M" in comp:
                # A + 1 or M + 1
                bin_comp = "110111"
        else:
            # 1
            bin_comp = "111111"
    elif '!' in comp:
        if "D" in comp:
            # !D
            bin_comp = "001101"
        else:
            # !A or !M
            bin_comp = "110001"
    elif '&' in comp:
        # D & A or D & M
        bin_comp = "000000"
    elif '|' in comp:
        # D|A or D|M
        bin_comp = "010101"
    elif 'D' in comp and '+' in comp:
        # D+A or D+M
        bin_comp = "000010"
    elif 'D' in comp and ('A' in comp or 'M' in comp):
        # Must be D-A, D-M, A-D, or M-D
        if comp.index("D") < comp.index("-"):
            bin_comp = "010011"
        else:
            bin_comp = "000111"

    else:
        #  must be D or A or M
        if 'D' in comp:
            bin_comp = '001100'
        else:
            bin_comp = '110000'
    return "111" + bin_a + bin_comp + bin_dest + bin_jump

if __name__ == '__main__':
    main()