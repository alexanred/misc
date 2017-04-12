#!/x/opt/pp/bin/python

import sys
import re
import operator 
import os

class FileRun:
   """Represents one file run """
   name = None
   count = None
   restricted = None
   tabCreated = None
   dbInsertError = None
   restart = None

   def __init__(self, name, count,restricted, tabCreated, dbInsertError, restart):
       self.name = name
       self.count = count
       self.restricted = restricted
       self.tabCreated = tabCreated
       self.dbInsertError = dbInsertError
       self.restart = restart

def processFile(filename):
    print "processing file name : " , filename
    f = open(filename, 'r')
    nameRegEx  =  re.compile(r'(file=)')
    successRegEx =  re.compile(r'(Process success Count\D*?:)')
    restrictedRegEx =  re.compile(r'(PAD restricted Count\D*?:)')
    tabCreatedRegEx =  re.compile(r'(Tab Creation Count\D*?:)')
    dbInsetErrorRegEx =  re.compile(r'(DB insert unique error\D*?:)')

    for lines in f:
        match = nameRegEx.search(lines)
        if match: 
             split = lines.split("=")
             name = split[1].strip()
             print "name:" , name
        match = successRegEx.search(lines)
        if match:
             split = lines.split(":")
             success = split[1].strip()
             print "success:" , success
        match = restrictedRegEx.search(lines)
        if match:
             split = lines.split(":")
             restrict = split[1].strip()
             print "restrict:" , restrict
        match = tabCreatedRegEx.search(lines)
        if match:
             split = lines.split(":")
             tab = split[1].strip()
             print "tab:" , tab
        match = dbInsetErrorRegEx.search(lines)
        if match:
             split = lines.split(":")
             db = split[1].strip()
             print "dbError" ,db 
     
    return FileRun(name,success,restrict,tab,db, None)

def process(fileprefix):
    print "processing with file prefix " , fileprefix
    count = 1
    list = []
    filename = fileprefix + str(count)
    while(os.path.isfile(filename)): 
      filerun = processFile(filename)
      list.append(filerun)
      failedfname = filename + ".failed"
      while(os.path.isfile(failedfname)):
          filerun = processFile(failedfname)
          list.append(filerun)
          failedfname = failedfname + ".failed"
      count = count + 1
      filename = fileprefix + str(count)
    print len(list)
    total = 0
    restricted = 0
    tabCount = 0
    dbErrorCount = 0
    for run in list:
        total = total + int(run.count)
        restricted = restricted + int(run.restricted)
        tabCount = tabCount+ int(run.tabCreated)
        dbErrorCount = dbErrorCount + int(run.dbInsertError)

    print "Total Enrolled   : " , total
    print "PAD Restricted   : " , restricted 
    print "TAB created count: " , tabCount 
    print "Already Enrolled : " , dbErrorCount 

def main():
  process(sys.argv[1])

if __name__ == '__main__':
  main()
