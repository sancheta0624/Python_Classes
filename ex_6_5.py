text = "X-DSPAM-Confidence:    0.8475"
length=len(text)
last=text[length-1]
schar=text.find('0')
first=text[schar-1]
fresult=float(text[schar:])
print (fresult)
