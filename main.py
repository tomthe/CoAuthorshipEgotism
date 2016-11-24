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

def generateDic():
    pass


for element in root.iterfind('section/section[@name="edge"]'):  #('section/section/section[@name="node"]'):
    i=i+1
    source =  element.find("attribute[@key='source']").text
    target =  element.find("attribute[@key='target']").text
    if (ord(firstLetters[target])> ord(firstLetters[source])):
        firstLetterCombo = firstLetters[target] + firstLetters[source]
    else:
        firstLetterCombo = firstLetters[source] + firstLetters[target]
    #print source, target, authors[source], authors[target], firstLetterCombo

    try:
        letterDic[firstLetterCombo] += 1
    except:
        letterDic[firstLetterCombo] = 1


print letterDic

def printLetterDicNice(letterDic):
    for i in xrange(65,91): #for every letter from A to Z:
        sum = 0
        aa = 0
        for j in xrange(65,91):
            letterCombo = chr(i)+chr(j)
            print letterCombo,
            try:
                sum += (int(letterDic.get(letterCombo,0)) + int(letterDic.get(letterCombo[::-1],0))) /2.0
                print "%3d |" % (int(letterDic.get(letterCombo, 0)) + int(letterDic.get(letterCombo[::-1],0))),
                if i==j:
                    aa = int(letterDic.get(letterCombo, 0))
            except:
                print "  0 |",
        print "%3.1f|%3.1f" % (sum / 26.0, sum / 13.0),  #(durch 2 weil jedes doppelt gezaehlt wird)
        randomCombo = chr(randint(65,91)) + chr(randint(65,91))
        bx = int(letterDic.get(randomCombo, 0)) + int(letterDic.get(randomCombo[::-1], 0))

        print "!%3.1f|%3.1f  |%4.1f|%3.1f" % (aa, sum/26.0 - aa, bx, sum/26.0-bx)
printLetterDicNice(letterDic)