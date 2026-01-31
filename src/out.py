import var

def out(line):
    file = open("../cache/elang.c", "a")

    if line.startswith('out('):
        start = line.find("out(") + 4

        if start + 1 != '"':
            end = line.rfind(");") - 0
            variable = line[start:end]

            if var.checkVar(variable) == "int":
                file.write(f'\tprintf("%d\\n", {variable});\n')
            else:
                file.write(f'\tprintf("%s\\n", {variable});\n')
        else:
            content = line[start:end]

            file.write(f'\tprintf("{content}\\n");\n')