def computegrade(fscore):
    if fscore >= 0.9 and fscore <= 1.0:
        return ("A")
    elif fscore >= 0.8 and fscore < 0.9:
        return ("B")
    elif fscore >= 0.7 and fscore < 0.8:
        return ("C")
    elif fscore >= 0.6 and fscore < 0.7:
        return ("D")
    elif fscore < 0.6 and fscore > 0:
        return ("F")
    elif fscore < 0 or fscore > 1:
        print ('Error: Bad Score')
        quit()

score = input("Enter Score: ")
try:
	fscore=float(score)
except:
    print('Error: Please use number between 0 and 1')
    quit()
print ("Your grade result" , computegrade(fscore))
