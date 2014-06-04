#!C:/DevTools/Python27/python
#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        Generate
# Purpose:
# Author:      Fortyseven
# Created:     01/06/2014
#-------------------------------------------------------------------------------

import sys, random, re, json

summary_strings = None

def loadStrings():
    global summary_strings
    f = open("summaries.clean.txt", "rb")
    summary_strings = f.readlines()

def findCommonWords(foo, bar):
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

def generateStyle1(string1, string2):
    common_words = findCommonWords(string1, string2)
    if not len(common_words): return None
    cword = common_words[random.randrange(0, len(common_words))]
    #print "cword = " + cword[0]
    newstring = string1[0:cword[1]] + string2[ cword[2]:]
    return newstring

def generateFrankensummary():
    string1 = summary_strings[random.randrange(0, len(summary_strings))].strip()
    string2 = summary_strings[random.randrange(0, len(summary_strings))].strip()
    #print "#1 :" + string1
    #print "#2 :" + string2
    #print
    return generateStyle1(string1, string2)

def main():
    loadStrings()
    #random.seed(0)
    seed = random.randint(0, sys.maxint)
    random.seed(seed)
    #print "#################################"
    #print "Seed = "  + str(seed)
    #print "NEW: " +
    print "Content-type: text/html\n\n"

    # If generateFrankensummary() returns None, it means no words were common between the chosen summaries; try again.
    for i in range(10):
        out = generateFrankensummary();
        if out: break

    if not out:
        print "{ result: \"ERROR GENERATING SPOOF\"}"
    else:
        print "{ \"result\":" + json.dumps(out)+", \"seed\":" + str(seed)+"}"

if __name__ == '__main__':
    main()