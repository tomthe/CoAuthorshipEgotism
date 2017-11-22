__author__ = 'tom'

__author__ = 'tom'

from lxml import etree
from random import randint
print "start"
#filename of authorship-network-xml. generated with yED
#Data downloaded from ...
#filename = "hep-th.xgml"
filename = "tmp_dblp_coauthorship.json"

from json import load
with open(filename) as file:
    dblp = load(file)

print "loaded"
print dblp[3]
print dblp[3][1]
print dblp[3][1][0]
print dblp[3][1].split(' ')
print dblp[3][1].split(' ')[-1][0]
print "printed"

authors = {}        #id:"authorname"
firstLetters = {}   #id:"first letter of author"
firstFirstLetters = {}
i=0

letterDic = {}      # 'AA: n occurences (37 times both authors begin with A)
oneLetterCount = {} # 'A': n occurences of this first letter (1301)

#go through every author-author-connection and count the lettercombo 1 up
for element in dblp:  #('section/section/section[@name="node"]'):
    i=i+1
    author1 =  element[0].upper()
    author2 =  element[1].upper()

    letter1 = author1.split(' ')[-1][0]
    letter2 = author2.split(' ')[-1][0]

    # combine the two letters to a lettercombo so that it's always AB, never BA:
    if (ord(letter1) < ord(letter2)):
        firstLetterCombo = letter1 + letter2
    else:
        firstLetterCombo = letter2 + letter1
    #print source, target, authors[source], authors[target], "|", firstLetterCombo  #last name
    #count the number up:
    try:
        letterDic[firstLetterCombo] += 1
    except:
        letterDic[firstLetterCombo] = 1
    #count, how often every letter appears in the connections
    try:
        oneLetterCount[letter1] += 1
    except:
        oneLetterCount[letter1] = 1
    try:
        oneLetterCount[letter2] += 1
    except:
        oneLetterCount[letter2] = 1
    if i % 1000==0:
        print i

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
            print "%6d i%7.3f s%7.3f" % (int(letterDic.get(letterCombo, 0)), float(isOftennessOfLetterCombo), float(predictedOftennessOfLetterCombo)),
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

flLetterCombo = []
flPredicted = []
flIs = []
fl0 = []
colors = []

def printLetterDicAbsolute(letterDic):
    resulttxt = ""
    xxPredicted = 0
    xxIs = 0

    for i in xrange(65,91): #for every letter from A to Z:
        sum = 0
        aa = 0
        for j in xrange(65,91):
            letterCombo = chr(i)+chr(j)
            predictedOftennessOfLetterCombo = (float(oneLetterCount.get(chr(i))) /numberConnections) *(float(oneLetterCount.get(chr(j))) /numberConnections)  * numberConnections
            isOftennessOfLetterCombo = letterDic.get(letterCombo, 0.0)
            ratioIsVsPredicted = isOftennessOfLetterCombo/predictedOftennessOfLetterCombo
            print letterCombo,
            #try:
            sum += (int(letterDic.get(letterCombo,0)) + int(letterDic.get(letterCombo[::-1],0))) /2.0
            print "i%6d s%9.1f" % (int(letterDic.get(letterCombo, 0)), float(predictedOftennessOfLetterCombo)),
            if (ratioIsVsPredicted)> 1.4:
                print '\033[91m' + "r%4.2f" % (ratioIsVsPredicted), '\033[0m',
            elif ratioIsVsPredicted == 0:
                print '\033[1m' + "r%4.2f" % (ratioIsVsPredicted), '\033[0m',
            elif (ratioIsVsPredicted < 0.8):
                print '\033[92m' + "r%4.2f" % (ratioIsVsPredicted), '\033[0m',
            else:
                print '\033[1m' + "r%4.2f" % (ratioIsVsPredicted), '\033[0m',
            if i==j:
                aa = letterCombo
                aaratio = ratioIsVsPredicted
                xxIs += isOftennessOfLetterCombo
                xxPredicted += predictedOftennessOfLetterCombo
            print "|",
            if ratioIsVsPredicted > 0.0:
                flLetterCombo.append(letterCombo)
                flPredicted.append(predictedOftennessOfLetterCombo)
                flIs.append(isOftennessOfLetterCombo)
                fl0.append(0)
                if i==j:
                    colors.append('red')
                else:
                    colors.append('blue')
        print "|", aa,": %6.4f" % aaratio
        resulttxt += " | " + aa + ": %6.4f" % aaratio
    print resulttxt
    print "is/predicted: ", xxIs,xxPredicted,float(xxIs)/xxPredicted
    return float(xxIs)/xxPredicted

printLetterDicAbsolute(letterDic)


# plot is-should diagram:
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, LabelSet

sourcedict = {'flPredicted':flPredicted,'flIs':flIs,'flLetterCombo':flLetterCombo}

source = ColumnDataSource(data=dict(xx=flPredicted,
                                    yy=flIs,
                                    txt=flLetterCombo,
                                    oo=fl0))
output_file("authorship_dblp_00.html", title="implicit egotism example")
plot = figure(title ="jojo",width=1300, height=900,active_scroll='wheel_zoom')
plot.circle(x=flPredicted, y=fl0, size=5,fill_alpha=0.2, color=colors)


labels = LabelSet(x='xx', y='oo', y_offset=8,
                  text_font_size="8pt", text_color="#555555",
                  text='txt', source=source, text_align='center')
plot.add_layout(labels)

show(plot)