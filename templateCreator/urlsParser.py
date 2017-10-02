from HTMLParser import HTMLParser
import re

class UrlsParser(HTMLParser):
    def __init__(self, output_list=None):
        HTMLParser.__init__(self)
        self.tags = ['link','img','script']
        self.attributes = ['href','src']

        if output_list is None:
            self.output_list = []
        else:
            self.output_list = output_list

        self.internal_links = []
        self.external_links = []
    def handle_starttag(self, tag, attrs):
        if tag in self.tags:
        	for attr in self.attributes:
        		attr_value = dict(attrs).get(attr)
        		if attr_value:
        			self.output_list.append(attr_value)
        			if not(re.search(':\/\/', attr_value)):
        				self.internal_links.append(attr_value)
