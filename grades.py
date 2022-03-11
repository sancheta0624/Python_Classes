score = input("Enter Score: ")
try:
	fscore=float(score)
except:
    print('Error: Please use number between 0 and 1')
    quit()
if fscore >= 0.9 and fscore < 1.0:
    print ("A")
elif fscore >= 0.8 and fscore < 0.9:
    print ("B")
elif fscore >= 0.7 and fscore < 0.8:
    print ("C")
elif fscore >= 0.6 and fscore < 0.7:
    print ("D")
elif fscore < 0.6 and fscore > 0:
    print ("F")
elif fscore < 0 or fscore > 1:
	print ('Error: Please enter number between 0 and 1')


    
