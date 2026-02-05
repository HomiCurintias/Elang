fns = []

def makeFunc(line):
    line = line.strip()
    if not line.startswith("fn"):
        return

    fn_start = line.find("fn") + 2
    while fn_start < len(line) and line[fn_start] == " ":
        fn_start += 1

    namEnd = line.find("(")
    if namEnd == -1:
        return
    name = line[fn_start:namEnd].strip()

    paramsEnd = line.rfind(")")
    if paramsEnd == -1 or paramsEnd < namEnd:
        return

    params_raw = line[namEnd + 1:paramsEnd].strip()

    params_c = []
    if params_raw:
        parts = [p.strip() for p in params_raw.split(",")]
        for p in parts:
            if not p:
                continue
            pieces = p.split()
            if len(pieces) < 2:
                continue
            p_type = pieces[0]
            p_name = " ".join(pieces[1:])

            if p_type == "int":
                params_c.append(f"int {p_name}")
            elif p_type == "str":
                params_c.append(f"char {p_name}[]")
            else:
                params_c.append(p)

    params_c_str = ", ".join(params_c) if params_c else "void"

    with open("../cache/elang.c", "a") as file:
        file.write(f"\tint {name}({params_c_str}) " + "{\n")

    fns.append(name)

def fnCheck(name):
    if name in fns:
        return 1
    else:
        return 0
