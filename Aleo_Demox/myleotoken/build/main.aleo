program myleotoken.aleo;

record Token:
    owner as address.private;
    balance as u32.private;


function mint:
    input r0 as u32.private;
    cast self.caller r0 into r1 as Token.record;
    output r1 as Token.record;


function transfer:
    input r0 as address.private;
    input r1 as u32.private;
    input r2 as Token.record;
    sub r2.balance r1 into r3;
    cast r0 r1 into r4 as Token.record;
    cast self.caller r3 into r5 as Token.record;
    output r4 as Token.record;
    output r5 as Token.record;


function main:
    input r0 as u32.public;
    input r1 as u32.private;
    add r0 r1 into r2;
    output r2 as u32.private;
