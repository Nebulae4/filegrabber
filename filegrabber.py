from os import replace

def filereader(file):
  with open(r'%s' % file, 'r') as file: 
    data = file.read() 

  return str(data)

def searchtext(location, str):
  with open(r'%s' % location, 'r') as file:
    content = file.read()
    if str in content:
      return str in content
    else:
      return False

def replacetextatline(location, line, str, rstr):
  with open(r'%s' % location, 'a') as file:
    content = file.read()
    if str in content[line]:
      replace(str, rstr)
    else:
      return False

def searchline(location, str):
  with open(r'%s' % location, 'r') as file:
    line = file.readlines()
    content = file.read()
    if str in content:
      return line[str]
    else:
      return False

def filemodifer(file, str):
  with open(r'%s' % file, 'w') as file: 
    file.write(str)

def fileappender(file, str):
  with open(r'%s' % file, 'a') as file: 
    file.write(str)

def filespliter(file):
  with open(r'%s' % file, 'r') as file: 
    data = file.read()
    readabledata = str(data)
    a,b = readabledata.split("|")
    return a,b

def splitlist(list,amt):  
  data = str(list)
  for i in range(0,(amt + 1)):
    return data.split("|")
