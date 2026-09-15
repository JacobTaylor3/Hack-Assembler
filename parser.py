class Parser:

    def __init__(self, path):
        self.stream = open(path, "r", encoding="utf-8")  # initalizes the file stream
        self.current_command = None
        self.next_command = None

    def reset_stream (self):
        self.stream.seek(0)

    def has_more_commands(self):

        # parse through the file and store next_command here, if present return true and populate next_command, otherwise None and return false
        # if this is false we exit out of the loop,advance is onl called when has_more_commands if true
        for line in self.stream:

            res = line.split("//")[0].strip()
            if res == "":
                continue

            self.next_command = res
            return True

        self.next_command = None
        return False
    

    def advance(self) -> None:
        self.current_command = self.next_command
        self.next_command = None

    def commandType(self):

        if self.current_command[0] == "@":
            return "A_COMMAND"

        elif self.current_command[0] == "(":
            return "L_COMMAND"

        else:
            return "C_COMMAND"

    def symbol(self) -> str:  # only called on A command or L command

        if self.commandType() == "A_COMMAND":
            return self.current_command.split("@")[1]

        return self.current_command.split("(")[1].split(")")[0]

    def dest(self) -> str:  # only called on C instruction

        if "=" in self.current_command:

            return self.current_command.split("=")[0]

        # no destination, jump
        return ""

    def comp(self) -> str:  # only called on C command

        # dest=comp;jmp
        # dest=comp
        # comp;jmp
        # comp

        if "=" in self.current_command and ";" in self.current_command:
            return self.current_command.split("=")[1].split(";")[0]

        elif "=" in self.current_command and not (";" in self.current_command):
            return self.current_command.split("=")[1]

        elif not ("=" in self.current_command) and ";" in self.current_command:
            return self.current_command.split(";")[0]

        else:
            # just comp
            return self.current_command

    def jump(self) -> str:  # only called on C command
        # comp;jmp
        if ";" in self.current_command:
            return self.current_command.split(";")[1]

        # otherwise no jump bits
        return ""
