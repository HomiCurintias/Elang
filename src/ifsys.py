import var

sla = "{"

def makeIf(line):
    file = open("../cache/elang.c", "a")

    start = line.find("(")
    end = line.find(")")
    expression = line[start + 1:end]

    if line[start + 1] == '"':
        if "==" in expression:
            start2 = line.find('("')
            end2 = line.rfind('" ==')
            string = line[start2:end2]

            if line[start2 + 1] == '"':
                start3 = line.find('== "') + 3
                end3 = line.rfind('")')
                string2 = line[start3:end3]

                file.write(f'\tif (strcmp{string}", {string2}") == 0) {sla}\n')
        elif "!=" in expression:
            start2 = line.find('("')
            end2 = line.rfind('" ==')
            string = line[start2:end2]

            if line[start2 + 1] == '"':
                start3 = line.find('== "') + 3
                end3 = line.rfind('")')
                string2 = line[start3:end3]

                file.write(f'\tif (strcmp{string}", {string2}") == 1) {sla}\n')
    if line[start + 1] != '"':
        if "==" in expression:
            start2 = line.find("(")
            end2 = line.rfind(")")

            content = line[start2:end2]

            file.write(f'\tif ({content}) {sla}\n')
        elif "!=" in expression:
            start2 = line.find("(") + 1
            mid = line.find("!=")
            end2 = line.rfind(")")

            content = line[start2:mid:end2]

            file.write(f'\tif ({content})) {sla}\n')