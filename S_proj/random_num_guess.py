isCorrect = False
attemps = 0
while isCorrect == False:
    a = int(input("Random No. between 10 \n"))
    attemps = attemps + 1
    if a == 7:
        isCorrect = True
        print("Correct guess Well Done you guessed it in "+ str(attemps) +" attemps")
