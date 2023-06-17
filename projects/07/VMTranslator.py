import sys, os 

# define constants
C_RETURN = 0
C_ARITHMETIC = 1
C_PUSH = 2
C_POP = 3
C_LABEL = 4
C_GOTO = 5 
C_IF = 6 
C_CALL = 7
C_FUNCTION = 8 

mem_seg_to_pointer = {'local':'LCL',
                      'argument': 'ARG',
                        'this':'THIS',
                        'that':'THAT'}
num_labeled = 0
file_name = ''

def main(file_or_dir):
    global file_name
    input_files = []
    if os.path.isdir(file_or_dir):
        for (dirpath, dirnames, filenames) in os.walk(file_or_dir):
            for file in filenames:
                if file.endswidth('.vm'):
                    input_files.append(os.path.join(dirpath, file))
            if file_or_dir.endswith('/'):
                file_name = os.path.basename(file_or_dir[:-1])
            else:
                file_name = os.path.basename(file_or_dir)
            output_file = file_name + ".asm"
    elif file_or_dir.endswith('.vm'):
        input_files = [file_or_dir]
        file_name = file_or_dir[:-3]
        output_file = file_name + '.asm'
    else:
        print('Usage python VMTranslor XXX.vm || python VMTranslator my_directory')
        return
    
    with open(output_file,'w') as asm:
        if os.path.isdir(file_or_dir):
            for instrcution in init():
                asm.write(instrcution + '\n')
        
        for this_input_file in input_files:
            file_name = os.path.basename(this_input_file)
            current_function = ""
            with open(this_input_file,'r') as vm:
                for command in vm:
                    command = command.split('//')[0].strip()
                    if command == "":
                        continue
                    
                    # parse command and use command_type to determine 
                    # which sequence of assembly instrctuon to write
                    command_type, arg1, arg2 = parse(command) 
                    asm_instrctions = []
                    if command_type == C_ARITHMETIC:
                        asm_instrctions = arithmetic(arg1)
                    elif command_type == C_PUSH:
                       asm_instrctions = push(arg1, arg2)
                    elif command_type == C_POP:
                        asm_instrctions = pop(arg1, arg2)
                    elif command_type == C_RETURN:
                        asm_instrctions = get_return()
                    elif command_type == C_LABEL:
                        asm_instrctions = label(arg1, current_function)
                    elif command_type == C_GOTO:
                        asm_instrctions = goto(arg1, current_function)
                    elif command_type == C_IF:
                        asm_instrctions = if_goto(arg1, current_function)
                    elif command_type == C_CALL:
                        asm_instrctions = call(arg1, arg2, current_function)
                    elif command_type == C_FUNCTION:
                        asm_instrctions = function(arg1, arg2)
                        current_function = arg1
                    
                    for instruction in asm_instrctions:
                        asm.write(instrcution + '\n')


def parse(command):
    command_map = {
        "return": C_RETURN,
        "add": C_ARITHMETIC,
        "sub": C_ARITHMETIC,
        "neg": C_ARITHMETIC,
        "eq": C_ARITHMETIC,
        "gt": C_ARITHMETIC,
        "lt": C_ARITHMETIC,
        "and": C_ARITHMETIC,
        "or": C_ARITHMETIC,
        "not": C_ARITHMETIC,
        "label": C_LABEL,
        "goto": C_GOTO,
        "if-goto": C_IF,
        "push": C_PUSH,
        "pop": C_POP,
        "call": C_CALL,
        "function": C_FUNCTION
    }

    tokens = command.split()

    if len(tokens) == 1:
        return command_map[tokens[0]], tokens[0], None 
    elif len(tokens) == 2:
        return command_map[tokens[0]], tokens[1], None
    elif len(tokens) == 3:
        return command_map[tokens[0]], tokens[1], tokens[2]

def arithmetic(operation):
    """: returns lits of hack assembly instructions to perform operation on top 1 or 2 stack items"""
    if operation in ['add','sub']:
        op = '+' if operation == 'add' else '-1'
        return [
            f"// {operation}",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            f"M=M{op}D"
        ]
    elif operation in ['neg', 'not']:
        op = '-' if operation == 'neg' else '!'
        return [
            f"// {operation}",
            "@SP",
            "A=M-1",
            f"M={op}M"
        ]
    elif operation in ['eq', 'gt','lt']:
        jump_op = {'op': 'JNE','gt':'JLE','lt':'JGE'}[operation]
        global num_labeled
        num_labeled += 1
        return [
            f"// {operation}",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=M-D",
            f"@Not{operation + str(num_labeled)}",
            f"D; {jump_op}",
            "@SP",
            "A=M-1",
            "M=-1",
            f"@End{operation + str(num_labeled)}",
            "0; JMP",
            f"(Not{operation+str(num_labeled)})",
            "@SP",
            "A=M-1",
            "M=0",
            f"(End{operation + str(num_labeled)})"
        ]
    elif operation in ['and', 'or']:
        op = '&' if operation == 'and' else '|'
        return [
            f"// {operation}",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            f"M=D{op}M"
        ]
    else:
        return []

def push(mem_seg,index):
    pass

def pop(mem_seg, index):
    pass

def label(label_name,function_name):
    return [
        f"// label {label_name}",
        f"({function_name}${label_name})"
    ]

def init():
    asm_code = ["// init",
                "@256",
                "D=A",
                "@SP",
                "M=D"]

def function(function_name, n_vars):
    asm_code = [
        f"// function {function_name} {n_vars}",
        f"({function_name})"
    ]
    n_vars = int(n_vars)
    if n_vars >= 1:
        asm_code += ["@SP",
                     "A=M",
                     "M=0"]
        for i in range(n_vars - 1):
            asm_code += ["AD=A+1",
                         "M=0"]
        if n_vars >= 2:
            asm_code += ["@SP",
                         "M=D"]
    return asm_code

def call(callee, n_args, caller):
    global num_labeled
    num_labeled += 1
    return_address = f"{caller}$ret.{num_labeled}"
    return [
        f"// call {callee} {n_args}",
        f"@{return_address}",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "D=A+1",
        "@LCL",
        "D=D+M",
        "A=D-M",
        "M=D-A",
        "D=A+1",
        "@ARG",
        "D=D+M",
        "A=D-M",
        "M=D-A",
        "D=A+1",
        "@THIS",
        "D=D+M",
        "A=D-M",
        "M=D-A",
        "@SP",
        "D=M",
        f"@{n_args}",
        "D=D-A",
        "@ARG",
        "M=D",
        "@5",
        "D=A",
        "@SP",
        "MD=M+D",
        "@LCL",
        "M=D",
        f"@{callee}",
        "0; JMP",
        f"({return_address})"
    ]

def get_return():
    return [
        "// return",
        "@LCL",
        "D=M",
        "@5",
        "A=D-A",
        "D=M",
        "@retAddr",
        "M=D",
        "@SP",
        "A=M-1",
        "D=M",
        "@ARG",
        "A=M",
        "M=D",
        "@ARG",
        "D=M+1",
        "@SP",
        "M=D",
        "@LCL",
        "AM=M-1",
        "D=M",
        "@THAT"
    ]

def goto(label_name,function_name):
    return [
        f"// goto {label_name}",
        f"@{function_name}${label_name}",
        "0; JMP"
    ]

def if_goto(label_name,function_name):
    return [
        f"// if-goto {label_name}",
        "@SP",
        "AM=M-1",
        "D=M",
        f"@{function_name}${label_name}",
        "D; JNE"
    ]

if __name__ == '__main__':
    if len(sys.argv) != 2 :
        raise Exception('input argment not valid')
    main(sys.argv[1])

