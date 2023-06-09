

def a_type(asm):
    return "0"

def c_type(asm):
    pass

def asm2hack(asm):
    if asm.startswith("@"):
        return a_type(asm)
    else:
        return c_type(asm)