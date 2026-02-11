import var
import funcs

sla = "{"

def _operand_type2(raw):
    token = raw.strip()

    if token.startswith('"') and token.endswith('"'):
        return "string"

    checked = var.checkVar(token)
    if checked:
        return checked

    checked_raw = var.checkVar(raw)
    if checked_raw:
        return checked_raw

    call_start = token.find("(")
    call_end = token.rfind(")")
    if call_start > 0 and call_end > call_start:
        fn_name = token[:call_start].strip()
        fn_type = funcs.fnCheck(fn_name)
        if fn_type == "str":
            return "string"
        if fn_type == "int":
            return "int"

    return 0

def makeWhile(line):
    start = line.find("(")
    end = line.rfind(")")
    if start == -1 or end == -1 or end <= start:
        return
    expression = line[start + 1:end]

    op = None
    for candidate in ["!=", "==", ">=", "<=", ">", "<"]:
        if candidate in expression:
            op = candidate
            break

    if not op:
        return

    left_raw, right_raw = expression.split(op, 1)
    left = left_raw.strip()
    right = right_raw.strip()

    left_type = _operand_type2(left_raw)
    right_type = _operand_type2(right_raw)
    is_string = left_type == "string" or right_type == "string"

    with open("../cache/elang.c", "a") as file:
        if is_string:
            if op == "==":
                file.write(f'\twhile (strcmp({left}, {right}) == 0) {sla}\n')
            elif op == "!=":
                file.write(f'\twhile (strcmp({left}, {right}) != 0) {sla}\n')
            return

        if op == "==":
            file.write(f'\twhile ({left} == {right}) {sla}\n')
        elif op == "!=":
            file.write(f'\twhile ({left} != {right}) {sla}\n')
        elif op == ">=":
            file.write(f'\twhile ({left} >= {right}) {sla}\n')
        elif op == "<=":
            file.write(f'\twhile ({left} <= {right}) {sla}\n')
        elif op == ">":
            file.write(f'\twhile ({left} > {right}) {sla}\n')
        elif op == "<":
            file.write(f'\twhile ({left} < {right}) {sla}\n')