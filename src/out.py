import var

def out(line):
    file = open("../cache/elang.c", "a")

    if line.startswith('out('):
        start = line.find("out(") + 4

        if line[start] != '"':
            end = line.rfind(");") - 0
            variable = line[start:end]

            if var.checkVar(variable) == "int":
                file.write(f'\tprintf("%d\\n", {variable});\n')
            elif var.checkVar(variable) == "string":
                file.write(f'\tprintf("%s\\n", {variable});\n')
            else:
                file.write(f'\tprintf("%d\\n", {variable});\n')
        else:
            end = line.rfind(");") - 0

            content = line[start:end]

            file.write(f'\tprintf({content[:-1]}\\n");\n')