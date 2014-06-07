import sys, random, re
from ISummaryGenerator import ISummaryGenerator

class SummaryAppendage(ISummaryGenerator):
    '''Generates a frankensummary by appending the final sentence in one summary
       to the end of another summary.'''

    def generate(self, string1, string2):
        #perpos = string2.rfind('.')
        #string1 = string1.replace('?')
        print "string1  has " + str(string1.count('.'))
        print "string2  has " + str(string2.count('.'))
        if string1.count('.') > 1 and string2.count('.') > 1:
            pieces1 = string1.split('.')
            pieces2 = string2.split('.')
            result = " ".join( [ pieces1[0] + '.',  pieces2[len(pieces2)-2] + '.' ] )
        else:
            result = None

        return (result, string1, string2)