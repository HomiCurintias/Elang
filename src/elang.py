import sys
import pathlib
import transpiler
import os
import subprocess

if len(sys.argv) < 2:
    raise SystemExit(1)

path = pathlib.Path(sys.argv[1])
if not path.is_absolute():
    path = pathlib.Path.cwd() / path
path = path.resolve()

base = pathlib.Path(__file__).resolve().parent
root = base.parent
cache = root / "cache"
lib = root / "lib"

if not path.exists():
    raise SystemExit(1)

os.chdir(base)

if not cache.exists():
    cache.mkdir()

for file in cache.iterdir():
    if file.is_file():
        try:
            file.unlink()
        except:
            pass

file2 = open(path, "r", encoding="utf-8")
content = file2.read()
file2.close()

Cfile = open(cache / "elang.c", "w", encoding="utf-8")
Cfile.write('#include <stdio.h>\n#include <string.h>\nint main(void) {\n')
Cfile.close()

loaded = []
lines = content.splitlines()
for line in lines:
    line = line.strip()
    if line.startswith("include"):
        name = line.replace("include", "", 1).strip()
        if name.endswith(";"):
            name = name[:-1].strip()
        if (name.startswith('"') and name.endswith('"')) or (name.startswith("'") and name.endswith("'")):
            name = name[1:-1].strip()

        included = None

        p = pathlib.Path(name)
        if p.is_absolute() and p.exists():
            included = p
        else:
            for file in lib.iterdir():
                if file.is_file():
                    if file.stem == name or file.name == name or file.name == name + ".e":
                        included = file
                        break

        if included is None:
           print("not found")
        else:
            if str(included) not in loaded:
                file3 = open(included, "r", encoding="utf-8")
                transpiler.transpilate(file3.read())
                file3.close()
                loaded.append(str(included))

transpiler.transpilate(content)

Cfile2 = open(cache / "elang.c", "a", encoding="utf-8")
Cfile2.write("\n\treturn 0;")
Cfile2.write("\n}")
Cfile2.close()

exe = "result.exe"

try:
    build = subprocess.run(["gcc", "elang.c", "-o", exe], cwd=cache, check=False)
except FileNotFoundError:
    raise SystemExit(1)

if build.returncode != 0:
    raise SystemExit(build.returncode)

run = subprocess.run([str(cache / exe)], cwd=cache, check=False)
raise SystemExit(run.returncode)
