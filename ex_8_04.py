fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    word=line.split()
    for words in word:
        lst.append(words)
res_lst= []
for w in lst:
    if w not in res_lst:
        res_lst.append(w)
res_lst.sort()
print(res_lst)
