from pathlib import Path

from wiki_source import WikiSource


def update_wikilinks(source: WikiSource, target: Path):
    """
    読み込んだテキストの中に target_word があった場合その言葉を [[]] で囲んで保存する。ただし、すでに [[]] で囲まれている場合は何もしない
    :param source: WikiSource 元になるWikiファイル
    :param target: Path 対象ファイルのパス
    """

    if source.title == target.stem:
        return

    with open(target, 'r+', encoding='utf-8') as f:
        text = f.read()
        if any(wikilink in text for wikilink in source.target_words.values()):
            return

        f.seek(0)
        lines = ''
        is_updated = False
        for line in f:
            for target_word, wikilink in source.target_words.items():
                if not is_updated and wikilink not in line and target_word in line:
                    line = line.replace(f'**{target_word}**', target_word)
                    line = line.replace(f'*{target_word}*', target_word)
                    line = line.replace(target_word, wikilink)
                    print(f'【{target_word}】 is updated in 【{target}】')
                    is_updated = True
                    break
            lines += line
        f.seek(0)
        f.write(lines)
