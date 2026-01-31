import var
import out

def transpilate(txt):
    file = open("../cache/elang.c", "a")

    lines = txt.splitlines()

    for line in lines:
        line = line.strip()

        if line.startswith("var"):
            var.createVar(line)
        elif line.startswith("out("):
            out.out(line)
        
        if line == "}":
            file.write("\t}")
        
        if not line:
            continue
