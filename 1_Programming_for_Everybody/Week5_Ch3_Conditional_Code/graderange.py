# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

num = raw_input('Enter an integer between 0.0 and 1.0: ')

try:
    n = float(num)
    if n < 0.6:
        print 'F'
    elif n < 0.7:
        print 'D'
    elif n < 0.8:
        print 'C'
    elif n < 0.9:
        print 'B'
    elif n <= 1.0:
        print 'A'
    else: n = -1
except:
    print 'Error message, enter an integer between 0.0 and 1.0'
    quit()

#Expected output: B