fname = input("Enter file:")
try:
    fhandle=open(fname)
    if len(fname) < 1:
        fname="mbox-short.txt"
except:
    print('File cannot be opened:',fname)
    exit()

counts=dict()
email= None
for line in fhandle:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    words=line.split()
    if words[0] =="From:":
        continue
    email=words[1]
    counts[email]=counts.get(email,0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword= word
        bigcount= count
print (counts)
print(bigword, bigcount)
# counting From as well as when in From: figure out how to deal with that.
