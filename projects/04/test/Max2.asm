// pseudocode
// r2 = max(r0,r1)
// if(r0>r1) then r2 = r0 
//           else r2 = r1

// r2 = r0
@r0
D=M
@r2 
M=D

// if r0 - r1 > 0 goto end 
@r0 
D=M 
@r1 
D=D-M 
// then -> condition -> else
@END 
D;JGT
//else r2 = r1  
@r1 
D=M 
@r2 
M=D 
// end 
(END)
@END
0;JMP 