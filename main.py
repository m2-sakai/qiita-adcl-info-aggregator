import config
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_info(url):
	"""
	qiita記事のURLをスクレイピングし、いいね数やストック数等の情報を抽出する。
	"""
	if re.search('https\://qiita\.com',url):
		res = requests.get(url)
		soup = BeautifulSoup(res.content, 'html.parser')
		title = soup.find('h1',{'class':'style-wo2a1i'}).text
		tags = [x.text for x in soup.find_all('a',{'class':'style-1a4ckru'})]
		num_likes = soup.find('div',{'class':'style-2pgeei'}).text
		num_stocks = soup.find('div',{'class':'style-krcte5'}).text
		return title, tags, num_likes, num_stocks
	else:
		print(f'URLを確認してください: {url}')
		return 0

# 1. Advent Calendarのカレンダーページにアクセス
url = f"https://qiita.com/advent-calendar/{config.year}/{config.calender_name}"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
print("info: Advent Calenderのページを取得しました。 URL: " + url + "]")

# 2. 担当者と記事のURLを抽出する
content = soup.find("div", {"class": 'style-1covvrn'})
series = content.find_all("tbody", {"class": 'style-azrjx0'})
authors=[]
urls=[]

for calender in series:
	authors += [x.text.rstrip() for x in calender.find_all("a", {"class":'style-zzg0i9'})]
	urls += [x.find('a').get('href') for x in calender.find_all("div", {"class":'style-1dctyxx'})]
print("info: 全ての投稿者と記事URLを取得しました。[記事数: " + str(len(authors)) + "]")

# 3. 個別の記事の情報を取得（複数記事記載している場合があるため、キーは記事のURL）
qiita_info_dic = {}
for author, url in zip(authors, urls):
	title, tags, num_likes, num_stocks = extract_info(url)
	qiita_info_dic[url] = [
		author,
		title,
		tags,
		num_likes,
		num_stocks
	]
print("info: 全ての記事の情報を取得しました。[記事数: " + str(len(authors)) + "]")

# 4. pandas DataFrameにし、CSV化する
output_file_name=f'output/{config.calender_name}_{config.year}_data.csv'
df = pd.DataFrame.from_dict(qiita_info_dic, orient='index').sort_values(0,ascending=False).reset_index()
df.columns = ['URL','投稿者','タイトル','タグ','いいね数','ストック数']
df.to_csv(output_file_name, index=False, encoding='utf-8')
print("info: 結果をCSVに出力しました。[ファイル名: " + output_file_name + "]")
