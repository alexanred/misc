import sys



def Count(filename):
  f = open(filename, 'r')
  sum = 0
  for lines in f:
    l = lines.split()
    k1 = l[0]
    k2 = l[1]    
    from datetime import datetime
    date_object1 = datetime.strptime(k1, '%H:%M:%S.%f')
    date_object2 = datetime.strptime(k2, '%H:%M:%S.%f')
    diff = date_object2 - date_object1
    sum = sum + diff.seconds*1000 + diff.microseconds/1000
    print (k1 , k2, diff.seconds*1000 + diff.microseconds/1000)    
  f.close()
  print("Average", sum/20)
def main():
  Count(sys.argv[1])

if __name__ == '__main__':
  main()
