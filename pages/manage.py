#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import csv

from home.models import Term


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pages.settings')
    try:
        from django.core.management import execute_from_command_line
        # with open('../word_phrases_list.csv') as csvfile:
        #    reader = csv.DictReader(csvfile)
        #    for row in reader:
        #        term = Term(kanji=row['Japanese(Kanji)'], kana=row['Japanese(kana)'], roomaji=row['Roomaji'], english_text=row['English'])
        #       term.save()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
