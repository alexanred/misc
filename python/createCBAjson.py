#!/x/opt/pp/bin/python

import sys

#*{  "sqlQuery": "insert into wuser_legal_logging (account_number, type, time_created, flags, major_version, minor_version, pypl_time_touched, update_version, id) values (1522138149569934460, 'Q', 0, 232, 1, 0, 232, 0, 1212121212899)",  "enablePagination": false,  "convertedPaginationQuery": "",  "limit": 0,  "message": "",  "offset": 0}

def createJson(filename):
  f = open(filename, 'r')
  timeValue = 212121212128991000
  count = 1
  print "{ \"action\": [ { \"data\": \"http://jaws.paypalcorp.com/v1/QIJawsServices/#!/database\", \"evType\": \"redirect\", \"newValue\": \"\" }, { \"data\": \"#!/database/executeQuery\", \"evType\": \"redirect\", \"newValue\": \"\" },{ \"data\": \"ul#resources li.resource.active ul.endpoints li.endpoint ul.operations li.post.operation div.content form.sandbox table.fullwidth tbody.operation-params tr td INPUT.parameter\", \"evType\": \"change\", \"newValue\": \"msmaster.qa.paypal.com\" }, { \"data\": \"ul#resources li.resource.active ul.endpoints li.endpoint ul.operations li.post.operation div.content form.sandbox table.fullwidth tbody.operation-params tr td INPUT.parameter.required\", \"evType\": \"change\", \"newValue\": \"cloc\" }, "

  first = 0;
  for lines in f:
    if (first == 1 ) :
       print ","
    print "{ \"data\": \"ul#resources li.resource.active ul.endpoints li.endpoint ul.operations li.post.operation div.content form.sandbox table.fullwidth tbody.operation-params tr td TEXTAREA.body-textarea\", \"evType\": \"change\", \"newValue\":  "
    first = 1;
    count = count + 1
    timeValue = timeValue + 1
    l = lines.split(",")
    k1 = l[0]

#    print k1 , " " , timeValue
    print "\"{  \\\"sqlQuery\\\": \\\"insert into wuser_legal_logging (account_number, type, time_created, flags, major_version, minor_version, pypl_time_touched, update_version, id) values (", k1, ", 'Q', 0, 232, 1, 0, 232, 0,", timeValue,")\\\",  \\\"enablePagination\\\": false,  \\\"convertedPaginationQuery\\\": \\\"\\\",  \\\"limit\\\": 0,  \\\"message\\\": \\\"\\\",  \\\"offset\\\": 0}\", "
    print  " \"msgType\": \"userEvent\" }, { \"data\": \"ul#resources li.resource.active ul.endpoints li.endpoint ul.operations li.post.operation div.content form.sandbox div.sandbox_header INPUT.submit\", \"evType\": \"click\", \"newValue\": \"\" }, { \"data\": \"Please enter the time in milliseconds\", \"evType\": \"timer\", \"newValue\": \"2000\", \"msgType\": \"userEvent\" },"
    print " { \"data\":\"alert(\\\"hello\\\")\", \"evType\": \"bg-inject\", \"newValue\": \"\", \"name\": \"showLog\", \"msgType\": \"userEvent\" }"
  print " ], \"name\": \"project0\", \"level\": \"1\", \"isLeaf\": true, \"expanded\": false, \"loaded\": true } "
  f.close()

def main():
  createJson(sys.argv[1])

if __name__ == '__main__':
  main()
