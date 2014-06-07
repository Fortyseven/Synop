#!C:\DevTools\Python27\python
#!/usr/bin/python

#-------------------------------------------------------------------------------
# Name:        GenerateSummary
# Author:      Fortyseven
# Created:     01/06/2014
#-------------------------------------------------------------------------------

import sys, random, json, cgi
from SummaryConjoin import SummaryConjoin
from SummaryNFlix import SummaryNFlix
from SummaryAppendage import SummaryAppendage

summary_strings = None

def loadStrings():
    global summary_strings
    f = open("summaries.clean.txt", "rb")
    summary_strings = f.readlines()



def generateFrankensummary(type_arg):
    '''Choose a pair of candidate summaries.'''
    string1 = summary_strings[random.randrange(0, len(summary_strings))].strip()
    string2 = summary_strings[random.randrange(0, len(summary_strings))].strip()
    if type_arg == 'nflix':
        gen = SummaryNFlix()
    elif type_arg == 'conjoin':
        gen = SummaryConjoin()
    elif type_arg == 'append':
        gen = SummaryAppendage()

    return gen.generate(string1, string2)

def main():
    arguments = cgi.FieldStorage()

    if arguments.has_key('seed'):
        arg_seed = arguments['seed']
    else:
        arg_seed = random.randint(0, sys.maxint)

    if arguments.has_key('type'):
        arg_type = arguments['type']
    else:
        arg_type = "append"

    #if not type in ["conjoin", "nflix"]:
    #    exit()

    loadStrings()

    #seed = random.randint(0, sys.maxint)
    #arg_seed = 336901525
    #arg_seed = 575186328
    random.seed(arg_seed)
    #print "#################################"
    #print "Seed = "  + str(seed)
    #print "NEW: " +
    print "Content-type: text/html\n\n"

    # If generateFrankensummary() returns None, it means no words were common
    # between the chosen summaries; try again.
    for i in range(99):
        print "Try #%s" % (i)
        out,string1,string2 = generateFrankensummary(arg_type)
        if out: break

    seed_string = "\"seed\":" + json.dumps(arg_seed);
    type_string = "\"type\":" + json.dumps(arg_type);
    string1_string = "\"string1\":" + json.dumps(string1);
    string2_string = "\"string2\":" + json.dumps(string2);

    if not out:
        result_string = "ERROR GENERATING SPOOF";
    else:
        result_string = json.dumps(out)

    #print "{ \"result\":" + result_string + ", " + seed_string  + ", " + type_string + ", " + string1_string + ", " + string2_string + " }"
    print "{ \"result\":" + result_string + ", " + seed_string  + ", " + type_string + " }"

if __name__ == '__main__':
    main()