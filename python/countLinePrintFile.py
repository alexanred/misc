#!/x/opt/pp/bin/python
import os
import sys


def checkArgs(argv): 
	if len(argv) != 2 :
		print "missing or incorrect arguments"
		print "Usage: ", argv[0], "  <dir>"
		sys.exit(2)

def validateDir(dir):
	if os.path.exists(dir) == False:
		print "The specified directory :" , dir , " does not exist"
		sys.exit(3)

def printAttributeUsage(attribute):
	for y in attribute.keys():
		print y,":", len(attribute[y])
	print "*****************************"
	for y in attribute.keys():
		print y, ":"
		for name in attribute[y]:
			print "	", name
	

def processDir(dir):
	attribute = {}
	for root, directories, filenames in os.walk(dir):
		for filename in filenames:
			afilename = os.path.join(root,filename)
			f = open(afilename, 'r')
			for line in f:
				line = line.strip()
				if len(line) and ( line[0] == '-' or line[0] == '#' ):
 					continue
				values = line.split(':')
				if len(values) > 1 :
					print values[0]
					if values[0] in attribute.keys():
						if afilename not in attribute[values[0]]:
							attribute[values[0]].append(afilename)
					else:
						attribute[values[0]] = [afilename]
			f.close()
	printAttributeUsage(attribute)
	
def main():
	checkArgs(sys.argv)
	rootDir = sys.argv[1]
	validateDir(rootDir)
	processDir(rootDir)

if __name__ == "__main__":
   main()
