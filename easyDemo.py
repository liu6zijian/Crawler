'''
Project: First spider demo
Author: Zijian Liu
'''
import requests # get information from URL
from bs4 import BeautifulSoup # transforn from HTML format to str
# F12开发人员选项，F5内容链接重新加载，箭头指定选取区域对应的Elements信息
res = requests.get('https://sports.sina.com.cn/basketball/nba/2020-01-04/doc-iihnzhha0201421.shtml')
res.encoding = 'utf-8' # 转码修改，防止中文乱码
soup = BeautifulSoup(res.text, 'html.parser') # 指定html解析器
# id 用 "#title", class 用 ".class", content 直接用 "content" 选取, .text 截取文本信息
[print(_.text) for _ in soup.select('.article')[0].select('p')]
