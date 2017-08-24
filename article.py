"""Class to hold article data"""

class Article(object):
    """An article with data required"""
    journal = ''
    journal_issns = []
    article_id = ''
    publication_date = ''
    title = ''

    def __init__(self, result):
        """Parse result and get its data"""
        self.journal = result.getElementsByTagName('journalTitle')[0].firstChild.nodeValue
        issns = result.getElementsByTagName('journalIssn')[0].firstChild.nodeValue
        self.journal_issns = issns.split(';')
        self.article_id = result.getElementsByTagName('doi')[0].firstChild.nodeValue
        if not self.article_id:
            self.article_id = result.getElementsByTagName('pmcid')[0].firstChild.nodeValue            
        self.publication_date = result.getElementsByTagName('firstPublicationDate')[0].firstChild.nodeValue
        self.title = result.getElementsByTagName('title')[0].firstChild.nodeValue
