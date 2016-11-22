__author__ = 'tom'

from lxml import etree


filename = "hep-th.xgml"

tree = etree.parse(filename)
root = tree.getroot()

print root.tag
print "done",[ child.text for child in root ]

authors = {}

i=0
id=-1
for element in root.iterfind('section/section[@name="node"]'):  #('section/section/section[@name="node"]'):
    i=i+1
    print "  ------------------------------------------- "
    print i, element.tag,"|1|", element.attrib,"|2|", element.text
    for el1 in element.findall("attribute[@key='id']"):
        print el1.text, "|", el1.tag,"|", el1.attrib,"--------!"
    id = element.find("attribute[@key='id']").text
    author = element.find("attribute[@key='label']").text
    print "author, id", author, id
    for el2 in element.iterfind('attribute'):
        #print "||", el2.tag,"|",el2.attrib,"|text:", el2.text
        print el2.attrib['key'], ":", el2.text
        if el2.attrib['key']== "id":
            id = el2.text
        elif el2.attrib['key']== "label":
            author = el2.text
            authors[id] = author
    try:
        print "--", element.iterfind('attribute')[0].text#, element.find('attribute')[1]
    except:
        print "no"

print authors