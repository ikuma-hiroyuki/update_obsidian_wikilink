import argparse
import os
from pathlib import Path

from dotenv import load_dotenv

from update_link import update_wikilinks
from wiki_source import get_wiki_sources, WikiSource

parser = argparse.ArgumentParser(description='マークダウンファイル内のウィキリンクを更新する')
parser.add_argument('--all', '-a', action='store_true', help='多対多でウィキリンクを更新するか')
parser.add_argument('--specific', '-s', action='store_true',
                    help='一対多で更新するか(全てのファイルを対象に、指定したファイル名・エイリアス名に合致する文字列をウィキリンク化するか)')
parser.add_argument('--one', '-o', action='store_true',
                    help='一対一で更新するか(指定したファイル内の指定した文字列をウィキリンク化するか)')


def all_update():
    """全てのファイルに対して全てのWikiリンクの更新を行う"""
    for file in files:
        for wiki_file in get_wiki_sources():
            update_wikilinks(wiki_file, file)


def specific_update(wiki_file_path):
    """全てのファイルに対して指定したWikiリンクファイルで更新を行う"""
    wiki_file = WikiSource(Path(wiki_file_path))
    for file in files:
        update_wikilinks(wiki_file, file)


if __name__ == '__main__':
    args = parser.parse_args()
    load_dotenv()
    base_dir = Path(os.getenv("BASE_PATH"))
    if not args.one:
        files = [p for p in base_dir.rglob('*.md')]

    if args.all:
        all_update()
    elif args.specific:
        target_wiki_file = input('ウィキリンク化したいファイルパスを入力してください:\n')
        specific_update(target_wiki_file)
    elif args.one:
        target_file = input('被更新対象ファイルのパスを入力してください:\n')
        target_wiki_file = input(':\n')
        target_file_path = base_dir / target_file
        target_wiki_file_path = base_dir / target_wiki_file
        update_wikilinks(WikiSource(target_wiki_file_path), target_file_path)
    else:
        print('オプションは --all または --specified または --one で指定してください。')
