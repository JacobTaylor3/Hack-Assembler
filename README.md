A Python implementation of an assembler for the Hack computer architecture from Nand2Tetris.

The assembler takes programs written in the Hack Assembly Language (.asm) and translates them into 16-bit Hack machine code (.hack) that can be executed by the Hack CPU.

This project was completed as Project 6 of The Elements of Computing Systems: Building a Modern Computer from First Principles.

Overview

The Hack platform uses a simple 16-bit instruction set consisting of three types of assembly commands:

A-instructions — load a constant or symbolic address into the A register
C-instructions — perform computations, assignments, and jumps
L-instructions — define symbolic labels used for branching

For example:

@R0
D=M
@R1
D=D-M
@GREATER
D;JGT

The assembler converts these instructions into binary machine code:

0000000000000000
1111110000010000
0000000000000001
1111010011010000
0000000000001010
1110001100000001
Features
Converts .asm files into .hack machine-code files
Supports A, C, and L instructions
Handles predefined Hack symbols
Supports user-defined labels
Automatically allocates memory addresses for variables
Removes whitespace and comments during parsing
Implements the Hack instruction encoding defined by the Hack ISA
Uses a two-pass assembly process for resolving symbols and labels
Architecture

The assembler is divided into several components, each responsible for a specific part of the translation process.

                    Hack Assembly Program
                            │
                            ▼
                       assembler.py
                            │
             ┌──────────────┴──────────────┐
             │                             │
        First Pass                    Second Pass
             │                             │
             ▼                             ▼
      Resolve Labels              Translate Instructions
             │                             │
             ▼                             ▼
      symbol_table.py              parser.py / code.py
             │                             │
             └──────────────┬──────────────┘
                            │
                            ▼
                     Hack Machine Code
                            │
                            ▼
                        .hack file
