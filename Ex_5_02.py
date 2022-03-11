largest=None
smallest=None
while True:
    num=input("Enter a number: ")
    try:
        fnum= float (num)
        if largest is None:
            largest=fnum
        elif smallest is None:
            smallest=fnum
        elif fnum < smallest:
            smallest=fnum
        elif fnum > largest:
            largest=fnum
    except:
        if num == 'done':
            print ("Maximum is", int(largest))
            print ("Minimum is", int(smallest))
            quit()
        print("Invalid input")
        continue
