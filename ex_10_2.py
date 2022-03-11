fname = input("Enter file:")
try:
    fhandle=open(fname)
    if len(fname) < 1:
        fname="mbox-short.txt"
except:
    print('File cannot be opened:',fname)
    exit()

counts=dict()
date= None
l=list()
for line in fhandle:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    words=line.split()
    if words[0] =="From:":
        continue
    date=words[5]
    delimiter = ':'
    date=date.split(delimiter)
    day=date[0]
    counts[day]=counts.get(day,0) + 1
for key, val in list(counts.items()):
    l.append( (key, val) )

l.sort()
for key, val in l[:25]:
    print(key, val)




    words=line.split(delimiter)
print(words)
    date=words[5]
days= None
for dates in date:
    delimiter=":"
    day


    counts[day]=counts.get(day,0) + 1
print (day)
