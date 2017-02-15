import time

MAX_TRY = 5
SLEEP_MULTIPLIER = 1

def operation():
    print "performing operation"
    from random import randint
    if(randint(0,9) == 2):
        return True
    else:
        return False

def execute(level):
    if( level == 0):
        print "exiting for level 0 retry finished"
        return False
    else:
       sleepValue = (MAX_TRY - level) * SLEEP_MULTIPLIER
       print "Executing Level" ,  level, " with sleep value", sleepValue
       time.sleep(sleepValue)
       result = operation()
       if( result == True):
           print "Execution success"
           return True
       else:
           print "Execution failure retrying"
           return execute(level-1)

if __name__ == '__main__':
  execute(4)
