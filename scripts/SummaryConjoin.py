import sys, random, re

from ISummaryGenerator import ISummaryGenerator

###############################################################################
class SummaryConjoin(ISummaryGenerator):
    '''Generates a frankensummary by finding common words between two random
    synopsiseseses and uses a random one of them as a break point to join the
    two.'''
    def generate(self, string1, string2):
        common_words = self.findCommonWords(string1, string2)
        if not len(common_words): return None
        cword = common_words[random.randrange(0, len(common_words))]
        #print "cword = " + cword[0]
        newstring = string1[0:cword[1]] + string2[ cword[2]:]
        return newstring

    def findCommonWords(self, foo, bar):
        words = []

        # go through each word in the summary and find the words both strings
        # have in common; we'll use those as splitting points
        for i, word in enumerate(foo.split(' ')):
            # Regex to make sure we don't get words inside of other words; we also
            # get the offset of the match
            res = re.search("\\b("+re.escape(word)+")\\b", bar);
            if res:
                if not word in words:
                    # Get offset of the word from original string
                    foo_res = re.search("\\b("+re.escape(word)+")\\b", foo);

                    # Save the word, the offset in the first string, and the
                    # offset in the second string
                    words.append([word, foo_res.start(), res.start()])
        return words