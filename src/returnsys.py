def makeReturn(line):
    start = line.find("(") + 1
    end = line.find(");")

    with open("../cache/elang.c", "a") as file:
        file.write(f'\treturn {line[start:end]};\n')