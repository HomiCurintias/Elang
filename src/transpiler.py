import var
import out
import ifsys

def transpilate(txt):
    file = open("../cache/elang.c", "a")

    lines = txt.splitlines()

    for line in lines:
        line = line.strip()

        if line.startswith("var"):
            var.createVar(line)
        elif line.startswith("out("):
            out.out(line)
        elif line.startswith("if"):
            ifsys.makeIf(line)
        
        
        if line == "}":
            file.write("\t}\n")
        
        if not line:
            continue
