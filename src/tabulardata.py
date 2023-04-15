#!/usr/bin/env python3

import json
from sys import argv

with open(argv[1]) as fo:
  data = json.load(fo)

# find min and max cell value
mn = mx = None
for y in data:
  for x in data[y]:
    value = float(data[y][x])
    if mn==None or value<mn: mn = value
    if mx==None or value>mx: mx = value

valuemapper = lambda v: int((float(v)-mn)/(mx-mn)*100)

xkeys = list(sorted(data[list(data.keys())[0]].keys()))
xs = len(xkeys)

lines = []
lines.append("\\begin{tabular}{l%s}" % ("c"*xs))
lines.append(" "+("".join(map(lambda key: " & "+key, xkeys)))+" \\\\")
for y in sorted(data.keys()):
  line = "  %s" % y
  for x in sorted(data[y].keys()):
    value = int(data[y][x])
    line += " &\cellcolor{green!%i!red}%i" % (valuemapper(value), value)
  lines.append(line+" \\\\")
lines.append("\\end{tabular}")

with open(argv[2], "w") as fo:
  fo.writelines("".join(map(lambda line: line+"\n", lines)))

print(data)
