number = 7
hiddenNumber= int(raw_input("Please enter your number:  "))
if hiddenNumber==number:
    print "Congratulations, you are the WINNER!"
elif hiddenNumber==6 or hiddenNumber==8:
    print "Uuuu, very close but not correct"
else:
    print "Sorry, you lost"
