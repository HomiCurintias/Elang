import var
import out
import ifsys
import funcs
import returnsys
import whilesys

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
            ifsys.makeIf(line)
        
        elif line.startswith("} else"):
            with open("../cache/elang.c", "a") as file:
                file.write("\t}\n\telse \n\t{\n")

        elif line.startswith("else"):
            with open("../cache/elang.c", "a") as file:
                file.write("\telse \n\t{\n")
        
        elif line.startswith("fn"):
            funcs.makeFunc(line)

        elif line.startswith("}"):
            with open("../cache/elang.c", "a") as file:
                file.write("\t}\n")
        
        elif line.startswith("return"):
            returnsys.makeReturn(line)
        
        elif line.startswith("while"):
            whilesys.makeWhile(line)

        else:
            with open("../cache/elang.c", "a") as file:
                try:
                    end = line.find("(")

                    name = line[:end]

                    if funcs.fnCheck(name) != 0:
                        file.write(f'\t{line}\n')
                except:
                    end = line.rfind("=") - 1

                    name = line[:end]

                    if var.checkVar(name) != "":
                        file.write(f'\t{line}\n')
