#!/usr/bin/python3
# Test script to list journals
import urllib.request
from datetime import datetime
from xml.dom.minidom import parseString

from config import url_list, url_detail
from article import Article

class ProcessXML(object):
    """Main class that fetches XML and parses it"""
    results = []
    articles = []
    errors = []

    def __init__(self):
        try:
            xml = urllib.request.urlopen(url_list)
            dom = parseString(xml.read())
            self.results = dom.getElementsByTagName("result")
        except Exception as err:
            self.errors.append(err)
            print('Cannot open URL = %s' % url_list)

    def print_journals(self):
        """Test method to check we can get data"""
        journals = []
        for element in self.results:
            journal = element.getElementsByTagName('journalTitle')[0].firstChild.nodeValue
            if journal not in journals:
                journals.append(journal)
        for journal in journals:
            print(journal)

    def populate_articles(self):
        """Fetch data and create articles"""
        for result in self.results:
            self.articles.append(Article(result))

    def print_articles(self):
        """Output article data"""
        count = 0
        for article in self.articles:
            count += 1
            print(count)
            print(article.journal)
            print(' '.join(article.journal_issns))
            print(article.article_id)
            print(article.publication_date)
            print(article.title)
            print('----------------------------')

    def get_earliest(self):
        earliest = datetime(3000, 1, 1)
        for article in self.articles:
            yymmdd = article.publication_date.split('-')
            yymmdd = [int(part) for part in yymmdd]
            pub_date = datetime(*yymmdd)
            if pub_date < earliest:
                earliest = pub_date
        return earliest
            
    def get_summary(self):  
        out = 'Articles processed: %s\n' % len(self.articles)
        out += 'Earliest published: %s\n' % self.get_earliest()
        return out

    def log_errors(self):
        line = '%s,processed=%s,errors=%s\n' % (datetime.now(), len(self.articles), len(self.errors))        
        with open('processxml.log', 'a') as log:
            log.write(line)
    
    def output(self):
        """Run the output"""
        self.populate_articles()
        self.print_articles()
        print(self.get_summary())
        self.log_errors()
        
processXML = ProcessXML()
processXML.output()


