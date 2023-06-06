// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// make R2 = 0
@R2 
M=0

// if r0 > 0, goto loop
@R0  
D=M 
@LOOP 
D;JGT 

// else goto end 
@END 
0;JMP 

// if R0 > 0, goto loop else end
(LOOP)
    // get R2
    @R2 
    D=M 
    // R2=R2+R1
    @R1 
    D=D+M 
    @R2 
    M=D

    //R0=R0-1
    @R0 
    D=M-1 
    M=D

    // if R0 > 0 then loop else next
    @LOOP
    D;JGT

(END)
    @END
    0;JMP


