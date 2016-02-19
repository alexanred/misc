#!/x/opt/pp/bin/python

import sys
import re
import operator 

def Count(filename):
  d = {}
  chatRegex =  re.compile(r'(-\D*?:)')
  f = open(filename, 'r')
  for lines in f:
    match = chatRegex.search(lines)
    if match:
        if match.group(1) in d:
             d[match.group(1)] = d[match.group(1)] + 1
        else:
             d[match.group(1)] = 1
  f.close()
  for key, value in sorted(d.items(), key=operator.itemgetter(1), reverse=True):
      print("{} : {}".format(key, value))
def main():
  Count(sys.argv[1])

if __name__ == '__main__':
  main()
