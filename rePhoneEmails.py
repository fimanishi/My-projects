#!/usr/bin/env python3

import re

def getPhones(text):
    getPhones = re.compile(r'''
                               \(?\b      # optional parenthesis
                               \d{3}
                               [)\- ]?    # location code numbers
                               \ ?
                               \d{3}    # first three numbers
                               [\- ]?   # optional separator
                               \d{4}\b    # last four numbers
                            ''', re.VERBOSE)
    phones = getPhones.findall(text)
    return phones

def getEmails(text):
    getEmails = re.compile(r'''
                            [\w\-.]+         # email name
                            @           # separator
                            \w+         # domain
                            \.\w{2,}       # . and type
                            ''', re.VERBOSE)
    emails = getEmails.findall(text)
    return emails


if __name__ == "__main__":
    print(getPhones("33789-281-9071 fhhfjs (4018) 384-2883 hfjsdfhusdifhsl 3378427482"))
    print(getEmails("fimanishi@gmail.com sbruble fima@getc.edu fjsjfkds@afjkds"))
