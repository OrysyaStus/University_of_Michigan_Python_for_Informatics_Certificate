#Asks for hours worked and the rate per hour, and computes total pay.

hours = raw_input('Enter hours:')
rate = raw_input('Enter rate per hour:')
pay = float(hours) * float(rate)
print pay
