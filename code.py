def dest(dest_mnemonic) -> str:

    if dest_mnemonic == "":
        return "000"
    elif dest_mnemonic == "M":
        return "001"
    elif dest_mnemonic == "D":
        return "010"
    elif dest_mnemonic == "MD" or dest_mnemonic == "DM":
        return "011"
    elif dest_mnemonic == "A":
        return "100"
    elif dest_mnemonic == "AM":
        return "101"
    elif dest_mnemonic == "AD":
        return "110"
    else:
        return "111"


def comp(comp_mnemonic) -> str:

    # a = 0 computations
    if comp_mnemonic == "0":
        return "0101010"
    elif comp_mnemonic == "1":
        return "0111111"
    elif comp_mnemonic == "-1":
        return "0111010"
    elif comp_mnemonic == "D":
        return "0001100"
    elif comp_mnemonic == "A":
        return "0110000"
    elif comp_mnemonic == "!D":
        return "0001101"
    elif comp_mnemonic == "!A":
        return "0110001"
    elif comp_mnemonic == "-D":
        return "0001111"
    elif comp_mnemonic == "-A":
        return "0110011"
    elif comp_mnemonic == "D+1":
        return "0011111"
    elif comp_mnemonic == "A+1":
        return "0110111"
    elif comp_mnemonic == "D-1":
        return "0001110"
    elif comp_mnemonic == "A-1":
        return "0110010"
    elif comp_mnemonic == "D+A":
        return "0000010"
    elif comp_mnemonic == "D-A":
        return "0010011"
    elif comp_mnemonic == "A-D":
        return "0000111"
    elif comp_mnemonic == "D&A":
        return "0000000"
    elif comp_mnemonic == "D|A":
        return "0010101"

    # a = 1 computations
    elif comp_mnemonic == "M":
        return "1110000"
    elif comp_mnemonic == "!M":
        return "1110001"
    elif comp_mnemonic == "-M":
        return "1110011"
    elif comp_mnemonic == "M+1":
        return "1110111"
    elif comp_mnemonic == "M-1":
        return "1110010"
    elif comp_mnemonic == "D+M":
        return "1000010"
    elif comp_mnemonic == "D-M":
        return "1010011"
    elif comp_mnemonic == "M-D":
        return "1000111"
    elif comp_mnemonic == "D&M":
        return "1000000"
    elif comp_mnemonic == "D|M":
        return "1010101"

def jump(jmp_mnemonic) -> str:

    if jmp_mnemonic == "":
        return "000"
    elif jmp_mnemonic == "JGT":
        return "001"
    elif jmp_mnemonic == "JEQ":
        return "010"
    elif jmp_mnemonic == "JGE":
        return "011"
    elif jmp_mnemonic == "JLT":
        return "100"
    elif jmp_mnemonic == "JNE":
        return "101"
    elif jmp_mnemonic == "JLE":
        return "110"
    else:
        return "111"
    
