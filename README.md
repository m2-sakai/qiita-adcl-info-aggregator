# Qiita Advent Calendar いいね数集計ツール

## 概要

本ツールは Qiita Advent Calendar のいいね数やストック数を集計し、CSV に出力するツールです。

## 動作環境

本ツールは `python: 3.10.4` で実装されています。そのため、本ツールを実行する場合は事前に python をインストールしてください。

## 起動方法

1. 依存ライブラリをインストールします。

   ```bash
   pip install requests beautifulsoup4 pandas
   ```

2. `config.py` に取得したいカレンダー名を記載します。

   ```py
   # 年
   year="2023"

   # カレンダー名
   calendar_name="xxxxxx"
   ```

3. `main.py` を実行します。すると、`output` フォルダに CSV が出力されます。

   ```bash
   $ py main.py
   info: Advent Calendarのページを取得しました。 URL: https://qiita.com/advent-calendar/XXXX/YYYY]
   info: 全ての投稿者と記事URLを取得しました。[記事数: XX]
   info: 全ての記事の情報を取得しました。[記事数: XX]
   info: 結果をCSVに出力しました。[ファイル名: output/YYYY_XXXX_data.csv]
   ```
