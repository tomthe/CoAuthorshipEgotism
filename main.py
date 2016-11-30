__author__ = 'tom'

from lxml import etree
from random import randint
filename = "hep-th.xgml"

tree = etree.parse(filename)
root = tree.getroot()

authors = {}
firstLetters = {}
firstFirstLetters = {}
i=0
id=-1
#get the first letter of the last name for every scientist-ID:
for element in root.iterfind('section/section[@name="node"]'):  #('section/section/section[@name="node"]'):
    i=i+1
    id = element.find("attribute[@key='id']").text
    author = element.find("attribute[@key='label']").text
    authors[id] = author
    firstLetters[id] = author[0]
    try:
        firstFirstLetters[id] = author.split(", ")[1][0]
    except:
        print "i",i

#print authors
#print firstLetters
#print firstFirstLetters

letterDic = {}
oneLetterCount = {}

def generateDic():
    pass

#go through every author-author-connection and count the lettercombo 1 up
for element in root.iterfind('section/section[@name="edge"]'):  #('section/section/section[@name="node"]'):
    i=i+1
    source =  element.find("attribute[@key='source']").text
    target =  element.find("attribute[@key='target']").text
    if (ord(firstLetters[target]) < ord(firstLetters[source])):
        firstLetterCombo = firstLetters[target] + firstLetters[source]
    else:
        firstLetterCombo = firstLetters[source] + firstLetters[target]
    #print source, target, authors[source], authors[target], "|", firstLetterCombo
    try:
        letterDic[firstLetterCombo] += 1
    except:
        letterDic[firstLetterCombo] = 1
    try:
        oneLetterCount[firstLetters[source]] += 1
    except:
        oneLetterCount[firstLetters[source]] = 1
    try:
        oneLetterCount[firstLetters[target]] += 1
    except:
        oneLetterCount[firstLetters[target]] = 1

print "letterDic: ", letterDic
print "oneLetterCount: ", oneLetterCount


def getNConnections(oneLetterCount):
    sum = 0
    for val in oneLetterCount.itervalues():
        sum += val
        #print val
    #print sum
    return sum
numberConnections = getNConnections(oneLetterCount)
print numberConnections

def getRelativeOftenness(letter):
    oneLetterSum = oneLetterCount.get(letter,0.1)
    return float(oneLetterSum) / numberConnections

def printLetterDicNice(letterDic):
    for i in xrange(65,91): #for every letter from A to Z:
        sum = 0
        aa = 0
        for j in xrange(65,91):
            letterCombo = chr(i)+chr(j)
            predictedOftennessOfLetterCombo = 1000.0 * getRelativeOftenness(chr(i)) * getRelativeOftenness(chr(j))
            isOftennessOfLetterCombo = 1000.0 * int(letterDic.get(letterCombo, 0.022)) / numberConnections
            print letterCombo,
            #try:
            sum += (int(letterDic.get(letterCombo,0)) + int(letterDic.get(letterCombo[::-1],0))) /2.0
            print "%3d i%5.3f s%5.3f" % (int(letterDic.get(letterCombo, 0)), float(isOftennessOfLetterCombo), float(predictedOftennessOfLetterCombo)),
            if (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo)> 1.5:
                print '\033[91m' + "r%5.3f" % (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo), '\033[0m',
            elif (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo < 0.66):
                print '\033[92m' + "r%5.3f" % (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo), '\033[0m',
            else:
                print '\033[1m' + "r%5.3f" % (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo), '\033[0m',
            if i==j:
                aa = int(letterDic.get(letterCombo, 0))
            print "|",
        #except:
            #print "  0 |",
        print "%3.1f|%3.1f" % (sum / 26.0, sum / 13.0),  #(durch 2 weil jedes doppelt gezaehlt wird)
        randomCombo = chr(randint(65,91)) + chr(randint(65,91))
        bx = int(letterDic.get(randomCombo, 0)) + int(letterDic.get(randomCombo[::-1], 0))

        print "!%3.1f|%3.1f  |%4.1f|%3.1f" % (aa, sum/26.0 - aa, bx, sum/26.0-bx)
printLetterDicNice(letterDic)

def printLetterDicAbsolute(letterDic):
    for i in xrange(65,91): #for every letter from A to Z:
        sum = 0
        aa = 0
        for j in xrange(65,91):
            letterCombo = chr(i)+chr(j)
            predictedOftennessOfLetterCombo = (float(oneLetterCount.get(chr(i))) /numberConnections) *(float(oneLetterCount.get(chr(j))) /numberConnections)  * numberConnections
            isOftennessOfLetterCombo = letterDic.get(letterCombo, 0.0)
            print letterCombo,
            #try:
            sum += (int(letterDic.get(letterCombo,0)) + int(letterDic.get(letterCombo[::-1],0))) /2.0
            print "%3d i%5.1f s%5.1f" % (int(letterDic.get(letterCombo, 0)), float(isOftennessOfLetterCombo), float(predictedOftennessOfLetterCombo)),
            if (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo)> 1.4:
                print '\033[91m' + "r%5.2f" % (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo), '\033[0m',
            elif isOftennessOfLetterCombo/predictedOftennessOfLetterCombo == 0:
                print '\033[1m' + "r%5.3f" % (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo), '\033[0m',
            elif (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo < 0.8):
                print '\033[92m' + "r%5.3f" % (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo), '\033[0m',
            else:
                print '\033[1m' + "r%5.3f" % (isOftennessOfLetterCombo/predictedOftennessOfLetterCombo), '\033[0m',
            if i==j:
                aa = int(letterDic.get(letterCombo, 0))
            print "|",
        print " gogo!"

printLetterDicAbsolute(letterDic)