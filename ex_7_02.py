# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    length=len(line)
    end=line[length-1]
    schar=line.find('0')
    first=line[schar-1]
    fresult=float(line[schar:])
    total=total+fresult
    avg=total/count
print("Average spam confidence:", avg)
