import var
import funcs

def out(line):
    with open("../cache/elang.c", "a") as file:
        if line.startswith('out('):
            start = line.find("out(") + 4

            if line[start] != '"':
                end = line.rfind(");")
                variable = line[start:end].strip()

                if var.checkVar(variable) == "int":
                    file.write(f'\tprintf("%d\\n", {variable});\n')
                elif var.checkVar(variable) == "string":
                    file.write(f'\tprintf("%s\\n", {variable});\n')
                else:
                    call_start = variable.find("(")
                    if call_start != -1:
                        name = variable[:call_start].strip()

                        if funcs.fnCheck(name) == "int":
                            file.write(f'\tprintf("%d\\n", {variable});\n')
                        elif funcs.fnCheck(name) == "str":
                            file.write(f'\tprintf("%s\\n", {variable});\n')
            else:
                end = line.rfind(");")

                content = line[start:end]

                file.write(f'\tprintf({content[:-1]}\\n");\n')
