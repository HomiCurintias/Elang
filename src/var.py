variables = {}

def createVar(line):
    file = open("../cache/elang.c", "a")

    if "var int" in line:
        start = line.find("int ") + 4
        end = line.rfind("=", start)
        name = line[start:end]
        valStart = line.find("=") + 1
        valEnd = line.rfind(";")
        value = line[valStart:valEnd].strip()

        file.write(f'\tint {name}= {value};\n')

        file.close()

        variables[name] = "int";
    elif "var str" in line:
        start = line.find("str ") + 4
        end = line.rfind("=", start)
        name = line[start:end]
        valStart = line.find("=") + 1
        valEnd = line.rfind(";")
        value = line[valStart:valEnd].strip()

        file.write(f'\tchar {name}[]= {value};\n')

        file.close()

        variables[name] = "string";

def checkVar(name):
    try:
        return variables[name]
    except:
        return 0