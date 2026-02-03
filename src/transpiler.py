import var
import out
import ifsys

def transpilate(txt):
    lines = txt.splitlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("var"):
            var.createVar(line)

        elif line.startswith("out("):
            out.out(line)

        elif line.startswith("if"):
            print(f"[DEBUG] IF LINE: {line!r}")
            ifsys.makeIf(line)
        
        elif line.startswith("} else"):
            with open("../cache/elang.c", "a") as file:
                file.write("\t}\n\telse \n\t{\n")

        elif line.startswith("else"):
            with open("../cache/elang.c", "a") as file:
                file.write("\telse \n\t{\n")

        elif line.startswith("}"):
            with open("../cache/elang.c", "a") as file:
                file.write("\t}\n")
