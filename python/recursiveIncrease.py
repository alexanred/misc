import time

MAX_RETRY = 5
SLEEP_MULTIPLIER = 1

def operation():
    print "performing operation"
    from random import randint
    if(randint(0,9) == 4):
        return True
    else:
        return False

def execute(level):
    if( level == MAX_RETRY):
        print "exiting for level ", MAX_RETRY, " retry finished"
        return False
    else:
       sleepValue = level * SLEEP_MULTIPLIER
       print "Executing Level" ,  level, " with sleep value", sleepValue
       time.sleep(sleepValue)
       result = operation()
       if( result == True):
           print "Execution success"
           return True
       else:
           print "Execution failure retrying"
           return execute(level+1)

if __name__ == '__main__':
  execute(0)
