import sys, random, re
from ISummaryGenerator import ISummaryGenerator

class SummaryAppendage(ISummaryGenerator):
    '''Generates a frankensummary by appending the final sentence in one summary
       to the end of another summary.'''

    def generate(self, string1, string2):
        string1 = self.clean(string1)
        string2 = self.clean(string2)

        # Make sure there's at least two sentences in at least one summary to
        # increase the comedy potential
        if string1.count('.') > 0 and string2.count('.') > 1:
            pieces1 = string1.split('.')
            pieces2 = string2.split('.')
            result = " ".join( [ pieces1[0] + '.',  pieces2[len(pieces2)-2] + '.' ] )
        else:
            result = None

        return (result, string1, string2)


    def clean(self, string):
        ''' Does some common replacements to decrease garbage results.'''

        # so "U.S.S." becomes "USS", etc
        res = re.search('([A-Za-z0-9])\.([A-Za-z0-9])\.([A-Za-z0-9])\.', string)
        if res: string = string.replace(res.group(0), res.group(1) + res.group(2) + res.group(3))

        # so "D.C." becomes "DC", etc
        res = re.search('([A-Za-z0-9])\.([A-Za-z0-9])\.', string)
        if res: string = string.replace(res.group(0), res.group(1) + res.group(2))

        # Common replacements
        string = string.replace('Dr.', 'Doctor')
        string = string.replace('Capt.', 'Captain')

        return string