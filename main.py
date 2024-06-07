import os
import argparse
from pathlib import Path

from dotenv import load_dotenv

from update_link import update_wikilinks
from wiki_source import wiki_sources, WikiSource

parser = argparse.ArgumentParser(description='Update wikilinks in markdown files')
parser.add_argument('--all', '-a', action='store_true', help='Update all wikilinks in all files')
parser.add_argument('--specific', '-s', action='store_true',
                    help='Update wikilinks in all files with a specific wiki file.')

load_dotenv()
base_dir = Path(os.getenv("BASE_PATH"))
files = [p for p in base_dir.rglob('*.md')]


def all_update():
    """全てのファイルに対して全てのWikiリンクの更新を行う"""
    for file in files:
        for wiki_file in wiki_sources:
            update_wikilinks(wiki_file, file)


def specific_update(wiki_file_path):
    """全てのファイルに対して指定したWikiリンクファイルで更新を行う"""
    wiki_file = WikiSource(Path(wiki_file_path))
    for file in files:
        update_wikilinks(wiki_file, file)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.all:
        all_update()
    elif args.specific:
        target_wiki_file = input('Please specify the target wiki file: ')
        specific_update(target_wiki_file)
    else:
        print('Please specify the option with --all or --specific')
