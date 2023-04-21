#!/usr/bin/env python3

import json

filename = "../var/csvheader.csv"

def parse_file (filename, sep=","):
  entries = []
  
  with open(filename) as fo:
    lines = list(map(str.strip, fo.readlines()))
    header = []
    
    for linei in range(len(lines)):
      line = lines[linei]
      
      if len(line)>0 and line[0]=="#":
        header = []
        cols = list(map(str.strip, line[1:].split(sep)))
        for i in range(len(cols)):
          header.append(cols[i])
      else:
        entry = {}
        cols = list(map(str.strip, line.split(sep)))
        for i in range(len(cols)):
          col = cols[i]
          
          if len(header)<i:
            print("Error: Unable to parse header index %u on line %u" % (i, linei))
            return None
          
          entry[header[i]] = col
        entries.append(entry)
  
  return entries

parsed = parse_file(filename)
print(json.dumps(parsed, indent=4, sort_keys=True))
