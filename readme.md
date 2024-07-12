# Project Name

Wikiリンク更新

## Description

指定したmdファイルもしくは既存の全てのmdファイルで.env配下にある全てのmdファイル内で合致する文字列をWikiリンクに変換します。

## Usage

1. .envに `BASE_PATH=C:\Users\ikuma\Downloads\History` のように基準になるパスを設定します。
2. main.pyを実行します。\
    オプション
   1. --all : 多対多で更新 (全てのファイルをウィキリンク化)
   2. --specific: 一対多で更新 (ウィキリンク化したいファイルパスを指定)
   3. --one: 一対一で更新 (ウィキリンク化したいファイルパスと対象ファイルパスを指定)