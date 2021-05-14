import re
import sys

def match (text, pat):
    patterns = ' '+pat
    text=' '+text
    adr={}
    patterns_mod=patterns
    i=1
    k=0
    while len(patterns) > i:
        if patterns[i] == patterns[i-1] and patterns[i]=='*':

            adr[k]=i
            k=k+1

        i=i+1

    m=len(adr)
    while m > 0:
        l=adr[m-1]

        patterns_mod = patterns_mod[:l] + patterns_mod[l+1:]
        m=m-1


    if len(patterns_mod)==3 and patterns_mod[1]!=text[1] and patterns_mod[2]=='*':
        return ('KO')
    #elif patterns_mod[0]=='*':

    elif patterns_mod=='*':
        return ('OK')
    #elif patterns_mod==
    elif re.search(patterns_mod, text):
        return ('OK')
    else:
        return ('KO')
if __name__ == "__main__":


    print(match(*sys.argv[1:]))