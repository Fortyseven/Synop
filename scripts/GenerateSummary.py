#!/usr/bin/python

#-------------------------------------------------------------------------------
# Name:        Generate
# Author:      Fortyseven
# Created:     01/06/2014
#-------------------------------------------------------------------------------

import sys, random, json
from FSStyle1 import FSStyle1

summary_strings = None

def loadStrings():
    global summary_strings
    f = open("summaries.clean.txt", "rb")
    summary_strings = f.readlines()



def generateFrankensummary():
    '''Choose a pair of candidate summaries.'''
    string1 = summary_strings[random.randrange(0, len(summary_strings))].strip()
    string2 = summary_strings[random.randrange(0, len(summary_strings))].strip()

    gen = FSStyle1()

    #print "#1 :" + string1
    #print "#2 :" + string2
    #print
    return gen.generate(string1, string2)

def main():
    loadStrings()
    #random.seed(0)
    seed = random.randint(0, sys.maxint)
    random.seed(seed)
    #print "#################################"
    #print "Seed = "  + str(seed)
    #print "NEW: " +
    print "Content-type: text/html\n\n"

    # If generateFrankensummary() returns None, it means no words were common
    # between the chosen summaries; try again.
    for i in range(10):
        out = generateFrankensummary();
        if out: break

    if not out:
        print "{ result: \"ERROR GENERATING SPOOF\"}"
    else:
        print "{ \"result\":" + json.dumps(out)+", \"seed\":" + str(seed)+"}"

if __name__ == '__main__':
    main()