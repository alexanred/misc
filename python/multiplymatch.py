#!/usr/local/bin/python

import os
import sys
import fileinput


if(len(sys.argv) < 2):
        print 'pass the filename parameter'
        sys.exit(0);

textToSearch =  "timeout="


fileToSearch  = sys.argv[1];
#fileToSearch = 'D:\dummy1.txt'


for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
        line = line.strip(' \n\t\r')
        line = line + '00'
        print line
    else:
       print line
