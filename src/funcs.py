fns = {}

def makeFunc(line):
    line = line.strip()
    if not line.startswith("fn"):
        return

    signature_start = line.find("fn") + 2
    while signature_start < len(line) and line[signature_start] == " ":
        signature_start += 1

    namEnd = line.find("(", signature_start)
    if namEnd == -1:
        return

    head = line[signature_start:namEnd].strip()
    head_parts = head.split()
    if len(head_parts) != 2:
        return

    ret_type = head_parts[0]
    name = head_parts[1]

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

    if ret_type == "int":
        with open("../cache/elang.c", "a") as file:
            file.write(f"\tint {name}({params_c_str}) " + "{\n")

            fns[name] = "int"
    elif ret_type == "str":
        with open("../cache/elang.c", "a") as file:
            file.write(f"\tchar* {name}({params_c_str}) " + "{\n")

            fns[name] = "str"
    

def fnCheck(name):
    return fns.get(name, 0)