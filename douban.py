'''
Project: Douban film spider demo
Author: Zijian Liu
'''
import requests # get information from URL
from bs4 import BeautifulSoup # transforn from HTML format to str
import csv
# F12开发人员选项，F5内容链接重新加载，箭头指定选取区域对应的Elements信息
headers = {
    'Cookie':'OCSSID=4df0bjva6j7ejussu8al3eqo03',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                 '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

# when the requests.text is empty, please add the argument headers
def getURLInfo(url):
    res = requests.get(url, headers = headers)
    res.encoding = 'utf-8' # 转码修改，防止中文乱码
    soup = BeautifulSoup(res.text, 'html.parser') # 指定html解析器
    scores = soup.select('.comment-info')
    comments = soup.select('.short')
    for score, comment in zip(scores, comments):
        score = score.select('span')[1]['title']
        with open('FilmComment.csv', "a+", newline='', encoding='utf-8-sig') as file:
            csv_file = csv.writer(file)
            datas = [u'%s'%(score), u'%s'%(comment.text)]
            csv_file.writerow(datas)
        # print(score, comment.text)
    return soup



res = requests.get('https://movie.douban.com/chart', headers = headers)
res.encoding = 'utf-8' # 转码修改，防止中文乱码
soup = BeautifulSoup(res.text, 'html.parser') # 指定html解析器
# print(soup.select('.pl2')[0].select('a')[0]['href'])

for _ in soup.select('.pl2'):
    subURL = _.select('a')[0]['href']
    filmName = _.select('a')[0].text
    print(filmName + "\t" + subURL)
    soup = getURLInfo(subURL)
    
    # print(score, comment.text)
    
# # id 用 "#title", class 用 ".class", content 直接用 "content" 选取, .text 截取文本信息
# [print(_.text) for _ in soup.select('.article')[0].select('p')]