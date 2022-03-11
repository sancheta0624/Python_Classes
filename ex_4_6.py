def computepay(h, r):
    if h <= 40 :
        return (float(h) * float(r))
    if h > 40 :
        return (((h-40) * (r * 1.50)) + float(40 * r))


hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter Rate:")
r=float(rate)

p = computepay(h, r)
print("Pay", p)
