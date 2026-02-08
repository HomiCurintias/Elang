import sys
import pathlib
import transpiler
import os

path = sys.argv[1]

for file in pathlib.Path("../cache").iterdir():
    if file.is_file():
        file.unlink()

file2 = open(path, "r")

content = file2.read()

Cfile = open("../cache/elang.c", "w")
Cfile.write('#include <stdio.h>\n#include <string.h>\nint main(void) {\n')
Cfile.close()

transpiler.transpilate(content)

Cfile2 = open("../cache/elang.c", "a")
Cfile2.write("\n\treturn 0;")
Cfile2.write("\n}")
Cfile2.close()
file2.close()

os.system("cd ../cache && gcc elang.c -o result.exe && result.exe")