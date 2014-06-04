#-------------------------------------------------------------------------------
# Name:        Page Skimmer
# Author:      Fortyseven
# Created:     31/05/2014
#-------------------------------------------------------------------------------

HOST = "instantwatcher.com"    #0000

import sys, httplib
from HTMLParser import HTMLParser

output = open("summaries.txt", "wb")

class MyHtmlParser(HTMLParser):
    #tag = None
    #attrs = None
    mProperTag = False
    mHandled = False

    def handle_starttag(self, tag, attrs):
        self.mProperTag = False
        if tag == "dd":
            for name, val in attrs:
                if (name == "class"):
                    if (val == "synopsis"):
                        self.mProperTag = True

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self.mProperTag == True and not self.mHandled:
            output.write(data.strip() + "\n")
            self.mHandled = True

def main():
    parse = MyHtmlParser()

    for i, s in enumerate(range(0,10000)):
        segment = "{0:04d}".format(i)
        conn = httplib.HTTPConnection(HOST, 80)
        conn.request("GET", "/titles/19"+segment)
        response = conn.getresponse()
        print "Fetching 19" + segment

        if (response.status == 200):
            parse.mHandled = False
            contents = response.read()
            parse.feed(contents)

    output.close()


if __name__ == '__main__':
    main()