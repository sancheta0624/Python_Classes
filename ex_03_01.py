hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error: Please use numerical input')
    quit()
print(h, r)
if h <= 40 :
    print ('Pay:',float(h) * float(r))
if h > 40 :
    print ('Pay:',((h-40) * (r * 1.50)) + float(40 * r))
