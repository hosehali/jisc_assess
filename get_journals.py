#!/usr/bin/python
from xml.dom.minidom import parseString
import urllib2
url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=OPEN_ACCESS:y'
xml = urllib2.urlopen(url)
dom = parseString(xml.read())
results = dom.getElementsByTagName("result")
for element in results:
    print element.getElementsByTagName('journalTitle')[0].firstChild.nodeValue





