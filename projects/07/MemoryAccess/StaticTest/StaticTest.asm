// push constant 111
@111
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 333
@333
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 888
@888
D=A
@SP
AM=M+1
A=A-1
M=D
// pop static 8
@SP
AM=M-1
D=M
@StaticTest.vm8
M=D
// pop static 3
@SP
AM=M-1
D=M
@StaticTest.vm3
M=D
// pop static 1
@SP
AM=M-1
D=M
@StaticTest.vm1
M=D
// push static 3
@StaticTest.vm3
D=M
@SP
AM=M+1
A=A-1
M=D
// push static 1
@StaticTest.vm1
D=M
@SP
AM=M+1
A=A-1
M=D
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-1D
// push static 8
@StaticTest.vm8
D=M
@SP
AM=M+1
A=A-1
M=D
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
