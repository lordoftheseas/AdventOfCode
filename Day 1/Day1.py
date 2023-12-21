import csv

def helpingadv(val):
  acc = ""
  for x in val:
      if x.isdigit():
          acc += x
  retval = acc[0] + acc[len(acc)-1]
  return retval

def advCode(rfile):
  acc = []
  justint = []
  with open(rfile) as file:
    reader = csv.reader(file)
    for lines in reader:
      acc.extend(lines)
  for i in acc:
      justint.append(int(helpingadv(i)))
  total = sum(justint)
  return total

print(advCode("data.txt")) #56042