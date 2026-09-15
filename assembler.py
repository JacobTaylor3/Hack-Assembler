from symbol_table import SymbolTable
from parser import Parser

from code import dest, comp, jump

import sys


# combines everything; the actual assembler calls other modules
class Assembler:

    def __init__(self, path):

        self.symbol_table = SymbolTable()
        self.parser = Parser(path=path)

    def init_symbol_table(self):

        for i in range(16):  # R0-15

            self.symbol_table.add_entry("R" + str(i), i)

        self.symbol_table.add_entry("SP", 0)
        self.symbol_table.add_entry("LCL", 1)
        self.symbol_table.add_entry("ARG", 2)
        self.symbol_table.add_entry("THIS", 3)
        self.symbol_table.add_entry("THAT", 4)
        self.symbol_table.add_entry("SCREEN", 16384)
        self.symbol_table.add_entry("KBD", 24576)

    def first_pass(self):

        line_num = 0
        while self.parser.has_more_commands():

            self.parser.advance()

            if self.parser.commandType() == "L_COMMAND":
                self.symbol_table.add_entry(self.parser.symbol(), line_num )

            elif self.parser.commandType() == "A_COMMAND":
                line_num += 1

            # C command
            else:
                line_num += 1

    def second_pass(self):  # actual translation
        # reset file stream to first line of file

        file = open("Prog.hack", "w")
        instructions = []
        ram_addr = 16

        while self.parser.has_more_commands():

            self.parser.advance()

            if self.parser.commandType() == "A_COMMAND":

                #IMPLEMENT the variable part!!!

                symbol = self.parser.symbol()

                if symbol.isdigit():
                    address = int(symbol) #its not  symbol
                else:
                    address = self.symbol_table.get_address(symbol)

                    if address is None: 
                        address = ram_addr
                        self.symbol_table.add_entry(symbol,ram_addr)
                        ram_addr+=1

                binary_address = format(int(address), "015b")

                instruction = "0" + binary_address

                instructions.append(instruction)

            elif self.parser.commandType() == "C_COMMAND":

                dest_bits = dest(self.parser.dest())

                comp_bits = comp(self.parser.comp())

                jmp_bits = jump(self.parser.jump())

                instruction = "111" + comp_bits + dest_bits + jmp_bits

                instructions.append(instruction)

            else:

                continue

        file.write("\n".join(instructions))
        file.close()

    def run(self):
        self.init_symbol_table()
        self.first_pass()
        self.parser.reset_stream()
        self.second_pass()


if __name__ == "__main__":
    # call the above functions

    input_file = sys.argv[1]

    assembler = Assembler(path=input_file)

    assembler.run()
