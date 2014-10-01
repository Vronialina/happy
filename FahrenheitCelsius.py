lower = 0
upper = 200
step = 5

cels = lower
while ( cels < upper ): 
    fahr = (9./5 * cels) + 32 # conversion
    print 'Celsius %6.1f = Fahrenheit %6.3f' % (cels , fahr) # formatierte Ausgabe
#    print "Celsius ", cels," = Fahrenheit ", fahr
    cels += step  # increment

# end of loop
