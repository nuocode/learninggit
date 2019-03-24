from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.douban.com/").text
soup = BeautifulSoup(html,"html.parser")
# print(soup.prettify())

#找到第一个p标签
# first_para = soup.find("p")
# print(first_para)
# para_title = soup.title
# print(para_title)
# print("第一个p节点class内容：",soup.p["class"])
# print("所有a节点：",soup.find_all("a"))
print(soup.text)

#结合有道的cnblogs继续写爬虫
