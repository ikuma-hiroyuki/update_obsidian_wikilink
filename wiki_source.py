import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
base_path = Path(os.getenv("BASE_PATH"))


class WikiSource:
    """
    Wikiファイルを表すクラス
    """

    def __init__(self, path: Path):
        self._path = path
        self.title = path.stem
        self._aliases = self.get_aliases()
        self.target_words = {self.title: f'[[{self.title}]]', **self._aliases}

    def get_aliases(self):
        """
        ObsidianYAMLフロントマターの中からエイリアスを取得してリストに格納する

        YAML配下のようになっているので、aliases: という文字列を見つけたら、その後の行を取得してリストに格納する
        ---
        aliases:
          - 衆愚政治
          - 衆愚政策
        ---
        :return:
        """

        aliases = {}
        with open(self._path, 'r', encoding='utf-8') as f:
            is_aliases = False
            for line in f:
                if is_aliases:
                    if line.startswith('  - '):
                        alias = line.replace('  - ', '').strip()
                        wikilink_alias = f'[[{self.title}|{alias}]]'
                        aliases[alias] = wikilink_alias
                    else:
                        break
                if line.startswith('aliases:'):
                    is_aliases = True
        return aliases


wiki_sources = [WikiSource(p) for p in base_path.rglob('*.md')]

if __name__ == '__main__':
    for wiki_file in wiki_sources:
        print(wiki_file.title, wiki_file.target_words)
