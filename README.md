# Qiita Advent Calender いいね数集計ツール

## 概要

本ツールは Qiita Advent Calender のいいね数やストック数を集計し、CSV に出力するツールです。

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
   calender_name= "xxxxxx"
   ```

3. `main.py` を実行します。すると、`output` フォルダに CSV が出力されます。

   ```bash
   $ py main.py

   ```
