import sys, random, re
from ISummaryGenerator import ISummaryGenerator

###############################################################################
class SummaryNFlix(ISummaryGenerator):
    '''Generates a frankensummary by attempting to simulate the overlapping of
       text close to how the actual bug worked.'''

    MAX_COL = 32

    def generate(self, string1, string2):
        # syn_a will be the shorter synopsis to be placed on top of syn_b
        if len(string1) > len(string2):
            syn_a = string2
            syn_b = string1
        else:
            syn_a = string1
            syn_b = string2

        #rows = [] #len(syn_b)/self.MAX_COL

        rows = []
        x = 0
        y = 0
        cur_row = ""

        for ch in syn_b:
            cur_row += ch
            x += 1
            if (x >= self.MAX_COL):
                x = 0
                y += 1
                rows.append(cur_row)
                cur_row = ""
        if cur_row:
            rows.append(cur_row)

        #print "Before: " + "".join(rows)

        x = 0
        y = 0
        cur_row = list(rows[y])
        for ch in syn_a:
            cur_row[x] = ch
            x += 1
            if (x >= self.MAX_COL):
                rows[y] = "".join(cur_row)
                x = 0
                y += 1
                cur_row = list(rows[y])
        if cur_row:
            rows[y] = "".join(cur_row)

        #print "Before: " + "".join(rows)

        return ("".join(rows), string1, string2)
