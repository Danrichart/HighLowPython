import random


upper_limit = 100
lower_limit = 0
count = 0
match = False

print "Please think of a number between one and one hundred."
print "I'll guess your number."
print "You tell me if I'm too high, too low, or correct."
print "Good luck!"

while match == False:

    guess = ((upper_limit - lower_limit) / 2 ) + lower_limit
    print "I guess: %d" % guess
    response = raw_input("too (h)igh, too (l)ow, or (c)orrect?")
    
    if response == "h":
        upper_limit = guess - 1
        count+=1
    elif response == "l":
        lower_limit = guess + 1
        count+=1
    elif response == "c":
        match = True
    else:
        print "type either h for too high, l for too low, or c for correct"

print "I got it! It took %d turns" % count
exit_input = raw_input("Press enter to exit:")
        
   
    
