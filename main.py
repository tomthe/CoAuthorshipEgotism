__author__ = 'tom'

from lxml import etree


filename = "hep-th.xgml"

tree = etree.parse(filename)
root = tree.getroot()

authors = {}

i=0
id=-1
for element in root.iterfind('section/section[@name="node"]'):  #('section/section/section[@name="node"]'):
    i=i+1
    id = element.find("attribute[@key='id']").text
    author = element.find("attribute[@key='label']").text
    authors[id] = author

print authors