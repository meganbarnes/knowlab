from bs4 import BeautifulSoup
import urllib
import numpy as np
import pandas as pd
import string
#import nltk
from string import maketrans
import random

def get_soup(article):
    page = urllib.urlopen(article)
    return BeautifulSoup(page)
    
base_url = 'https://en.wikipedia.org/wiki/'

files = ['graded_files_updated/featured_articles.txt', 'graded_files_updated/a-class_articles.txt', 'graded_files_updated/good_articles.txt', 'graded_files_updated/b-class_articles.txt', 'graded_files_updated/c-class_articles.txt', 'graded_files_updated/start-class_articles.txt', 'graded_files_updated/stub-class_articles.txt']

names = []
soups = []
print "starting"

for fil in files:
    print fil
    lines = set(open(fil, 'r').readlines())
    lines = random.sample(lines, 400)
    for line in lines:
        line = line.strip()
        names.append(line)
        soup = get_soup(base_url+line)
        if soup is None:
            continue
        else:
            soups.append(soup)
      
out_names = open('names.txt', 'w')
out_soups = open('soups.txt', 'w')

for item in names:
    out_names.write("%s\n" % item)
for item in soups:
    out_soups.write("%s\n" % item)