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
    pass

def push(mem_seg,index):
    pass

def pop(mem_seg, index):
    pass

def label(label_name,function_name):
    pass

def init():
    pass

def function(function_name, n_vars):
    pass

def call(callee, n_args, caller):
    pass

def get_return():
    pass

def goto(label_name,function_name):
    pass

def if_goto(label_name,function_name):
    pass

if __name__ == '__main__':
    if len(sys.argv) != 2 :
        raise Exception('input argment not valid')
    main(sys.argv[1])

