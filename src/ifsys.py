import var

sla = "{"

def makeIf(line):
    file = open("../cache/elang.c", "a")

    start = line.find("(")
    end = line.find(")")
    expression = line[start + 1:end]

    op = None
    for candidate in ["!=", "==", ">=", "<=", ">", "<"]:
        if candidate in expression:
            op = candidate
            break

    if not op:
        file.close()
        return

    left_raw, right_raw = expression.split(op, 1)
    left = left_raw.strip()
    right = right_raw.strip()

    is_left_string = left.startswith('"') and left.endswith('"')
    is_right_string = right.startswith('"') and right.endswith('"')

    left_type = var.checkVar(left)
    if left_type != "string":
        left_type = var.checkVar(left_raw)

    right_type = var.checkVar(right)
    if right_type != "string":
        right_type = var.checkVar(right_raw)

    is_string = is_left_string or is_right_string or left_type == "string" or right_type == "string"

    if is_string:
        if op == "==":
            file.write(f'\tif (strcmp({left}, {right}) == 0) {sla}\n')
        elif op == "!=":
            file.write(f'\tif (strcmp({left}, {right}) != 0) {sla}\n')
        file.close()
        return

    if op == "==":
        file.write(f'\tif ({left} == {right}) {sla}\n')
    elif op == "!=":
        file.write(f'\tif ({left} != {right}) {sla}\n')
    elif op == ">=":
        file.write(f'\tif ({left} >= {right}) {sla}\n')
    elif op == "<=":
        file.write(f'\tif ({left} <= {right}) {sla}\n')
    elif op == ">":
        file.write(f'\tif ({left} > {right}) {sla}\n')
    elif op == "<":
        file.write(f'\tif ({left} < {right}) {sla}\n')

    file.close()