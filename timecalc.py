hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40 :
    print (float(h) * float(r))
if h > 40 :
    print (((h-40) * (r * 1.50)) + float(40 * r))
