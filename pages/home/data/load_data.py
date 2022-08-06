import csv

from home.models import Term

with open('../word_phrases_list.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        term = Term(kanji=row['Japanese(Kanji)'], kana=row['Japanese(kana)'], roomaji=row['Roomaji'], english_text=row['English'])
        term.save()
