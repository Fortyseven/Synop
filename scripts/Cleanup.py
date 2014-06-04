#-------------------------------------------------------------------------------
# Name:        Cleanup
# Purpose:
# Author:      Fortyseven
# Created:     01/06/2014
#-------------------------------------------------------------------------------

from sets import Set
import hashlib

known_hashes = []
acceptable_eos = Set(".?!")

def main():
    f = open("summaries.txt", "rb")
    out = open("summaries.clean.txt", "wb")

    count = 0
    reject = 0

    lines = f.readlines()
    for i, line in enumerate(lines):
        temp = line.replace("\n", "")
        if temp:
            eos = temp[len(temp)-1];
            if eos in acceptable_eos:
                hash = hashlib.md5(temp).hexdigest()
                if temp.find("An example of") > -1:
                    reject += 1
                    continue
                if temp.find("El Fuente") > -1:
                    reject+=1
                    continue
                #print hash
                if not (hash in known_hashes):
                    out.write(temp+"\n")
                    known_hashes.append(hash)
                    count += 1
                else:
                    reject += 1

    out.close()
    f.close()
    print("{2} entries; {0} unique; {1} rejected\n".format(count, reject, count+reject))

if __name__ == '__main__':
    main()