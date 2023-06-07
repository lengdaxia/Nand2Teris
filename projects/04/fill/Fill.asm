// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// if Keyboard > 0 ? FILL : CLEAR

(LOOP)
    // get keyborad value.
    @KBD 
    D=M 

    // jump to on If it's more than 0
    @ON 
    D;JGT 

    // Jump to off otherwise
    @OFF 
    0;JMP 


// Turn the sreen on and loop
(ON)
    // set the draw value R0=-1 (1111111111111111)
    @R0 
    M=-1

    //Draw 
    @DRAW 
    0;JMP 

// Turn the screen of and loop.
(OFF)
    //set R0=0,(0000000000000000)
    @R0
    M=0

    //draw
    @DRAW
    0;JMP 

(DRAW)

    //set counter R1=8192
    @8191
    D=A 
    @R1 
    M=D 

    // walk the sreen and set values to R0
    (NEXT)
    // calculte position
    @R1 
    D=M 
    @pos 
    M=D 
    @SCREEN 
    D=A 
    @pos 
    M=M+D 

    //actually draw the value at the current position
    @R0 
    D=M 
    @pos 
    A=M 
    M=D 

    // counter --
    @R1 
    D=M-1 
    M=D 

    // count >= 0, draw next 
    @NEXT 
    D;JGE 

// loop again and wait user to press keyborad
@LOOP 
0;JMP 




