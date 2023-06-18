// push constant 17
@17
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 17
@17
D=A
@SP
AM=M+1
A=A-1
M=D
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
@Noteq1
D; JNE
@SP
A=M-1
M=-1
@Endeq1
0; JMP
(Noteq1)
@SP
A=M-1
M=0
(Endeq1)
// push constant 17
@17
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 16
@16
D=A
@SP
AM=M+1
A=A-1
M=D
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
@Noteq2
D; JNE
@SP
A=M-1
M=-1
@Endeq2
0; JMP
(Noteq2)
@SP
A=M-1
M=0
(Endeq2)
// push constant 16
@16
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 17
@17
D=A
@SP
AM=M+1
A=A-1
M=D
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
@Noteq3
D; JNE
@SP
A=M-1
M=-1
@Endeq3
0; JMP
(Noteq3)
@SP
A=M-1
M=0
(Endeq3)
// push constant 892
@892
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 891
@891
D=A
@SP
AM=M+1
A=A-1
M=D
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@Notlt4
D; JGE
@SP
A=M-1
M=-1
@Endlt4
0; JMP
(Notlt4)
@SP
A=M-1
M=0
(Endlt4)
// push constant 891
@891
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 892
@892
D=A
@SP
AM=M+1
A=A-1
M=D
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@Notlt5
D; JGE
@SP
A=M-1
M=-1
@Endlt5
0; JMP
(Notlt5)
@SP
A=M-1
M=0
(Endlt5)
// push constant 891
@891
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 891
@891
D=A
@SP
AM=M+1
A=A-1
M=D
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@Notlt6
D; JGE
@SP
A=M-1
M=-1
@Endlt6
0; JMP
(Notlt6)
@SP
A=M-1
M=0
(Endlt6)
// push constant 32767
@32767
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 32766
@32766
D=A
@SP
AM=M+1
A=A-1
M=D
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@Notgt7
D; JLE
@SP
A=M-1
M=-1
@Endgt7
0; JMP
(Notgt7)
@SP
A=M-1
M=0
(Endgt7)
// push constant 32766
@32766
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 32767
@32767
D=A
@SP
AM=M+1
A=A-1
M=D
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@Notgt8
D; JLE
@SP
A=M-1
M=-1
@Endgt8
0; JMP
(Notgt8)
@SP
A=M-1
M=0
(Endgt8)
// push constant 32766
@32766
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 32766
@32766
D=A
@SP
AM=M+1
A=A-1
M=D
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@Notgt9
D; JLE
@SP
A=M-1
M=-1
@Endgt9
0; JMP
(Notgt9)
@SP
A=M-1
M=0
(Endgt9)
// push constant 57
@57
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 31
@31
D=A
@SP
AM=M+1
A=A-1
M=D
// push constant 53
@53
D=A
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
// push constant 112
@112
D=A
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
// neg
@SP
A=M-1
M=-M
// and
@SP
AM=M-1
D=M
A=A-1
M=D&M
// push constant 82
@82
D=A
@SP
AM=M+1
A=A-1
M=D
// or
@SP
AM=M-1
D=M
A=A-1
M=D|M
// not
@SP
A=M-1
M=!M
